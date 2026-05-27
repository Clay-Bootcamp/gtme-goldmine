# Project #1 — Landing Page / Portfolio Website

> **Full tutorial, uncut:** [YouTube livestream](https://www.youtube.com/watch?v=u2F_oum4rVw&t=1713s)

> **Stop. Read this before you touch anything else in this folder.**

## Don't copy this project.

If you clone this folder, swap my name for yours, change the wallpaper, and call it done — you wasted an hour. You didn't learn anything. You don't have a site that's about *you*. You have a worse version of mine.

The point of GTM Goldmine is not the code. **The point is the method.** Build the thing that fits *your* audience, *your* circumstances, *your* vision — with Claude Code holding the keyboard and you holding the spec.

That's it. That's the whole repo.

---

## Build your own version.

**Time:** ~60 minutes.
**Prereqs:**
- Claude Code installed → see [`Foundations/01-Setup`](../../Foundations/01-Setup/)
- Your LinkedIn profile as a PDF (open your profile → ⋯ More → Save to PDF)
- A reference site you actually like (optional but huge)

### Step 1 — Open Claude Code in a new, empty folder

```bash
mkdir my-landing-page && cd my-landing-page
claude
```

### Step 2 — Paste this prompt, verbatim

```
I want to build my own personal landing page / portfolio website, in
the spirit of Project #1 from the GTM Goldmine repo
(https://github.com/Clay-Bootcamp/gtme-goldmine).

I do NOT want to copy that project. I want my own version, tailored to
my audience, my vision, and my circumstances.

Before you write a single line of code, do this in order:

1. Ask me 5 high-signal questions covering:
   - Who my primary audience is, and the single most important goal of
     the site (one CTA wins — what is it?)
   - What source material I have to draw from (LinkedIn PDF, resume,
     existing bio, none)
   - The visual style I want, with reference sites or screenshots if I
     have them
   - Sections beyond bio + work history I want included
     (writing, projects, testimonials, contact, etc.)
   - Tech stack preference and where it'll live (local first, or deploy
     somewhere from day one)

2. Wait for my answers. Do not proceed until I've answered all 5.

3. Once I've answered, switch into plan mode (Shift+Tab twice) and
   draft a plan. Tell me exactly what files you'll create, what each
   will contain, and what the visual approach will be. Do NOT build
   anything yet. Wait for my approval.

4. Once I approve the plan, exit plan mode and build it.

Start by asking the 5 questions.
```

### Step 3 — Answer the questions like you mean it

No "you decide." No "whatever's easier." Every lazy answer costs you 20 minutes of rework later. If you don't have a strong opinion on something, say *why* and ask Claude to recommend with a tradeoff — but never punt blindly.

### Step 4 — Read the plan. Push back if it's wrong.

Plan mode is not a rubber stamp. If something's off, say so. If it's close, ask for one specific change. The 60 seconds you spend here saves the next 30 minutes of bad code.

### Step 5 — Build

Exit plan mode, approve, watch it go. Iterate on copy, colors, layout in the same session. Deploy when you love it (drag-and-drop to [Netlify Drop](https://app.netlify.com/drop) — no terminal needed).

---

## Why this works

The four-step ritual above is the **Golden Prompts Framework**: *Think → Ask → Plan → Build*. It's how you get Claude Code to build what you actually want, not what it assumes you want. Full breakdown: [`Foundations/03-Golden-Prompts-Framework.md`](../../Foundations/03-Golden-Prompts-Framework.md).

Every project in this repo follows the same pattern. Copying any of them is missing the entire point.

---

## What's actually in this folder

For reference only — so you can see what I shipped on stream for *my* version. **Don't ship it as yours.**

- `index.html` — markup + all note content (about me, quick links, writing, currently building, principles, kind words)
- `styles.css` — dark Apple Notes theme + Lake Tahoe wallpaper backdrop
- `app.js` — tiny click handler that swaps the visible note
- `wallpaper.png` — the desktop image I used

**Live site:** [genuine-rugelach-843966.netlify.app](https://genuine-rugelach-843966.netlify.app/)

To poke around locally: `open index.html` (Mac) or double-click the file. No build step, no install.
