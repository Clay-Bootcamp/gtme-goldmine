**[🏠 Course Home](./README.md)**  ·  Module 4 — Project Setup & Memory  ·  Lesson 8 of 27

---

# CLAUDE.md files and how to use them

> ## 📺 Video Lesson
> **▶️ [Watch the Supercut walkthrough](https://supercut.ai/share/claude-code-gtm/BIYYbpJ1zCKzpxIZZFC8ER)**
>
> This lesson has a video. Watch it first, then use the notes below as your reference.

# CLAUDE.md

Your project's signboard. The first thing Claude reads in every session.

## What it is

A markdown file named exactly `CLAUDE.md` (case-sensitive) placed in your project root. Claude Code auto-loads it at the start of **every** session and it **survives `/clear`**.

Think of it as: *the onboarding brief a new teammate reads in their first 5 minutes.*

## Why it matters for GTM engineers

Without CLAUDE.md, every new session is a fresh amnesiac Claude. You repeat yourself. You re-explain the project. You re-state the rules.

With CLAUDE.md, every session starts oriented — project goal, stack, conventions, and rules are already loaded.

---

## The signboard principle

**CLAUDE.md is NOT a dump file.** It is a signboard:

- **High-level orientation only** — what the project is, why it exists, how it's structured
- **Rules Claude must follow** — the guardrails
- **Pointers to other files** — for anything detailed

Details (progress logs, architecture notes, long decision rationale) go in **separate files** like `progress.md`, `architecture.md`, `decisions.md`. CLAUDE.md points to them using `@imports`.

Why: every line in CLAUDE.md costs context tokens every session. Bloated CLAUDE.md = wasted context + Claude skims past the important stuff.

---

## What belongs in CLAUDE.md

- **One-line project description** (what is this?)
- **Goal / outcome** (why does it exist?)
- **Stack** (tools, languages, key libraries)
- **Conventions** (file naming, coding style, folder structure)
- **Hard rules** (things Claude must never do — "never commit .env", "never modify /output/")
- **Pointers** to detail files (progress.md, etc.)

## What does NOT belong

- Session progress notes → put in `progress.md`
- Long business context → put in a linked doc
- Full code examples → link to the code
- Every preference you've ever had — if it's not essential, cut it

---

## @imports — the pointer system

CLAUDE.md supports `@filename.md` syntax. Claude loads those files automatically when relevant, without bloating the signboard.

```
## Current progress
@progress.md

## Architecture decisions
@architecture.md
```

This keeps CLAUDE.md light but gives Claude access to detail on demand.

---

## Example CLAUDE.md (lead enrichment project)

```markdown
# Lead Enrichment Agent

A Claude Code agent that takes a CSV of company domains and returns:
- CMO LinkedIn URL
- Their last 3 posts
- A suggested outreach angle

## Stack
- Python 3.11
- Exa AI for web search
- Proxycurl for LinkedIn
- Output: enriched CSV in /output/

## Conventions
- API keys in .env only — never in code
- Use uv for package management
- One function, one responsibility
- All logs go to /logs/enrichment.log

## Hard rules
- NEVER commit .env or credentials
- NEVER modify /output/ directly — that's live data
- ALWAYS run test_enrichment.py before shipping

## Current state
@progress.md

## Architecture
@architecture.md
```

That's it. ~30 lines. Everything deeper lives in the linked files.

---

## How to create one

**Option 1 (fast):** Run `/init` in your project directory. Claude scans the codebase and generates a starter CLAUDE.md. Then refine.

**Option 2 (deliberate):** Ask Claude to create it, specify what you want put inside it. Recommended because it forces you to think.

---

## When to update CLAUDE.md

Three checkpoints worth training yourself on. CLAUDE.md becomes a living feedback loop — wins get encoded, mistakes get fenced off.

### 1. When you make a decision or learn a convention

*"We're using async functions everywhere."* *"All Exa queries get cached for 24h."*

> *"Add this to CLAUDE.md."*
>

### 2. When Claude does something really well ✅

This is the one most people miss. When Claude nails a pattern — writes exactly the right code, handles an edge case elegantly, makes a call you'd have made — capture it so it happens every time.

> *"That worked perfectly. Write what went well to CLAUDE.md so we do it this way every time going forward."*
>

Wins become durable instructions instead of one-off lucky outputs.

### 3. When Claude messes up horribly ❌

The opposite move. When Claude breaks a convention, touches a file it shouldn't have, or makes a mess — capture the lesson as a hard rule.

> *"That was wrong. Add a 'never do this again' rule to CLAUDE.md explaining exactly what you did and why not to."*
>

Your "Hard rules" section grows organically from real mistakes, not from you trying to anticipate everything upfront.

---

## The workflow loop

1. **Start project** → create CLAUDE.md (via `/init` or by hand).
2. **Work.** Claude has context from the signboard every session.
3. **Capture as you go** — update CLAUDE.md at the three checkpoints above (decisions, wins, mistakes).
4. **Approaching 150K context?** Update `progress.md` with current state (NOT CLAUDE.md — progress goes in `progress.md`).
5. **`/clear`.** New session loads CLAUDE.md → follows `@progress.md` → Claude knows exactly where you left off.

---

## Common pitfalls

- **Treating it as a dump file** — bloats context, Claude skims past the signal
- **If everything is IMPORTANT, nothing is** — use emphasis sparingly
- **Never updating it** — stale CLAUDE.md gives wrong assumptions forever
- **Mixing CLAUDE.md and progress.md** — one is orientation (stable), one is state (changes constantly)
- **Writing in long paragraphs** — Claude processes structured bullets better

---

## Quick reference

| Command / Syntax | Purpose |
| --- | --- |
| `/init` | Auto-generate starter CLAUDE.md |
| `/memory` | Show which CLAUDE.md files are loaded |
| `@filename.md` | Import another markdown into context |

**Rule of thumb:** If it needs to be true *every session*, it goes in CLAUDE.md (or something `@imported` from it). If it changes often, it goes in a linked file.

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [The Golden Prompts Framework](./07-golden-prompts-framework.md) | [All Lessons](./README.md) | [Project Hierarchies & CLAUDE.md](./09-project-hierarchies.md) |
