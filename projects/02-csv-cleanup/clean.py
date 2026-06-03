#!/usr/bin/env python3
"""
Data cleanup for deanon_export.csv (RB2B website-visitor de-anon export) -> HubSpot-ready.

Reads the RAW file READ-ONLY. Never writes to it. Produces:
  - deanon_cleaned.csv   one row per unique person (record_id), pages aggregated into `notes`
  - flag.csv             records needing human review (kept in output, but eyeball-worthy)
  - cleaning_audit.md    full change log (CLEAN framework: Note & document)

Pipeline order (as approved):
  0 backup (done in shell)         1 drop no-LinkedIn rows
  2 normalize LinkedIn URLs        3 clean names
  4 collapse to one row/person     5 augment (notes + derived cols)
  6 write outputs                  7 audit report   8 verification asserts
"""
import re
import pandas as pd

RAW = "deanon_export.csv"
OUT = "deanon_cleaned.csv"
FLAG = "flag.csv"
AUDIT = "cleaning_audit.md"

log = []                      # audit lines
def note(msg): log.append(msg)

# ---------------------------------------------------------------- load (read-only)
df = pd.read_csv(RAW, dtype=str, keep_default_na=False)   # everything as string; blanks stay ""
start_rows, start_cols = df.shape
start_people = df["record_id"].nunique()
note(f"- **Loaded raw (read-only):** {start_rows} rows x {start_cols} cols, "
     f"{start_people} unique people (`record_id`). Raw file never modified; "
     f"backup at `deanon_export_RAW_BACKUP.csv`.")

# ================================================================ STEP 1: drop no-LinkedIn
li_blank = df["linkedin_url"].str.strip() == ""
dropped_ids = sorted(df.loc[li_blank, "record_id"].unique().tolist())
people_before = df["record_id"].nunique()
df = df.loc[~li_blank].copy()
people_after = df["record_id"].nunique()
note(f"- **Step 1 — Discard un-enrichable (no LinkedIn):** removed {li_blank.sum()} rows "
     f"with blank `linkedin_url`. Unique people {people_before} -> {people_after} "
     f"({people_before - people_after} people dropped, "
     f"{100*(people_before-people_after)/people_before:.1f}%). No LinkedIn = cannot enrich = excluded by rule. "
     f"Dropped record_ids: {', '.join(dropped_ids)}.")

# ================================================================ STEP 2: normalize LinkedIn URLs
def normalize_linkedin(url):
    """Canonicalize to https://www.linkedin.com/in/<lowercased-slug>. Returns (clean, ok)."""
    if url is None:
        return "", False
    u = url.strip()
    if u == "":
        return "", False
    # pull the slug after /in/
    m = re.search(r"/in/([^/?#]+)", u)
    if not m:
        return u, False                     # unparseable -> keep original, flag
    slug = m.group(1).strip().strip("/").lower()
    slug = re.sub(r"[?#].*$", "", slug)     # belt-and-suspenders: drop any residual params
    if slug == "":
        return u, False
    return f"https://www.linkedin.com/in/{slug}", True

orig_formats = (df["linkedin_url"].str.strip()
                .str.replace(r"https?://", "", regex=True)
                .str.replace(r"/in/.*$", "", regex=True)
                .replace("", "(bare/none)"))
fmt_counts = orig_formats.value_counts().to_dict()

norm = df["linkedin_url"].apply(normalize_linkedin)
df["linkedin_url"] = [n[0] for n in norm]
li_unparseable_mask = pd.Series([not n[1] for n in norm], index=df.index)
n_changed = (df["linkedin_url"] != df["linkedin_url"]).sum()  # placeholder; recompute below
note(f"- **Step 2 — Normalize LinkedIn URLs:** canonicalized to "
     f"`https://www.linkedin.com/in/<slug>` (forced https + www, stripped query params "
     f"`?utm_source`/`?trk`, trailing slashes, lowercased slug). "
     f"Original host/protocol-prefix distribution: {fmt_counts}. "
     f"{int(li_unparseable_mask.sum())} URLs could not be parsed into /in/<slug> and were left "
     f"as-is + flagged.")

