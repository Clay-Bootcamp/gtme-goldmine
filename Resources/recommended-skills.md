# Recommended Skills

## What it is

A short list of skills worth installing today — plus the habit that matters more than any skill: **learning to write your own.**

Skills are custom slash commands (same thing — covered in the Skills & Slash Commands doc). You install them, then invoke with `/skill-name` or let Claude call them automatically.

## Why it matters for GTM engineers

You're not a developer. You don't have to invent everything from scratch. The community has already built playbooks for the boring parts. Your job: steal the good ones, skip the noise, and write 2–3 custom skills that encode YOUR way of doing GTM work.

---

## Three skills to start with

### 1. `frontend-design` (official Anthropic)

Breaks the generic AI default aesthetic — no more purple gradients, Inter font, grid of feature cards. Gives Claude Anthropic's internal design system before it writes a single line. 277K+ installs for a reason.

Install it before you ever build a landing page.

→ `github.com/anthropics/skills` (follow README)

### 2. `grill-me` (Matt Pocock)

Three sentences of pure leverage. When invoked, Claude interviews you relentlessly about your plan — one question at a time, walking down every branch of the decision tree — until every ambiguity is resolved. It even recommends answers so you can fly through with "yes" when it's obvious.

This is the antidote to *"I had a vague idea and Claude built the wrong thing."* Run it before `/plan`.

→ `github.com/mattpocock/skills` (9K+ stars)

---

## Follow GTM engineers who share skills

Don't browse random skill marketplaces. Follow people whose work you trust and download their stacks (LinkedIn and X).

- **Anthropic** (`github.com/anthropics/skills`) — official document skills, reference implementations
- **GTM engineers building in public** — ask them what they're running

---

## Learn to write your own skills

Third-party skills handle generic tasks. **Your 10x leverage is encoding YOUR frameworks** — your enrichment logic, your outreach voice, your qualification criteria, your voice.

Rule: **if you do something 3+ times, write the skill.**

See `skills-and-slash-commands.md` for how. It's a markdown file. You can do this.

---

## Common pitfalls

- **Installing 20 skills from random repos.** Official Claude Code docs explicitly flag untrusted skills as a security risk — a malicious skill can exfiltrate data or run unexpected code. Stick to people with reputations.
- **Never writing your own.** The real leverage isn't in what you install; it's in what you encode.
- **Treating skills like a library to browse.** They're not. Install 2–3, use them until they're muscle memory, then write yours.

---

## Quick reference

| Skill | What it does | Source |
| --- | --- | --- |
| `frontend-design` | Breaks generic AI design defaults | anthropics/skills |
| `grill-me` | Interviews you until every ambiguity is resolved | mattpocock/skills |
| **Your own skills** | Encode YOUR GTM frameworks | You write it |

---

## Rule of thumb

Install 2–3 trusted skills. Write your own for anything you do 3+ times. Everything else is noise.
