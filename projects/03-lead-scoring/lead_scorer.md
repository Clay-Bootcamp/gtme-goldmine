# Lead Scorer — Clay.com Demo Requests

Formalized rubric for scoring inbound demo requests against Clay.com's ICP.
Scoring is **CSV-only** — every judgment is made from the data in the file; no external
research or enrichment. Every prospect in the file gets a score (a demo request = a prospect).

Reference ICP: `clay_icp.md`. Input: `clay_demo_requests.csv`.

---

## Output

Three columns are appended to each row:

| Column | Type | Meaning |
|--------|------|---------|
| `lead_score` | integer 1–10 | How well the prospect fits Clay's ICP (higher = better). Floor of 1. |
| `fit_label` | enum | `Very good fit` · `Good fit` · `Not a good fit` |
| `justification` | text | 1–2 line explanation of the score |

### Score → label mapping
- **8–10 → Very good fit**
- **5–7 → Good fit**
- **1–4 → Not a good fit**

---

## Scoring model (10 points)

Additive model. The two strongest buying signals — **outbound tooling** and **CRM** — are
weighted hardest and together account for half the total (5 of 10 points). This reflects the
domain finding that a prospect already running outbound tools and a CRM is the clearest
indicator of readiness for Clay.

| # | Signal | Points | Rule |
|---|--------|--------|------|
| 1 | **Outbound tooling** | 0–3 | 2+ outbound tools in stack = **3** · exactly 1 = **2** · none = **0** |
| 2 | **CRM in stack** | 0–2 | Salesforce or HubSpot = **2** · other CRM (e.g. Pipedrive) = **1** · none = **0** |
| 3 | **Company size** | 0–2 | 50–500 employees = **2** · near-miss (30–49 or 501–800) = **1** · else **0** |
| 4 | **Stage + ARR** | 0–2 | +1 if stage in Series A/B/C · +1 if ARR in $5M–$100M |
| 5 | **Industry + persona** | 0–1 | **1** if industry is B2B SaaS / Tech / Professional Services **and** buyer title is a GTM role (Sales, RevOps, Revenue, Growth, GTM, Marketing/Sales Ops) · else **0** |
| | **Raw total** | /10 | sum of the above |

### Tool reference lists
- **Outbound tools:** Outreach, Salesloft, Apollo, Instantly
- **Strong CRM:** Salesforce, HubSpot
- **Other CRM:** Pipedrive (and similar dedicated CRMs)
- **GTM-fit industries:** B2B SaaS, Enterprise Tech, Professional Services

*(Note: ZoomInfo, Clearbit, 6sense etc. are data/intent tools, not counted as outbound tooling
or CRM for signals 1–2.)*

---

## Disqualifier caps

Applied **after** the raw total. Every prospect is still scored (no removals); a disqualifier
caps the maximum score so the prospect lands in "Not a good fit" while the underlying signal
strength stays visible. If multiple caps apply, the **lowest** wins. The final score is never
below the floor of **1**.

| Disqualifier | Detection rule | Cap |
|--------------|----------------|-----|
| **Wrong industry** — B2C, local, non-tech | industry NOT in {B2B SaaS, Enterprise Tech, Professional Services} | **3** |
| **Too small / too early** — pre-seed, founder-led, no ops | employees < 10 OR funding stage in {Pre-seed, Bootstrapped} | **3** |
| **Too large & slow** — enterprise, long procurement | employees ≥ 5000 | **4** |

`final_score = max(1, min(raw_total, applicable_caps...))`

---

## Notes / deliberate choices

- **PLG companies with no sales motion are NOT extra-penalized.** A firmographically strong
  company that scores 0 on outbound and CRM (e.g. Linear) can still land at the bottom of
  "Good fit" on firmographics alone. This was reviewed and accepted in the dry run.
- **Competitors are scored normally.** Direct competitors (e.g. Apollo) are scored on fit like
  any other lead — a demo request makes them a prospect.
- **Caps preserve signal.** A disqualified-but-otherwise-strong company (capped at 3–4) reads
  differently in its raw signals than a genuinely weak one, even though both label as
  "Not a good fit".