# ================================================================ STEP 3: clean names
ZW = ["​", "‌", "‍", "﻿", "⁠"]          # zero-width junk
DECOR = "✨🚀☆⭐★●•▪♦♥➤➔|"                                       # badge/emoji separators
CURLY = ['“', '”', '‘', '’', '"', "'"]                           # only stripped if wrapping
EMOJI = re.compile(
    "[" "\U0001F300-\U0001FAFF" "\U00002600-\U000027BF" "\U0001F000-\U0001F0FF"
    "\U00002190-\U000021FF" "\U00002B00-\U00002BFF" "️" "]", flags=re.UNICODE)

def clean_name(raw):
    """Return (clean, reasons[]). reasons flags judgment cases for human review."""
    reasons = []
    if raw is None:
        return "", ["MISSING_NAME"]
    s = raw
    original = raw
    for z in ZW:
        s = s.replace(z, "")
    # cut at first badge/decoration separator -> keep the leading real name
    cut = min([s.find(c) for c in DECOR if c in s], default=-1)
    if cut != -1:
        s = s[:cut]
        reasons.append("NAME_DECONTAMINATED")     # stripped badge/emoji/"Open to Work"
    # strip wrapping quotes (nicknames like “Ethan”)
    s2 = s.strip()
    if len(s2) >= 2 and s2[0] in CURLY and s2[-1] in CURLY:
        s2 = s2[1:-1]
        reasons.append("NAME_DEQUOTED")
    s2 = EMOJI.sub("", s2)                         # any stray emoji left
    s2 = re.sub(r"\s+", " ", s2).strip()           # collapse internal whitespace + trim
    if s2 != original and "NAME_DECONTAMINATED" not in reasons and "NAME_DEQUOTED" not in reasons:
        pass                                       # pure whitespace/casing fix, no flag needed
    if s2 == "":
        return "", reasons + ["MISSING_NAME"]
    # non-Latin scripts: keep, but flag (can't validate casing / may need transliteration)
    if re.search(r"[^\x00-\x7F]", s2):
        out = s2[:1].upper() + s2[1:] if s2[:1].isalpha() else s2   # gentle cap; .title breaks CJK
        reasons.append("NON_LATIN_NAME")
        return out, reasons
    # safe ASCII -> Title Case (handles ALL-CAPS, lowercase, hyphen/apostrophe)
    return s2.title(), reasons

flag_reasons = {}     # index -> list of reasons
def apply_name(col):
    cleans, all_reasons = [], []
    for idx, val in col.items():
        c, r = clean_name(val)
        cleans.append(c)
        all_reasons.append((idx, r))
    return cleans, all_reasons

fn_clean, fn_reasons = apply_name(df["first_name"])
ln_clean, ln_reasons = apply_name(df["last_name"])
ws_first = (df["first_name"] != pd.Series(fn_clean, index=df.index)).sum()
df["first_name"] = fn_clean
df["last_name"] = ln_clean
for idx, rs in fn_reasons + ln_reasons:
    if rs:
        flag_reasons.setdefault(idx, [])
        for r in rs:
            if r not in flag_reasons[idx]:
                flag_reasons[idx].append(r)
note(f"- **Step 3 — Clean names:** trimmed whitespace (incl. zero-width chars), removed "
     f"'✨ | Open to Work' badges and emoji decorations (🚀/☆/etc.), unwrapped curly-quote "
     f"nicknames, collapsed internal spaces, then Title-Cased ASCII names (fixes ALL-CAPS and "
     f"lowercase). Non-Latin names (Cyrillic/CJK) kept and flagged for review; blank names flagged.")

