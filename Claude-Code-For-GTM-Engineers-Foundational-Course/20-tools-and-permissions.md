**[🏠 Course Home](./README.md)**  ·  Module 7 — Security & Permissions  ·  Lesson 20 of 27

---

# Tools & Permissions

## What it is (plain English)

Every time Claude Code does something on your machine — reads a file, searches your CSV, fetches a URL, runs a command — it's using a **built-in tool**. You don't call these tools. You tell Claude what you want in plain English, Claude picks the right tool.

**Permissions are the guardrails.** Before Claude does anything that could change your stuff, you get a prompt: *Allow once / Always allow / Deny*. That prompt is your steering wheel.

## Why it matters

1. **The prompt is your steering wheel.** When Claude asks *"Allow Edit?"*, you need to know what Edit means so you can decide. Clicking Allow blindly is how things break.
2. **Non-technical GTMEs get spooked by prompts and click "Always allow" on everything to shut them up.** That's how Claude ends up overwriting your master lead list. Learn the modes. Use them.

## The tools that matter

Seven core tools cover ~95% of what Claude does. You never type these — Claude picks them.

| Tool | What Claude does | Prompts you? |
| --- | --- | --- |
| **Read** | Opens a file on your machine | No |
| **Grep / Glob** | Searches file contents or filenames | No |
| **Write** | Creates a new file | Yes |
| **Edit** | Changes part of an existing file | Yes |
| **Bash** | Runs a terminal command | Yes |
| **WebFetch** | Reads a specific URL | Yes |
| **WebSearch** | Searches the web | Yes |

Read-only tools are auto-approved. Anything that changes files or hits the internet prompts you. That's the default safety posture.

> Subagents (`Task`) and skills run through this same tool layer — see [Agents & Subagents](./13-agents-and-subagents.md) and [Skills & Slash Commands](./11-skills-and-slash-commands.md).
>

## Permission modes (this is the important part)

Press **Shift+Tab** inside a Claude Code session to cycle modes. The current mode shows in the status bar.

| Mode | How to activate | What it does | When to use |
| --- | --- | --- | --- |
| **default** | On startup | Asks before any file change, Bash command, or web call | Most of the time |
| **acceptEdits** | Shift+Tab once | Auto-approves Edit/Write; Bash still prompts | Iterating on a trusted project, prompts breaking flow |
| **plan** | Shift+Tab twice | Read-only — Claude researches + proposes, can't change anything | Big refactors, early exploration (see the Golden Prompts Framework) |
| **bypassPermissions** | `--dangerously-skip-permissions` flag | ⚠️ Skips every check | **Sandbox / VM / throwaway project only.** |

Three things to know:

- **Some paths are always protected.** Even in acceptEdits, Claude can't auto-write to `.env`, `.gitignore`, or its own config. You'll always get prompted for those.
- **You can pre-approve patterns** to kill prompt fatigue. Type `/permissions` inside a session to open the UI, or edit `.claude/settings.json` to always allow things like `Bash(git status:*)` or `Read`.
- **Auto mode** (newer, classifier-based) is a middle ground — auto-approves safe actions, blocks risky ones. Appears in the Shift+Tab cycle if your plan supports it.

## GTM example — lead enrichment

You tell Claude: *"Enrich the 50 leads in `leads.csv` with a one-line company description scraped from their website."*

Claude picks tools in sequence:

1. **Read** `leads.csv` — no prompt
2. **Grep** to find the URL column — no prompt
3. **WebFetch** the first company site → *"Allow WebFetch?"* → Always allow
4. **Write** `leads-enriched.csv` → *"Allow Write?"* → Always allow for this file
5. **Edit** the original `leads.csv` if you asked for in-place updates → prompt fires because it's touching your source data

Two clicks and you're in flow. That's default mode working as designed.

## Common pitfalls

- **Clicking "Always allow" on `Bash` with no scope.** That pre-approves *any* Bash command forever for this project. Scope it: `Bash(git:*)` or `Bash(npm run test:*)`.
- **Using `-dangerously-skip-permissions` to "save time."** You are one bad prompt away from `rm -rf` on real files. If you need unattended execution, run Claude Code inside a Docker container or a throwaway folder.
- **Staying in acceptEdits for destructive work.** It auto-approves edits across the whole session. Shift+Tab back to default before a big refactor.
- **Ignoring the prompt.** Read what Claude wants to do before clicking Allow. The prompt is information, not friction.

## Quick reference

| You want to... | Do this |
| --- | --- |
| Let Claude explore but not change anything | Plan mode (Shift+Tab twice) |
| Iterate fast on a trusted project | acceptEdits mode (Shift+Tab once) |
| Pre-approve a common command | `/permissions` or edit `.claude/settings.json` |
| Run unattended in a sandbox | `--dangerously-skip-permissions` (isolated env only) |
| See what tools are active in a session | Just ask Claude: *"what tools do you have access to?"* |

## Rule of thumb

**Stay in default. Shift+Tab to acceptEdits when prompts are breaking flow on a project you trust. Use plan mode for anything big. Never use `--dangerously-skip-permissions` outside a sandbox — there's no undo.**

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [MCP vs API vs CLI](./19-mcp-vs-api-vs-cli.md) | [All Lessons](./README.md) | [Security & Privacy Primer](./21-security-and-privacy.md) |
