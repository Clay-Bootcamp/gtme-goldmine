# Project #4 — Sales Email Personalizer (one winning template → many sites, grounded in real facts)

> **Full tutorial, uncut:** [YouTube livestream](https://youtu.be/WbAr9jErXkE)

> **Stop. Read this before you touch anything else in this folder.**

## Don't copy this project.

If you clone this folder, swap my candle shops for your prospects, and call it done — you wasted an hour. You didn't learn anything, and you have an email pitching *AI voice agents* for *voicemail-only support lines* to a list that probably has nothing to do with phone support. Your template wins on a different angle, your prospects expose different signals, and "personalized" means something different for your offer than it does for mine.

The point of GTM Goldmine is not the code. **The point is the method.** Take *your* highest-performing template, point Claude Code at *your* list of sites, and have it live-crawl each one, find the specific facts that make your angle true, and write a per-prospect email grounded in real evidence — with Claude Code holding the keyboard and you holding the spec.

---

## Verify or skip — never fabricate

The thing that makes this build good is **not** the personalization — it's the discipline of refusing to personalize when the facts aren't there. The template hinges on one specific, checkable claim ("your support line is voicemail-only / weekday-only, so after-hours questions go unanswered"). For every site, Claude crawls the live pages, and either:

- **the gap is verifiable** → generate the email, quoting the exact source (contact page, hours, phone), or
- **the gap can't be confirmed** (no phone, open 7 days, store offline, hours "vary") → **skip and flag**, with a reason.

That's why the run produced **4 emails and 6 skips** out of 10 stores — and why every row carries a `justification` citing what was found on the site. A personalizer that invents a gap to fill every row is worse than no personalizer: it gets you marked as a spammer and torches the template. Get the verify-or-skip rule right and the personalization takes care of itself.

---

## Build your own version.

**Time:** ~45–60 minutes.
**Prereqs:**
- Claude Code installed → see [Foundational Course — Install Claude Code](../../Claude-Code-For-GTM-Engineers-Foundational-Course/04-install-claude-code.md)
- **Your** highest-performing email template (subject + body) — the one you already know converts. Know which parts are the fixed skeleton and which one specific fact makes the angle land.
- A CSV (or just a list) of real sites/domains you want to scale that template across.
- A clear answer to "what fact has to be true on the site for this email to be honest?" — that's the gap Claude will hunt for and refuse to fake.

### Step 1 — Open Claude Code in a new, empty folder

```bash
mkdir my-email-personalizer && cd my-email-personalizer
# drop your sites CSV into this folder, then:
claude
```

### Step 2 — Paste this prompt, verbatim

```
I have a very well-performing email template, and I want to scale it across a
list of websites — automatically rewriting the messaging so each email reflects
that site's real, specific details. The domains are in the CSV in this folder.
I do NOT want to copy Project #4 from the GTM Goldmine repo
(https://github.com/Clay-Bootcamp/gtme-goldmine) — I want my own version, built
on MY template, MY list, and MY offer.

Before you build anything, do this in order:

1. Read the CSV and tell me what's in it. Then ask me to paste my winning
   template, and have me mark which parts are the fixed skeleton vs. the parts
   that should flex per site.

2. Ask me 5 high-signal questions covering:
   - The offer + sender: what I'm pitching, who I am, and the ONE specific
     fact that has to be true on a site for this email to be honest
   - Where per-site details come from: live-crawl each site, a data provider,
     or facts I'll hand you (push me toward live crawling for real specifics)
   - What "done" looks like: fill columns in the CSV, generate drafts, or push
     to a sending tool — and whether you also need to find the contact address
   - Edge cases: what to do when a site doesn't fit the angle (e.g. the fact
     can't be verified) — skip and flag, or force an email anyway
   - Guardrails: how much each email may vary, hard rules on length/claims,
     and an absolute "never fabricate a fact to fill a row" rule

3. Wait for my answers. Do not proceed until I've answered all 5.

4. Switch into plan mode (Shift+Tab twice) and lay out the plan: for each site,
   crawl the live pages, verify whether my angle's key fact is actually true and
   quotable, generate the email only if it is, and skip-and-flag with a reason
   if it isn't. Tell me the exact output format. Do NOT build yet — wait for
   approval.

5. Once I approve, build it. Crawl the sites (in parallel is fine), and produce
   a CSV with the site URL, contact email, the generated email, and a
   justification column that CITES the source for every claim and explains every
   skip. Never invent a fact. When in doubt, skip.

Start by reading the CSV.
```

### Step 3 — Answer the questions like you mean it

No "you decide." The whole build lives or dies on one answer: *what fact has to be true for this email to be honest?* For my template it was "the phone line is voicemail-only or weekday-only." For yours it might be a specific tech they run, a job they're hiring for, a missing feature. Get that wrong and Claude either skips everyone or fabricates to fill rows — both useless.

### Step 4 — Read the plan. Push back if it's wrong.

The plan is where you lock in the verify-or-skip contract. If the plan would write an email for every row no matter what, stop it — make "skip and flag when the fact isn't on the site" explicit before any crawling happens. That one rule is the difference between a list you'd actually send and a spam cannon.

### Step 5 — Build, then audit every row

Exit plan mode, approve, watch it crawl. Then **read the `justification` column on every single row** — both the generated and the skipped. Click through to the cited source on a couple of them. If a justification doesn't quote something real from the site, the email is fabricated and the whole template is at risk. Spot-checking here is not optional.

---

## Why this works

This is the **Golden Prompts Framework**: *Think → Ask → Plan → Build*. The twist for personalization work is that the contract you approve before any crawling is a **verify-or-skip rule**, not just a plan for code — Claude commits to citing a real source for every claim and skipping anything it can't confirm, *before* it touches a single site. That's how you get a list you'd stake your sender reputation on, instead of mail-merge dressed up as research. Full breakdown: [Foundational Course — The Golden Prompts Framework](../../Claude-Code-For-GTM-Engineers-Foundational-Course/07-golden-prompts-framework.md).

Every project in this repo follows the same pattern. Copying any of them is missing the entire point.

---

## What's actually in this folder

For reference only — so you can see what I shipped on stream for *my* version: scaling one AI-voice-agent template across 10 real California candle & soap shops. The shops are real public businesses; every fact in the output was live-crawled from their own sites and cited. **Don't ship my template or my list as yours — the angle is tuned to my exact offer.**

- `email_template.txt` — the winning template I scaled: an AI-voice-agent pitch built around one verifiable gap (voicemail-only / weekday-only support). **Read this first** — it shows what stays fixed and what flexes per store.
- `candle_shops.csv` — the raw input: 10 candle/soap shops (name, URL, location, wax type) with empty columns for the support details Claude crawled and filled.
- `personalized_emails.csv` — the output: `url`, `email_address`, `generated_email` (subject + body), and `justification` (cited sources for every email, and a reason for every skip). **4 emails generated, 6 skipped & flagged.**

### The cut, at a glance

| Store | Verdict | Why |
|---|---|---|
| P.F. Candle Co. | ✅ Email | Site explicitly says voicemail-only, Mon–Fri, weekend replies Mon/Tue — exact match |
| Honey Pacifica | ✅ Email | Phone + Mon–Fri 8:30–4, "prefer email" (corrected "voicemail-only" → "only staffed Mon–Fri") |
| Knorr Candle Shop | ✅ Email | Phone + Mon–Fri 9:30–5; framed around limited hours |
| Beeswax Candle Studio | ✅ Email | Phone + limited shop hours (Wed–Sun, closed Mon/Tue) |
| North Bay Candleworks | ⏭️ Skip | Phone exists, but no hours / no voicemail evidence |
| Often Wander | ⏭️ Skip | Email-only, no phone |
| Backyard Candles | ⏭️ Skip | Storefront offline ("store unavailable") |
| Toby's Candle & Soap | ⏭️ Skip | Open 7 days, not voicemail-only |
| Busy Bees Candle Co. | ⏭️ Skip | No phone published |
| Toadily Handmade | ⏭️ Skip | "Hours vary / by appointment" — can't assert the fixed-days gap |

Note: only P.F. Candle Co. was a verbatim match for the template's "voicemail-only" wording. Honey Pacifica, Knorr, and Beeswax matched a broader after-hours gap (limited weekday/shop hours), so the offer stayed identical and only the hook was adjusted to what each site actually states — never beyond it.
