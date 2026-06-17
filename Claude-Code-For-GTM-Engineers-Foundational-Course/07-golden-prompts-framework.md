**[🏠 Course Home](./README.md)**  ·  Module 3 — The Golden Prompts Framework  ·  Lesson 7 of 27

---

# The Golden Prompts Framework

The 4-step framework for getting Claude Code to build what you actually want — not what it assumes you want.

## What it is

Four prompts (and one mode) that run *before* you say "build it." This is the difference between power users who ship and hobbyists who quit after Claude goes off the rails on a 45-minute build.

## Why it matters for GTM engineers

You're not a developer. You can't tell at a glance if Claude is about to build the wrong thing. These prompts front-load the thinking so execution is fast, accurate, and doesn't burn your API budget on rework.

---

## The 4 Steps

### 1. THINK FIRST

Before you open Claude Code, open a note. Write what you actually want in plain English:

- What's the outcome?
- What does "done" look like?
- What data or tools are involved?

**If you can't write it clearly, Claude can't build it clearly.** Don't skip this.

### 2. Socratic Questioning

Paste your brief into Claude Code. Then add this prompt:

> *"Before you build anything, ask me 5 questions to really make sure you understand what I need."*
>

What it does:

- Eliminates assumptions you didn't know you were making
- Forces you to think through edge cases
- Lowers the risk of things going wrong

Answer the questions properly — no "whatever you think is fine." Then ask Claude to re-summarize what it's building based on your answers.

### 3. Plan Mode

Plan Mode is a read-only mode in Claude Code. Claude can analyze your project and propose a plan, but it can't edit files, run commands, or touch anything until you approve.

**How to activate:**

- Press `Shift+Tab` twice — you'll see `⏸ plan mode on` at the bottom of your terminal
- Or type `/plan`
- Windows users: if `Shift+Tab` skips Plan Mode, use `/plan` or `Alt+M`

Then prompt:

> *"Now show me your plan before you start. DO NOT BUILD until I approve."*
>

Review the plan. If it's wrong, iterate in chat. If it's close but needs tweaks, press `Ctrl+G` to open the plan in your text editor and edit directly (faster than describing changes in chat).

### 4. Build

Exit Plan Mode (`Shift+Tab` once more) and approve. Now Claude executes against a plan you've already signed off on — so execution is faster, cheaper, and actually matches what you asked for.

---

## Example: Building a lead enrichment agent

1. **Think First:** "I want an agent that takes a CSV of 100 companies, finds the CMO's LinkedIn, pulls their last 3 posts, and adds a 'topic angle' column for cold outreach."
2. **Socratic:** Claude asks — Which enrichment provider? What if the CMO isn't found? What format for the LinkedIn field? How long should the topic angle be?
3. **Plan Mode:** Claude outlines the file structure, the API calls it'll make, the error handling, and the output format. You review, tweak one step, approve.
4. **Build:** Runs cleanly in ~10 min instead of 40 min of back-and-forth.

---

## Common pitfalls

- **Skipping Think First** and prompting from instinct → Claude builds something, but not what you wanted
- **Lazy Socratic answers** ("you decide") → you're still letting Claude assume
- **Approving Plan Mode without reading the plan** → defeats the entire point
- **Forgetting to exit Plan Mode** before saying "go" → Claude won't actually build anything

---

## Quick reference

| Step | Action / Prompt |
| --- | --- |
| 1. Think First | Write brief in your own words, offline |
| 2. Socratic | `"Before you build anything, ask me 5 questions to really make sure you understand what I need."` |
| 3. Plan Mode | `Shift+Tab` twice (or `/plan`) → `"Now show me your plan before you start. DO NOT BUILD until I approve."` |
| 4. Build | Exit Plan Mode (`Shift+Tab`) → approve |

**The rule:** Think → Ask → Plan → Build. In that order. Every time.

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Your First Claude Code Project](./06-your-first-project.md) | [All Lessons](./README.md) | [CLAUDE.md Files](./08-claude-md-files.md) |
