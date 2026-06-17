**[🏠 Course Home](./README.md)**  ·  Module 5 — Workflow Building Blocks  ·  Lesson 11 of 27

---

# Skills and Slash Commands

Skills are superpowers or reusable workflows you can load into Claude Code & invoke by typing `/` to save yourself time.

## What they are

Anything you type starting with `/` is a slash command. There are two kinds:

1. **Built-in slash commands** — ship with Claude Code. Hardcoded features like `/clear`, `/compact`, `/init`.
2. **Custom slash commands (aka Skills)** — ones you create. A folder of markdown that defines a reusable workflow. Type `/your-skill-name` and Claude loads those instructions and runs them.

> Note: Anthropic merged "commands" and "skills" into one system. A **Skill is a custom slash command**. Same thing, two names.
>

## Why it matters for GTM engineers

Stop copy-pasting the same prompt every day. Package "how you research a prospect" or "how you write a cold email" into `/prospect-research` or `/cold-email`. Invoke anywhere with one word.

Commit them to your repo → team-wide tooling. Everyone on your team gets the same workflows.

---

## Built-in slash commands — the ones worth knowing

| Command | What it does |
| --- | --- |
| `/init` | Generate starter CLAUDE.md |
| `/clear` | Wipe conversation, start fresh |
| `/compact` | Summarize and continue (not recommended — see Context Management) |
| `/context` | Show current token usage breakdown |
| `/statusline` | Configure bottom status bar |
| `/memory` | Show which CLAUDE.md files are loaded |
| `/plan` | Enter Plan Mode |
| `/model` | Switch models mid-session |
| `/cost` | See session cost |
| `/diff` | View all edits Claude has made |
| `/mcp` | Manage MCP servers |
| `/help` | Full command list |

Type `/` in Claude Code to see all available commands with autocomplete.

---

## Custom slash commands (Skills) — make your own

Every skill is a folder under `.claude/skills/` containing a `SKILL.md` file.

**Scope:**

- `~/.claude/skills/` — **personal**, available in every project
- `./.claude/skills/` — **project-scoped**, shared with your team via git

**How Claude uses them:**

- **Manual:** type `/skill-name` — Claude runs the skill
- **Auto:** if the task matches the skill's `description`, Claude invokes it on its own

### Minimal example: a GTM skill

File: `.claude/skills/prospect-research/SKILL.md`

```markdown
---
name: prospect-research
description: Research a prospect before cold outreach. Use when the user provides a LinkedIn URL or company name and wants quick context for an email.
---

Research the prospect ($ARGUMENTS) and output:

**Prospect:** [Name], [Role], [Company]
**Recent signals:** 2–3 things they've posted or their company has
announced in the last 30 days
**3 cold email hooks:** Each hook is one line. Specific, not generic.

Steps:
1. Check their LinkedIn profile — current role, recent posts
2. Search their company's latest news
3. Identify a pattern or angle worth referencing
4. Write 3 hooks that sound like a human wrote them — not an SDR tool
```

Invoke with: `/prospect-research https://linkedin.com/in/somebody`

`$ARGUMENTS` is a placeholder — whatever you type after the slash command gets inserted there.

---

## Skills vs CLAUDE.md — which when?

| If you want... | Use |
| --- | --- |
| Rules/context true in **every** session | **CLAUDE.md** (loads automatically) |
| A workflow you run **sometimes** | **Skill** (loads on demand) |
| Quick reference or detail doc | Regular `.md` file linked from CLAUDE.md via `@import` |

Context budget matters. CLAUDE.md eats tokens every session. Skills don't — they only load when triggered.

---

## GTM-flavored skill ideas

Brainstorm starters you can actually build:

- `/prospect-research [LinkedIn URL]`
- `/enrich-csv [file path]`
- `/linkedin-post [topic]`
- `/objection-handler [objection text]`
- `/discovery-call-prep [company name]`
- `/icp-score [account list]`
- `/email-teardown [paste email]`
- `/pricing-page-copy [product feature]`

**Rule of thumb:** If you've copy-pasted a prompt more than 3 times, make it a skill.

---

## How to write a good skill

- **Be directive, not conversational.** Imperative verbs: *"Research…", "Generate…", "Output…"* — not *"Maybe you could…"*
- **Specify output format.** Bullets, tables, sections — tell Claude exactly how to structure the response.
- **Front-load keywords in `description`.** That's how Claude decides to auto-invoke. Vague description = never triggers.
- **Keep it under ~500 words.** Longer skills get skimmed.
- **One skill, one workflow.** A "do-everything" skill is less effective than three focused ones.

---

## Common pitfalls

- **Skills too long** → Claude ignores parts of it
- **Vague `description`** → auto-invocation never fires, stays manual-only
- **Kitchen-sink skills** → split into focused workflows
- **Conversational tone** → use imperative commands instead
- **Forgetting the YAML frontmatter** → skill won't load at all
- **Not versioning** → commit `.claude/skills/` so your team has the same tooling

---

## Quick reference

|  |  |
| --- | --- |
| Personal skills location | `~/.claude/skills/[name]/SKILL.md` |
| Project skills location | `./.claude/skills/[name]/SKILL.md` |
| Required frontmatter | `name` (=slash command), `description` |
| Input variable | `$ARGUMENTS` (everything after the slash command) |
| See all available commands | Type `/` in Claude Code |

**Rule of thumb:** CLAUDE.md = always true. Skills = sometimes true. Built-in commands = Claude Code itself.

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Context Management & Context Rot](./10-context-management.md) | [All Lessons](./README.md) | [Recommended Skills](./12-recommended-skills.md) |
