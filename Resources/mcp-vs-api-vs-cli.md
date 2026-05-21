# MCP vs API vs CLI

## What it is

There are three ways Claude Code talks to your tools. They look overlapping, but they're not interchangeable — each one is the right tool for a different situation.

- **MCP** — a pre-made USB cable. Plug it in; Claude uses the tool natively.
- **CLI** — a remote control you already own. Claude runs commands you're already authenticated for.
- **API** — the raw wall outlet every tool has. Claude writes code that hits it directly.

Same goal (Claude acts inside your tools). Three different mechanisms with different setup costs and different ceilings.

---

## The mental model

| Method | Metaphor | Setup effort | Flexibility | Context cost |
| --- | --- | --- | --- | --- |
| **MCP** | Pre-made USB cable | Low (one-time install + auth) | Medium — limited to what the MCP exposes | Small (tool search defers loading) |
| **CLI** | Remote you already own | Zero if already installed | Medium — limited to CLI commands | Tiny — Claude just runs bash |
| **API** | The wall outlet itself | Higher (keys, `.env`, docs) | High — anything the tool supports | Depends on the script |

---

## Decision tree

Ask these three questions in order:

1. **Does the tool have an MCP?** → Use the MCP.
2. **No MCP. Do you already have the CLI installed and logged in?** → Use the CLI.
3. **No MCP, no CLI?** → Use the API.

Start at the top every single time. Don't overthink it.

---

## Why the order matters

**MCPs are built for Claude.** They expose a curated set of actions with clear descriptions — Claude knows exactly what each tool can do without reading docs. Low setup, low confusion, natural language end-to-end.

**CLIs are great when available.** Battle-tested, you've already authenticated, and Claude knows the syntax for all the popular ones. But the tool has to have a CLI, and you have to have installed it.

**APIs are the most powerful but most expensive to set up.** Docs reading, key management, `.env` files, error handling, rate limits. Worth every bit of that effort when MCPs and CLIs don't cover your use case — but painful to default to.

---

## GTM example: one workflow, three mechanisms

Building an enrichment pipeline that pulls from HubSpot, enriches via Clay, deploys a dashboard to Vercel:

- **HubSpot → MCP.** Reading contacts and updating deals. The HubSpot MCP exists and handles this natively.
- **Vercel → CLI.** You already have `vercel` installed. Claude deploys with one command. No plumbing.
- **Clay → API.** No MCP (at time of writing). Give Claude the docs + your key, Claude writes the script.

One pipeline. Three mechanisms. Each picked because it's the cheapest path at that step.

---

## Common pitfalls

- **Using the API when an MCP exists.** You're doing 5x the work for no gain.
- **Insisting on APIs "for flexibility"** when an MCP covers what you need. Only graduate to API when you hit a real wall.
- **Installing an MCP when the CLI already works.** If `gh` is installed and authenticated, the GitHub MCP is redundant weight.
- **Mixing mechanisms in one session needlessly.** If you can stay on MCP-only, do. Switching between MCP + CLI + API in one conversation burns context with tool schemas.

---

## Rule of thumb

**MCP first. CLI second. API last. Stop climbing the ladder the moment your use case is covered.**
