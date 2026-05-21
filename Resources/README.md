# Resources

Reference docs for the GTM Goldmine. Read **[Foundations](../Foundations/)** first — those four lessons get Claude Code on your machine and teach the prompting framework. Everything below is "look it up when you need it."

Each doc is short on purpose. Skim what's relevant. Come back when you hit the problem it solves.

---

## Why & What

- **[Why Claude Code?](./why-claude-code.md)** — The argument for why GTMEs should pick this up.
- **[Claude Code's Capabilities](./claude-code-capabilities.md)** — What it actually does that ChatGPT and Perplexity can't.

## Project Setup & Memory

- **[CLAUDE.md files and how to use them](./claude-md-files.md)** — The signboard file that orients Claude at the start of every session.
- **[Project Hierarchies & CLAUDE.md](./project-hierarchies.md)** — How to organize multi-folder projects so shared context flows everywhere automatically.
- **[Context Management & Context Rot](./context-management.md)** — The 150K rule, when to `/clear`, and how to keep Claude sharp over long sessions.

## Workflow Building Blocks

- **[Skills and Slash Commands](./skills-and-slash-commands.md)** — Reusable workflows you invoke with `/your-skill`. Stop copy-pasting prompts.
- **[Recommended Skills](./recommended-skills.md)** — The 2–3 worth installing today, plus the case for writing your own.
- **[Agents and Subagents](./agents-and-subagents.md)** — Delegate noisy, context-heavy work to subagents so your main thread stays clean.
- **[Model Selection](./model-selection.md)** — When to use Opus, Sonnet, or Haiku. The cost-and-security calculus.
- **[Hooks](./hooks.md)** — Guarantees vs. suggestions: shell commands that fire automatically on session events.

## Connecting to External Systems

- **[MCPs (Model Context Protocol)](./mcps.md)** — The USB cable. Pre-built integrations to HubSpot, Gmail, Slack, Notion, etc.
- **[APIs](./apis.md)** — The wall outlet. When no MCP exists, Claude writes the API code for you.
- **[CLIs (Command-Line Interfaces)](./clis.md)** — The remote you already own. Tools like `gh` and `vercel` Claude can drive directly.
- **[MCP vs API vs CLI](./mcp-vs-api-vs-cli.md)** — The decision tree for picking the cheapest integration path.

## Security & Permissions

- **[Tools & Permissions](./tools-and-permissions.md)** — The seven core tools and the permission modes (default / acceptEdits / plan / bypass).
- **[Security & Privacy Primer](./security-and-privacy.md)** — Six rules to keep you and your customers' data out of trouble.

## Practical Use Cases

- **[Browser Navigation Use Cases for GTM](./browser-navigation-for-gtm.md)** — Multi-page research, CRM busywork, SaaS automation — what Claygent and scrapers can't touch.
- **[Systems Design GTM Agent](./systems-design-gtm-agent.md)** — Download a ready-made agent for systems design conversations.

## GitHub & Deployment

- **[Introduction to GitHub](./github/01-introduction.md)** — The Dropbox-for-code mental model and repo anatomy.
- **[Link GitHub to Claude Code](./github/02-link-github-to-claude-code.md)** — One prompt to wire up your terminal to GitHub.
- **[Commit & Restore](./github/03-commit-and-restore.md)** — The only two Git commands you need to know.
- **[Connect GitHub and Vercel](./github/connect-github-and-vercel.md)** — Auto-deploy your website every time you push.
