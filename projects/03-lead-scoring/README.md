# Project #3 — Lead Scoring from a CSV (inbound demo requests → prioritized list)

> **Full tutorial, uncut:** [YouTube livestream](https://www.youtube.com/watch?v=HdG5IxNUUc4)

> **Stop. Read this before you touch anything else in this folder.**

## Don't copy this project.

If you clone this folder, run my `score_leads.py` against my CSV, and call it done — you wasted an hour. You didn't learn anything, and you have a scorer hard-wired to *Clay's* ICP and *my* CSV schema, not yours. Your leads have different columns, your ICP weights different signals, and "a good lead" means something different for your business than it does for mine.

The point of GTM Goldmine is not the code. **The point is the method.** Point Claude Code at *your* lead list and *your* ICP, make it design a scoring rubric with you, plan the model, and build a scorer that ranks leads the way *your* GTM team actually prioritizes them — with Claude Code holding the keyboard and you holding the spec.

---

## Rubric before code

The thing that makes this build good is **not** the Python — it's the `lead_scorer.md` rubric. Before a single line of scoring logic gets written, you and Claude agree on a written, point-by-point model: which signals matter, how many points each is worth, and which disqualifiers cap a score. The script is just a deterministic, CSV-only executor of that rubric — no LLM guesswork, no external enrichment, same input always yields the same score. Get the rubric right and the code writes itself.

---

## Build your own version.

**Time:** ~45–60 minutes.
**Prereqs:**
- Claude Code installed → see [`Foundations/01-Setup`](../../Foundations/01-Setup/)
- A real CSV of leads you want to prioritize (inbound demo requests, a webinar list, an event scan, a cold list) — with firmographic and/or tech-stack columns to score against
- A clear, written-down ICP — who's a great fit, who's a hard no, and *why*. If you don't have one, writing it is half this project.
- Python 3 (Claude will set this up if you don't have it)

### Step 1 — Open Claude Code in a new, empty folder

```bash
mkdir my-lead-scoring && cd my-lead-scoring
# drop your leads CSV (and an ICP doc, if you have one) into this folder, then:
claude
```

### Step 2 — Paste this prompt, verbatim

```
In this project there is a CSV of leads, and my job as a GTM engineer is to
score and prioritize them against my ICP. I do NOT want to copy Project #3
from the GTM Goldmine repo (https://github.com/Clay-Bootcamp/gtme-goldmine)
— I want my own scorer, tailored to MY ICP and MY CSV.

We are NOT writing any scoring code yet. I want to nail the rubric on paper
before we touch the data.

Do this in order:

1. Read the CSV first — list every column, show me a few sample rows, and
   tell me which columns are usable scoring signals vs. just identifiers.
   If I included an ICP doc, read it too and reflect it back to me.

2. Then ask me 5 high-signal questions covering:
   - My ICP: what makes a lead a GREAT fit vs. a weak one, in concrete,
     checkable terms (size, stage, industry, tech stack, persona/title)
   - Which signals are the STRONGEST buying indicators, and how I want
     them weighted relative to each other (what should dominate the score)
   - Disqualifiers: who is a hard no regardless of other signals, and
     whether they should be dropped or just capped/flagged as "not a fit"
   - Edge cases: competitors, missing/blank fields, near-misses on a
     threshold, PLG companies with no sales motion — how each is handled
   - Output: the score scale (e.g. 1–10), fit labels and their cutoffs,
     what justification I want per row, and how the file should be sorted

3. Wait for my answers. Do not proceed until I've answered all 5.

4. Then write the rubric as a markdown doc FIRST (signals, points, weights,
   disqualifier caps, score→label mapping) and show it to me. Do NOT write
   any Python yet. We iterate on the rubric until I approve it.

5. Once I approve the rubric, switch into plan mode (Shift+Tab twice) and
   plan the scorer: a deterministic, CSV-only script that implements the
   rubric exactly, appends score / label / justification columns, never
   mutates my raw file, and prints a ranked summary. Wait for approval.

6. Once I approve, build it, run it on my CSV, and walk me through the
   top and bottom of the ranked list so I can sanity-check the scores.

Start by reading the CSV.
```

### Step 3 — Answer the questions like you mean it

No "you decide." A lead score is a *business* decision encoded as math. Whether a Series A company outranks a Series C one, whether a missing CRM is a minor ding or a disqualifier, whether you score competitors at all — only you know. Every lazy answer here ships a ranked list your sales team won't trust, which is worse than no list.

### Step 4 — Read the rubric. Push back if it's wrong.

The rubric is the whole game. If the weights don't match how you actually prioritize — if "running outbound tooling" should outweigh "headcount" and the draft has it backwards — say so *before* it becomes code. Run it against 3–4 leads you already have a gut feel for; if the scores disagree with your gut, the rubric is wrong, not your gut.

### Step 5 — Build

Exit plan mode, approve, watch it run. Then **read the ranked output** top-to-bottom — the justification column tells you *why* each lead landed where it did. Spot-check a few high and low scores by hand before you hand the list to anyone.

---

## Why this works

This is the **Golden Prompts Framework**: *Think → Ask → Plan → Build*. The twist for scoring work is that the artifact you approve before any code is a **written rubric**, not a plan for code — Claude drafts the point model, you argue with it, and only once it matches your judgment does it become a deterministic script. That's how you get a scorer you'd actually stake a quota on, instead of a black box that spits out numbers. Full breakdown: [`Foundations/03-Golden-Prompts-Framework.md`](../../Foundations/03-Golden-Prompts-Framework.md).

Every project in this repo follows the same pattern. Copying any of them is missing the entire point.

---

## What's actually in this folder

For reference only — so you can see what I shipped on stream for *my* version: scoring a batch of inbound demo requests against [Clay.com](https://www.clay.com/)'s ICP. The demo-request rows are **synthetic** — the companies are real but the contacts and demo requests were generated for the stream, so the data is safe to look at. **Don't ship my rubric or script as yours; they're tuned to Clay's exact ICP.**

- `lead_scorer.md` — the scoring rubric I built live: a 10-point additive model (outbound tooling + CRM weighted hardest), disqualifier caps, and the score→label mapping. **Read this first** — it's the heart of the project.
- `clay_icp.md` — Clay's Ideal Customer Profile (primary + secondary ICP, anti-ICP, personas, pain points). The source material the rubric was derived from.
- `score_leads.py` — the scorer that implements `lead_scorer.md` exactly: deterministic, CSV-only (no LLM, no enrichment), appends `lead_score` / `fit_label` / `justification`, and prints a ranked summary.
- `clay_demo_requests.csv` — the raw input: 32 synthetic inbound demo requests with firmographics and tech stacks.
- `clay_demo_requests_scored.csv` — the output: the same 32 rows with score, fit label, and a one-line justification appended.

To run it yourself: `python3 score_leads.py` from inside this folder (defaults to the newest non-scored CSV). It regenerates `clay_demo_requests_scored.csv` from the raw file.
