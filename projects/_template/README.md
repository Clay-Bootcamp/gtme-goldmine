<!--
GTM GOLDMINE PROJECT README — TEMPLATE
=======================================
Copy this folder to projects/NN-your-project/ and fill in every [bracketed]
placeholder. The anti-copy framing and the 4-step Golden Prompts ritual
stay the same on every project. The variable parts:

  - Project number + title
  - One-line description of what gets built
  - Time estimate
  - Project-specific prereqs (inputs the builder needs to bring)
  - The 5 question topics inside the prompt (tailored to the project)
  - File list at the bottom (matches what's actually in the folder)
  - Live demo URL if you deployed

Delete this comment block before publishing.
-->

# Project #[NN] — [Project Title]

> **Stop. Read this before you touch anything else in this folder.**

## Don't copy this project.

If you clone this folder, swap [the obvious things — name, inputs, outputs] for yours, and call it done — you wasted [~time]. You didn't learn anything. You have a worse version of mine.

The point of GTM Goldmine is not the code. **The point is the method.** Build the thing that fits *your* circumstances, *your* needs, *your* vision — with Claude Code holding the keyboard and you holding the spec.

---

## Build your own version.

**Time:** ~[time estimate]
**Prereqs:**
- Claude Code installed → see [`Foundations/01-Setup`](../../Foundations/01-Setup/)
- [Project-specific input #1 — e.g., "A CSV of leads you want to enrich", "Your LinkedIn profile as a PDF", "An API key for X"]
- [Project-specific input #2 — optional / delete if not needed]

### Step 1 — Open Claude Code in a new, empty folder

```bash
mkdir my-[project-slug] && cd my-[project-slug]
claude
```

### Step 2 — Paste this prompt, verbatim

```
I want to build my own version of Project #[NN] — [Project Title] —
from the GTM Goldmine repo
(https://github.com/Clay-Bootcamp/gtme-goldmine).

I do NOT want to copy that project. I want my own version, tailored
to my circumstances and goals.

Before you write a single line of code, do this in order:

1. Ask me 5 high-signal questions covering:
   - [Question topic 1 — usually about audience / outcome / "what does done look like"]
   - [Question topic 2 — usually about input data or source material]
   - [Question topic 3 — usually about constraints / tools / providers]
   - [Question topic 4 — usually about edge cases or scope boundaries]
   - [Question topic 5 — usually about tech stack / deploy target / format]

2. Wait for my answers. Do not proceed until I've answered all 5.

3. Once I've answered, switch into plan mode (Shift+Tab twice) and
   draft a plan. Tell me exactly what files you'll create, what each
   will contain, and what the approach will be. Do NOT build anything
   yet. Wait for my approval.

4. Once I approve the plan, exit plan mode and build it.

Start by asking the 5 questions.
```

### Step 3 — Answer the questions like you mean it

No "you decide." No "whatever's easier." Every lazy answer here costs you 20 minutes of rework later. If you don't have a strong opinion on something, say *why* and ask Claude to recommend with a tradeoff — but never punt blindly.

### Step 4 — Read the plan. Push back if it's wrong.

Plan mode is not a rubber stamp. If something's off, say so. If it's close, ask for one specific change. The 60 seconds you spend here saves the next 30 minutes of bad code.

### Step 5 — Build

Exit plan mode, approve, watch it go. Iterate on the result in the same session.

---

## Why this works

This is the **Golden Prompts Framework**: *Think → Ask → Plan → Build*. It's how you get Claude Code to build what you actually want, not what it assumes you want. Full breakdown: [`Foundations/03-Golden-Prompts-Framework.md`](../../Foundations/03-Golden-Prompts-Framework.md).

Every project in this repo follows the same pattern. Copying any of them is missing the entire point.

---

## What's actually in this folder

For reference only — so you can see what I shipped on stream for *my* version. **Don't ship it as yours.**

- [`file1`] — [one-line description]
- [`file2`] — [one-line description]
- [`file3`] — [one-line description]

**Live demo (if applicable):** [URL or delete this line]

To poke around locally: [how to run — e.g., "`open index.html`" or "`python main.py`" or delete if N/A]