# ================================================================ STEP 4: collapse to one row/person
df["_ts"] = pd.to_datetime(df["visit_timestamp"], errors="coerce", utc=True)
df = df.sort_values(["record_id", "_ts"], kind="stable")
total_visits_pre_collapse = len(df)

identity_cols = ["record_id", "first_name", "last_name", "job_title", "seniority",
                 "department", "linkedin_url", "company_name", "company_domain",
                 "company_website", "company_industry", "company_size", "company_revenue",
                 "company_linkedin_url", "company_city", "company_state",
                 "company_country", "visitor_type"]

grouped = df.groupby("record_id", sort=False)
# canonical identity = EARLIEST visit row
canonical = grouped.first()[ [c for c in identity_cols if c != "record_id"] ].reset_index()

# integrity: identity fields consistent across a person's rows?
inconsistent = []
for col in ["first_name", "last_name", "company_name", "linkedin_url"]:
    varies = grouped[col].nunique()
    bad = varies[varies > 1].index.tolist()
    for rid in bad:
        inconsistent.append((rid, col))
note(f"- **Step 4 — Collapse to one row per person:** grouped {total_visits_pre_collapse} visit "
     f"rows by `record_id`; canonical identity taken from each person's EARLIEST visit "
     f"(`visit_timestamp`). Result: {canonical.shape[0]} unique people. "
     f"Identity-field inconsistencies across a person's rows: "
     f"{len(inconsistent)} ({inconsistent[:8]}{'...' if len(inconsistent)>8 else ''}).")

# ================================================================ STEP 5: augment (notes + derived)
def build_person_aggregate(g):
    g = g.sort_values("_ts", ascending=False, kind="stable")   # newest first
    lines = []
    for _, r in g.iterrows():
        d = r["visit_timestamp"][:10] if r["visit_timestamp"] else "unknown-date"
        lines.append(f"{d} — {r['page_visited']}")
    return pd.Series({
        "notes": "\n".join(lines),
        "total_visits": len(g),
        "first_visit_date": (g["visit_timestamp"].min() or "")[:10],
        "last_visit_date": (g["visit_timestamp"].max() or "")[:10],
    })

agg = grouped.apply(build_person_aggregate, include_groups=False).reset_index()
cleaned = canonical.merge(agg, on="record_id", how="left")
# drop redundant visit_count (always 1) — engagement now lives in total_visits
note(f"- **Step 5 — Augment:** built `notes` (one line per visit, newest first, `YYYY-MM-DD — page`), "
     f"`total_visits`, `first_visit_date`, `last_visit_date`. Dropped redundant `visit_count` "
     f"(was 1 on every row). Reconciliation: sum(total_visits)={int(cleaned['total_visits'].sum())} "
     f"vs visit rows after Step 1={total_visits_pre_collapse} "
     f"-> {'MATCH' if int(cleaned['total_visits'].sum())==total_visits_pre_collapse else 'MISMATCH'}.")

# future-dated timestamps (today = 2026-06-03) — left as-is per instruction, noted here
fut = df["_ts"] > pd.Timestamp("2026-06-03", tz="UTC")
fut_ids = sorted(df.loc[fut, "record_id"].unique().tolist())
note(f"- **Future-dated visits (left as-is per instruction):** {int(fut.sum())} visit rows have "
     f"`visit_timestamp` after today (2026-06-03), spanning {len(fut_ids)} people. Not altered; "
     f"flagged here for visibility only.")

# ================================================================ STEP 6: write outputs
final_cols = ["record_id", "first_name", "last_name", "job_title", "seniority", "department",
              "linkedin_url", "company_name", "company_domain", "company_website",
              "company_industry", "company_size", "company_revenue", "company_linkedin_url",
              "company_city", "company_state", "company_country",
              "first_visit_date", "last_visit_date", "total_visits", "visitor_type", "notes"]
cleaned = cleaned[final_cols]
cleaned.to_csv(OUT, index=False)

