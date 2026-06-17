**[🏠 Course Home](./README.md)**  ·  Module 5 — Workflow Building Blocks  ·  Lesson 13 of 27

---

# Agents and Subagents

## What it is (plain English)

When you use Claude Code, you're talking to the **main agent** — the one that reads your prompts, picks tools, does the work. Think of it as your project manager.

**Subagents are employees the main agent can delegate to.** You say: *"spin up a subagent to research these 20 companies."* The subagent goes off in its own separate context window, does the noisy work (reading websites, fetching news, parsing LinkedIn), and hands back a **clean summary** — not the 50 pages of raw content it read to get there.

The main agent stays the manager. Subagents do the grunt work and report back.

## Why it matters for GTM engineers

Context is your most valuable resource. The **150K rule** (from [Context Management](./10-context-management.md)) says models degrade after ~150K tokens, regardless of window size. A deep prospect research session — 20 company sites, 20 news pulls, 20 LinkedIn profiles — blows through that fast. By the time you're composing outreach, your main agent is drowning in raw HTML.

Subagents are the fix. The subagent absorbs the noise in its own context, summarizes, and **only the summary returns**. Your main agent stays sharp.

This isn't about making Claude smarter. It's about preserving the quality of the context you already have.

## How it works

1. A task looks heavy — lots of reading, lots of fetches, lots of noise
2. Main agent spins up a subagent with a specific job + prompt
3. Subagent runs in its own fresh context — own tools, own system prompt, own transcript
4. When done, subagent returns **only its final summary** to the main agent
5. All the raw tool calls and intermediate noise stay inside the subagent and get discarded

One hard rule: **subagents can't spawn other subagents.** No infinite nesting. Two-layer workflows get orchestrated from the main thread.

## Three ways to invoke a subagent

Natural language first, always:

1. **Describe the job.** *"Use a subagent to research Acme Corp's recent news. Return a one-paragraph summary."* Main agent picks a built-in subagent and delegates.
2. **@-mention a custom one.** *"@prospect-researcher dig into these 10 accounts."* Forces a specific subagent.
3. **Let auto-delegation fire.** If your custom subagents have good descriptions, Claude routes matching tasks automatically.

**Pro tip:** While a subagent is running, press **Ctrl+B** to send it to the background. Keep working in the main session; results surface when it's done. Run `/tasks` to see what's running.

## Built-in subagents

Ship with Claude Code. You don't create them — they just work:

| Subagent | What it does |
| --- | --- |
| **Explore** | Read-only codebase/folder exploration |
| **Plan** | Research + propose a plan (no changes). Fires during plan mode. |
| **general-purpose** | Multi-step exploration + action for complex tasks |

## Creating your own subagent

Run **`/agents`** inside a session. Fill in:

- **Name** — job-shaped: `prospect-researcher`, `csv-enricher`, `email-personalizer`
- **Description** — when to delegate (this is the routing signal — be specific)
- **System prompt** — how it behaves
- **Tools** — which built-in tools + MCPs it's allowed to touch
- **Model** — which Claude model it runs (see [Model Selection](./14-model-selection.md) — this matters for cost)

Saved as markdown files with YAML frontmatter. Project-level: `.claude/agents/`. User-level (all projects): `~/.claude/agents/`. You don't have to touch the files — `/agents` handles it.

## GTM example — prospect research at scale

**Setup:** 20 target accounts. For each: (a) two-line snapshot, (b) recent news, (c) CEO's latest public quote, (d) suggested outreach angle.

**Without subagents:** Main agent reads 20 websites + fetches 20 news feeds + pulls 20 profiles, all into the main context. By account #15, the context is full of HTML, and the quality of the outreach angles craters.

**With subagents:** You say *"Use a subagent per account. Return a structured summary: snapshot, news, CEO quote, angle. Nothing else."*

- 20 subagents fan out (batch to 5 at a time if you want to stay cost-sane)
- Each reads, fetches, synthesizes in its own context
- Each returns ~150 words of structured output
- Main agent stitches 20 clean summaries into the final plan

Context stays clean. You keep iterating in the same session without needing `/clear`.

## Common pitfalls

- **Vague descriptions.** `"helps with research"` won't get delegated to. Say what it does: `"Researches a single company by name. Returns snapshot, news, and a 2-line outreach angle. Use for prospect research batches."`
- **Too many specialist agents.** Five well-scoped beats twenty overlapping. Flooding Claude with options makes auto-routing unreliable.
- **Using subagents for tiny tasks.** Delegation has overhead. Quick fix or one-file edit → stay in the main session.
- **Parallel agents editing the same file.** Recipe for conflicts. Tightly-coupled changes stay in one context.
- **Expecting subagents to coordinate.** They can't talk to each other. Each reports to the main thread. Orchestration is the main agent's job.

## Subagents vs. skills

| Use a... | When |
| --- | --- |
| **Skill** | You want to inject *knowledge or procedure* into Claude's context ("how we write outreach emails") |
| **Subagent** | You want to *isolate a side task* in its own context window with its own tools |

Skills run inside the main context. Subagents spin off into their own.

## Quick reference

| You want to... | Do this |
| --- | --- |
| Delegate a heavy task | *"Use a subagent to [job]. Return [structured output]."* |
| Force a specific subagent | `@agent-name` in your prompt |
| Create or manage custom subagents | Run `/agents` |
| Save a subagent for a project | `.claude/agents/` |
| Save across all projects | `~/.claude/agents/` |
| Background a running subagent | `Ctrl+B` |
| See what's running in background | `/tasks` |

## Rule of thumb

**The main agent is the manager. Subagents are the employees. Delegate anything noisy, context-heavy, or parallelizable — prospect research, CSV enrichment, multi-source lookups. Keep the main agent on decisions, synthesis, and final output. If your context is bloating before you've done the actual work, you needed a subagent three steps ago.**

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Recommended Skills](./12-recommended-skills.md) | [All Lessons](./README.md) | [Model Selection](./14-model-selection.md) |
