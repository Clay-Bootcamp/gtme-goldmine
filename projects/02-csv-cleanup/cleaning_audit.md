# Data Cleaning Audit — deanon_export.csv → HubSpot

Framework: **CLEAN** (Conceptualize, Locate, Evaluate, Augment, Note). Raw file read-only; backup at `deanon_export_RAW_BACKUP.csv`.

**Start:** 642 rows / 400 people  →  **End:** 331 clean contacts, 33 flagged & held back for manual review.

## Change log

- **Loaded raw (read-only):** 642 rows x 21 cols, 400 unique people (`record_id`). Raw file never modified; backup at `deanon_export_RAW_BACKUP.csv`.
- **Step 1 — Discard un-enrichable (no LinkedIn):** removed 36 rows with blank `linkedin_url`. Unique people 400 -> 364 (36 people dropped, 9.0%). No LinkedIn = cannot enrich = excluded by rule. Dropped record_ids: RB2B-000023, RB2B-000024, RB2B-000036, RB2B-000041, RB2B-000048, RB2B-000052, RB2B-000064, RB2B-000084, RB2B-000099, RB2B-000108, RB2B-000117, RB2B-000136, RB2B-000149, RB2B-000151, RB2B-000177, RB2B-000182, RB2B-000184, RB2B-000186, RB2B-000187, RB2B-000190, RB2B-000194, RB2B-000197, RB2B-000216, RB2B-000233, RB2B-000236, RB2B-000275, RB2B-000283, RB2B-000296, RB2B-000310, RB2B-000317, RB2B-000320, RB2B-000322, RB2B-000343, RB2B-000354, RB2B-000372, RB2B-000389.
- **Step 2 — Normalize LinkedIn URLs:** canonicalized to `https://www.linkedin.com/in/<slug>` (forced https + www, stripped query params `?utm_source`/`?trk`, trailing slashes, lowercased slug). Original host/protocol-prefix distribution: {'www.linkedin.com': 404, 'linkedin.com': 202}. 0 URLs could not be parsed into /in/<slug> and were left as-is + flagged.
- **Step 3 — Clean names:** trimmed whitespace (incl. zero-width chars), removed '✨ | Open to Work' badges and emoji decorations (🚀/☆/etc.), unwrapped curly-quote nicknames, collapsed internal spaces, then Title-Cased ASCII names (fixes ALL-CAPS and lowercase). Non-Latin names (Cyrillic/CJK) kept and flagged for review; blank names flagged.
- **Step 4 — Collapse to one row per person:** grouped 606 visit rows by `record_id`; canonical identity taken from each person's EARLIEST visit (`visit_timestamp`). Result: 364 unique people. Identity-field inconsistencies across a person's rows: 0 ([]).
- **Step 5 — Augment:** built `notes` (one line per visit, newest first, `YYYY-MM-DD — page`), `total_visits`, `first_visit_date`, `last_visit_date`. Dropped redundant `visit_count` (was 1 on every row). Reconciliation: sum(total_visits)=606 vs visit rows after Step 1=606 -> MATCH.
- **Future-dated visits (left as-is per instruction):** 68 visit rows have `visit_timestamp` after today (2026-06-03), spanning 41 people. Not altered; flagged here for visibility only.
- **Step 6 — Outputs written:** `deanon_cleaned.csv` (364 rows x 22 cols); `flag.csv` (33 records for human review). Raw untouched.
- **Flag breakdown (by person):** {'NAME_DECONTAMINATED': 19, 'NON_LATIN_NAME': 11, 'NAME_DEQUOTED': 3}.
- **Step 8 — Verification:** ALL PASS (364 expected: got 364 unique people, 0 dup, 0 blank LinkedIn, visits reconciled).
- **Step 9 — Remove flagged from clean file (caution, user-requested):** all 33 records present in `flag.csv` (NAME_DECONTAMINATED, NON_LATIN_NAME, NAME_DEQUOTED) removed from `deanon_cleaned.csv`. Final clean contacts 364 -> **331**. Flagged people remain in `flag.csv` for later manual import. Re-checked: clean file has 0 flagged records, 0 duplicates, 0 blank LinkedIn -> ALL PASS.

## Flag reason codes

- `MISSING_NAME` — blank first/last name (has LinkedIn, still enrichable)
- `NAME_DECONTAMINATED` — stripped '✨ | Open to Work' badge / emoji; verify extracted name
- `NAME_DEQUOTED` — unwrapped curly-quote nickname (e.g. “Ethan” → Ethan)
- `NON_LATIN_NAME` — Cyrillic/CJK name; kept as-is, may need transliteration
- `LINKEDIN_UNPARSEABLE` — URL had no parseable /in/<slug>; left as-is
