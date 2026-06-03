# Model Selection

> ⚠️ **This doc will age fast.** Anthropic ships new Claude models every few months, and the aliases (`opus`, `sonnet`, `haiku`) auto-point to the latest version. Specific model numbers below are accurate as of April 2026. The *logic* — when to use each tier — is what lasts.

## What it is (plain English)

Claude comes in three tiers that scale with capability and cost:

- **Opus** — the smartest, slowest, most expensive
- **Sonnet** — the daily driver. Smart enough for most real work, fast enough to not hurt
- **Haiku** — fast and cheap. Great for simple, mechanical, high-volume work

You switch with `/model`. Subagents can also run on a different model than the main agent — that's where most of the cost savings live.

## Why it matters for GTM engineers

Two reasons:

1. **Cost.** Opus is roughly 5x the price of Sonnet. Run Opus by default and you'll burn your usage limit on a single prospect research batch. Run Haiku by default and your planning and code will get sloppy.
2. **Security.** Smaller models are measurably more vulnerable to prompt injection. When your agent is reading scraped websites, inbound emails, or leads from a sketchy list, a weaker model is more likely to follow a malicious instruction hidden in that content. GTMEs feed Claude third-party data constantly. This matters.

## The current lineup (June 2026)

| Tier | Current | Where it shines | Where it fails |
| --- | --- | --- | --- |
| **Opus** | Opus 4.8 | Planning, architecture, hard debugging, code writing for anything non-trivial | Simple or high-volume tasks — you're paying for reasoning you don't need |
| **Sonnet** | Sonnet 4.6 | Default for almost everything. Coding, writing, analysis, most agentic loops | Hard architecture decisions that really need to be right |
| **Haiku** | Haiku 4.5 | Mechanical high-volume work: renaming, formatting, extracting fields, simple summaries, cheap subagent execution | Real code writing, security-sensitive tasks, anything touching untrusted input |

## The rule to live by

- **Planning and code writing → Opus.** Decisions here cascade everywhere downstream. Pay for quality.
- **Daily work → Sonnet.** Default.
- **Mindless execution → Haiku.** Only when the task is simple AND the input is trusted.

Shortcut for mixed workflows: **`/model opusplan`** — Opus in plan mode (thinking, architecture), Sonnet in execution (typing the code). Top-tier reasoning on the decisions, economical execution on the grunt work.

## Switching models

Natural language first:

- *"Switch to Opus — I want to think through this architecture."* Claude handles it.
- `/model` opens a picker. `/model sonnet` / `/model opus` / `/model haiku` jumps directly.
- `/status` shows what you're currently on.
- On startup: `claude --model opus`
- Per-subagent: set it when creating via `/agents` (see `agents-and-subagents.md`)

## The security angle (important)

Cheaper models are easier to jailbreak. Confirmed by research and red-team testing:

- In adversarial tests, Haiku shows significantly higher over-compliance rates than Sonnet or Opus on the same injected prompts
- Smaller open models have been tricked into inserting backdoors into generated code with up to 95% success rates under red-team conditions
- Frontier models (Opus, Sonnet) more reliably recognize and refuse obfuscated or encoded malicious instructions

**What this means for you:** if a task ingests third-party content (scraped sites, inbound emails, partner CSVs) AND takes actions (writes files, sends messages, hits APIs), **don't skimp on the model.** Opus or Sonnet only. A Haiku agent reading untrusted websites and acting on what it finds is a real liability.

## GTM example — prospect research batch

Running the subagent pattern from `agents-and-subagents.md` — 20 subagents enriching 20 accounts:

- **Main agent (orchestrator):** Opus. Decides what to delegate, synthesizes the final report.
- **Each research subagent:** Sonnet. Enough judgment to not get injected by a weird company website. Doesn't need Opus reasoning.
- **Post-processing subagent (formats the final CSV):** Haiku. Pure formatting. Input is Sonnet's clean summaries (trusted). Dirt cheap.

Three tiers doing their jobs. Rough cost vs. all-Opus: cut in half with no quality loss on the important steps.

## Common pitfalls

- **Opus-for-everything.** Burn through usage in a day; no visible quality gain on 80% of tasks.
- **Haiku touching untrusted input.** Injection risk jumps. Don't.
- **Not switching mid-session.** You started on Sonnet, hit a hard architecture decision, kept going. Switch to Opus for the hard part, switch back after.
- **Forgetting subagents have their own model setting.** Main agent on Opus doesn't mean your 20 subagents are. Check in `/agents`.

## Quick reference

| You want to... | Model |
| --- | --- |
| Plan a system or write complex logic | Opus |
| Daily coding, writing, iterating | Sonnet (default) |
| Rename fields, format CSVs, extract simple patterns | Haiku |
| Mix — heavy planning then execution | `/model opusplan` |
| Run many subagents cheaply | Sonnet or Haiku per subagent, Opus on main |
| Process untrusted scraped or inbound content | Sonnet or Opus — never Haiku |

## Rule of thumb

**Sonnet by default. Opus when decisions matter — planning, architecture, code you'll actually ship. Haiku only for mechanical work on trusted input. Anything touching third-party content stays on Sonnet or Opus. Cheap models get jailbroken.**
