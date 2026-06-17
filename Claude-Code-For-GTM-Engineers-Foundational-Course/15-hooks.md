**[🏠 Course Home](./README.md)**  ·  Module 5 — Workflow Building Blocks  ·  Lesson 15 of 27

---

# Hooks

## What it is (plain English)

**Hooks = Zapier triggers for your Claude Code session.** When a specific event happens — Claude's about to write a file, Claude just ran a Bash command, your session is starting — a shell command runs automatically.

**Prompts are suggestions. Hooks are guarantees.** *"Always back up the CSV before editing"* is a prompt (Claude might forget). A PostToolUse hook on `Edit` that copies the file to a backup folder **will fire every single time**, regardless of the prompt, the session, or whether Claude even remembers.

You won't live in this file, but understanding hooks matters because (a) shared skills and team setups often ship with them, and (b) two or three well-placed hooks can dramatically tighten your workflow.

## Why it matters for GTM engineers

- **Guardrails that don't rely on Claude remembering.** Your `.env` file full of API keys? A hook can hard-block Claude from touching it, regardless of session, prompt, or permission mode.
- **Deterministic automation.** Auto-backup `leads.csv` before every edit. Auto-format CSVs after every write. Slack-ping you when a 20-account enrichment batch finishes. Zero prompting.
- **Team-wide enforcement.** Hooks committed to `.claude/settings.json` apply to every teammate automatically. Beats asking politely.

## The key events

| Event | When it fires | What it's good for |
| --- | --- | --- |
| **PreToolUse** | Before Claude uses a tool | Block dangerous actions (writes to `.env`, destructive Bash) |
| **PostToolUse** | After a tool succeeds | Auto-format, backup, validate |
| **SessionStart** | Session opens | Load context, set environment |
| **Stop** | Claude finishes responding | Notifications, logs |

There are more (UserPromptSubmit, SubagentStop, Notification, etc.) — `/hooks` shows them all. These four cover ~90% of what you'll use.

## Setting one up

Run **`/hooks`** inside a session. The UI walks you through:

1. **Pick an event** (`PreToolUse`, `PostToolUse`, etc.)
2. **Add a matcher** — which tool(s) this fires on (`Edit|Write` for file changes, `Bash` for commands)
3. **Add the command** — what to run when it fires

Saved to `.claude/settings.json` (project, shared with team) or `~/.claude/settings.json` (user, all projects).

Or just ask Claude: *"Add a PreToolUse hook that blocks edits to any `.env` file."* Claude writes the config.

## Three hooks worth setting up today

1. **Protect sensitive files.** PreToolUse on `Edit|Write` that blocks writes to `.env`, `.git/`, and production configs. Even in acceptEdits mode, this is a hard firewall.
2. **Auto-backup before edits.** PostToolUse on `Edit|Write` that copies the original file to a `.backups/` folder before changes. Saves you when Claude overwrites something important.
3. **Notify on completion.** Stop hook that fires a desktop notification or Slack ping when Claude finishes. Useful for long agentic jobs — like the 20-subagent batches from [Agents & Subagents](./13-agents-and-subagents.md).

## Common pitfalls

- **Writing hooks from scratch when you don't need to.** Copy battle-tested hooks from shared team configs or Anthropic's docs. Reinventing is where bugs live.
- **Slow hooks slow everything.** Each matched hook runs synchronously before/after its tool call. A slow script becomes a tax on every action. Keep hooks fast or mark them `async` when possible.
- **Hooks fire on subagents too.** Your safety gates apply recursively (good). Slow hooks compound across every subagent tool call (bad).
- **Using hooks when a prompt would do.** Hooks are for things that MUST fire every single time. Protecting a file, backing up data, pinging notifications — hook. "Be thorough in your research" — prompt.

## Quick reference

| You want to... | Event | Matcher |
| --- | --- | --- |
| Block writes to sensitive files | PreToolUse | `Edit|Write` |
| Block risky Bash commands | PreToolUse | `Bash` |
| Auto-format or back up after changes | PostToolUse | `Edit|Write` |
| Inject context when session starts | SessionStart | — |
| Get pinged when Claude's done | Stop | — |
| See or manage all hooks | `/hooks` | — |

## Rule of thumb

**Hooks are guarantees. Prompts are suggestions. If something absolutely must happen every time — protecting a file, backing up data, firing a notification — use a hook. For anything softer or one-off, just prompt Claude. Start with 2-3 hooks, not twenty.**

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Model Selection](./14-model-selection.md) | [All Lessons](./README.md) | [MCPs (Model Context Protocol)](./16-mcps.md) |
