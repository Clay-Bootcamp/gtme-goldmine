#!/usr/bin/env python3
"""Score Clay.com demo requests against the ICP rubric. CSV-only, deterministic.

Implements lead_scorer.md exactly. Appends lead_score / fit_label / justification.

Usage:
    python3 score_leads.py [input.csv]

If no input is given, the newest *.csv in this folder (excluding *_scored.csv) is
scored. Output is written next to the input as <name>_scored.csv.
"""
import csv
import glob
import os
import re
import sys

# Columns the rubric reads. The scorer fails loudly if any are missing.
REQUIRED_COLUMNS = ["title", "company", "industry", "employees",
                    "funding_stage", "est_arr", "Tech Stack"]

OUTBOUND = {"outreach", "salesloft", "apollo", "instantly"}
CRM_STRONG = {"salesforce", "hubspot"}
CRM_OTHER = {"pipedrive"}
GTM_INDUSTRIES = {"b2b saas", "enterprise tech", "professional services"}
GTM_TITLE_KEYWORDS = ["sales", "revops", "rev ops", "revenue", "growth", "gtm",
                      "marketing ops", "sales op", "marketing manager"]
SERIES_AC = {"series a", "series b", "series c"}


def parse_arr_millions(s):
    """Return ARR in $M, or None if not a numeric dollar figure."""
    s = s.strip().replace("$", "").replace("+", "").replace(",", "")
    m = re.match(r"([0-9.]+)\s*([MB])", s, re.I)
    if not m:
        return None
    val = float(m.group(1))
    if m.group(2).upper() == "B":
        val *= 1000
    return val


def parse_stack(s):
    return [t.strip().lower() for t in s.split(",") if t.strip()]


def score_row(row):
    stack = parse_stack(row["Tech Stack"])
    industry = row["industry"].strip().lower()
    title = row["title"].strip().lower()
    employees = int(row["employees"].replace(",", "").strip())
    stage = row["funding_stage"].strip().lower()
    arr = parse_arr_millions(row["est_arr"])

    # Signal 1 — outbound tooling (0-3)
    n_outbound = sum(1 for t in OUTBOUND if any(t == s for s in stack))
    s1 = 3 if n_outbound >= 2 else (2 if n_outbound == 1 else 0)

    # Signal 2 — CRM (0-2)
    if any(c in stack for c in CRM_STRONG):
        s2 = 2
    elif any(c in stack for c in CRM_OTHER):
        s2 = 1
    else:
        s2 = 0

    # Signal 3 — company size (0-2)
    if 50 <= employees <= 500:
        s3 = 2
    elif (30 <= employees < 50) or (500 < employees <= 800):
        s3 = 1
    else:
        s3 = 0

    # Signal 4 — stage + ARR (0-2)
    stage_ok = stage in SERIES_AC
    arr_ok = arr is not None and 5 <= arr <= 100
    s4 = (1 if stage_ok else 0) + (1 if arr_ok else 0)

    # Signal 5 — industry + persona (0-1)
    industry_ok = industry in GTM_INDUSTRIES
    persona_ok = any(k in title for k in GTM_TITLE_KEYWORDS)
    s5 = 1 if (industry_ok and persona_ok) else 0

    raw = s1 + s2 + s3 + s4 + s5

    # Disqualifier caps
    caps = []
    if industry not in GTM_INDUSTRIES:
        caps.append(3)
    if employees < 10 or stage in {"pre-seed", "bootstrapped"}:
        caps.append(3)
    if employees >= 5000:
        caps.append(4)

    final = raw
    if caps:
        final = min(final, min(caps))
    final = max(1, final)

    if final >= 8:
        label = "Very good fit"
    elif final >= 5:
        label = "Good fit"
    else:
        label = "Not a good fit"

    breakdown = dict(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, raw=raw,
                     caps=caps, n_outbound=n_outbound, final=final)
    return final, label, breakdown


def justify(row, b):
    """Build a 1-2 line justification from the breakdown."""
    parts = []
    # Outbound + CRM framing (the dominant signals)
    if b["s1"] == 3:
        parts.append("running a full outbound motion")
    elif b["s1"] == 2:
        parts.append("some outbound tooling")
    else:
        parts.append("no outbound tooling")
    if b["s2"] == 2:
        parts.append("CRM in place (Salesforce/HubSpot)")
    elif b["s2"] == 1:
        parts.append("a basic CRM")
    else:
        parts.append("no CRM")

    firm = f"{row['employees']} emp, {row['funding_stage']}, {row['est_arr']} ARR, {row['industry']}"

    cap_note = ""
    if b["caps"]:
        reasons = []
        industry = row["industry"].strip().lower()
        emp = int(row["employees"].replace(",", "").strip())
        stage = row["funding_stage"].strip().lower()
        if industry not in GTM_INDUSTRIES:
            reasons.append("non-ICP industry")
        if emp < 10 or stage in {"pre-seed", "bootstrapped"}:
            reasons.append("too small/early")
        if emp >= 5000:
            reasons.append("enterprise/slow procurement")
        cap_note = f" Capped as Not-a-good-fit ({', '.join(reasons)})."

    return f"{firm}; {parts[0]}, {parts[1]}.{cap_note}".strip()


def pick_newest_csv():
    candidates = [
        f for f in glob.glob("*.csv")
        if not f.endswith("_scored.csv")
    ]
    if not candidates:
        sys.exit("No CSV found in this folder to score.")
    return max(candidates, key=os.path.getmtime)


def main():
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        infile = pick_newest_csv()

    if not os.path.exists(infile):
        sys.exit(f"Input file not found: {infile}")

    base, _ = os.path.splitext(infile)
    outfile = base + "_scored.csv"

    with open(infile, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    missing = [c for c in REQUIRED_COLUMNS if c not in (fieldnames or [])]
    if missing:
        sys.exit(
            f"CSV is missing required column(s): {', '.join(missing)}.\n"
            f"Expected schema includes: {', '.join(REQUIRED_COLUMNS)}."
        )

    print(f"Scoring {infile} ({len(rows)} rows) -> {outfile}\n")
    out_fields = list(fieldnames) + ["lead_score", "fit_label", "justification"]
    results = []
    for row in rows:
        score, label, b = score_row(row)
        row["lead_score"] = score
        row["fit_label"] = label
        row["justification"] = justify(row, b)
        results.append((row, b))

    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for row, _ in results:
            writer.writerow(row)

    # Console summary, sorted by score desc
    results.sort(key=lambda x: x[0]["lead_score"], reverse=True)
    print(f"{'Score':>5}  {'Label':<14}  {'Company':<18}  {'Breakdown (ob/crm/size/sa/ind = raw -> final)'}")
    print("-" * 100)
    for row, b in results:
        bd = f"{b['s1']}/{b['s2']}/{b['s3']}/{b['s4']}/{b['s5']} = {b['raw']}"
        if b["caps"]:
            bd += f" cap{min(b['caps'])}"
        print(f"{row['lead_score']:>5}  {row['fit_label']:<14}  {row['company']:<18}  {bd} -> {b['final']}")


if __name__ == "__main__":
    main()