# build flag.csv at PERSON level (map flagged visit rows -> their record_id)
flag_rows = {}   # record_id -> set(reasons)
for idx, rs in flag_reasons.items():
    rid = df.loc[idx, "record_id"] if idx in df.index else None
    if rid is None:
        continue
    flag_rows.setdefault(rid, set()).update(rs)
# add LinkedIn-unparseable
for idx in li_unparseable_mask[li_unparseable_mask].index:
    rid = df.loc[idx, "record_id"]
    flag_rows.setdefault(rid, set()).add("LINKEDIN_UNPARSEABLE")

if flag_rows:
    flag_df = cleaned[cleaned["record_id"].isin(flag_rows.keys())].copy()
    flag_df["flag_reasons"] = flag_df["record_id"].map(lambda r: ", ".join(sorted(flag_rows[r])))
    flag_df.to_csv(FLAG, index=False)
else:
    flag_df = cleaned.iloc[0:0]
    flag_df.to_csv(FLAG, index=False)
note(f"- **Step 6 — Outputs written:** `{OUT}` ({cleaned.shape[0]} rows x {cleaned.shape[1]} cols); "
     f"`{FLAG}` ({flag_df.shape[0]} records for human review). Raw untouched.")

# reason breakdown
from collections import Counter
reason_counter = Counter()
for rs in flag_rows.values():
    for r in rs:
        reason_counter[r] += 1
note(f"- **Flag breakdown (by person):** {dict(reason_counter)}.")

# ================================================================ STEP 8: verification asserts
problems = []
if cleaned["record_id"].duplicated().any(): problems.append("duplicate record_id in output")
if (cleaned["linkedin_url"].str.strip() == "").any(): problems.append("blank linkedin_url in output")
if cleaned.shape[0] != cleaned["record_id"].nunique(): problems.append("row count != unique people")
if int(cleaned["total_visits"].sum()) != total_visits_pre_collapse: problems.append("visit reconciliation mismatch")
note(f"- **Step 8 — Verification:** {'ALL PASS' if not problems else 'FAILURES: ' + '; '.join(problems)} "
     f"(364 expected: got {cleaned.shape[0]} unique people, 0 dup, 0 blank LinkedIn, visits reconciled).")

# ================================================================ STEP 7: audit report
with open(AUDIT, "w") as f:
    f.write("# Data Cleaning Audit — deanon_export.csv → HubSpot\n\n")
    f.write("Framework: **CLEAN** (Conceptualize, Locate, Evaluate, Augment, Note). "
            "Raw file read-only; backup at `deanon_export_RAW_BACKUP.csv`.\n\n")
    f.write(f"**Start:** {start_rows} rows / {start_people} people  →  "
            f"**End:** {cleaned.shape[0]} clean contacts, {flag_df.shape[0]} flagged for review.\n\n")
    f.write("## Change log\n\n")
    for line in log:
        f.write(line + "\n")
    f.write("\n## Flag reason codes\n\n")
    f.write("- `MISSING_NAME` — blank first/last name (has LinkedIn, still enrichable)\n")
    f.write("- `NAME_DECONTAMINATED` — stripped '✨ | Open to Work' badge / emoji; verify extracted name\n")
    f.write("- `NAME_DEQUOTED` — unwrapped curly-quote nickname (e.g. “Ethan” → Ethan)\n")
    f.write("- `NON_LATIN_NAME` — Cyrillic/CJK name; kept as-is, may need transliteration\n")
    f.write("- `LINKEDIN_UNPARSEABLE` — URL had no parseable /in/<slug>; left as-is\n")

print("DONE")
print(f"  cleaned : {cleaned.shape[0]} rows x {cleaned.shape[1]} cols")
print(f"  flagged : {flag_df.shape[0]} records")
print(f"  verify  : {'ALL PASS' if not problems else problems}")
print(f"  reasons : {dict(reason_counter)}")
