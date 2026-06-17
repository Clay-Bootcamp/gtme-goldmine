**[🏠 Course Home](./README.md)**  ·  Module 6 — Connecting to External Systems  ·  Lesson 18 of 27

---

# CLIs (Command-Line Interfaces)

## What it is

**A CLI is a tool you run from the terminal.** If you've ever typed `git commit` or `npm install`, you've used a CLI.

Most modern SaaS tools ship a CLI — GitHub, Vercel, Supabase, Stripe, Twilio, AWS. You install it once, log in once, then run commands like:

- `gh pr create` → opens a GitHub pull request
- `vercel deploy` → deploys a site
- `supabase db push` → pushes database changes

Here's the trick: **once you've installed and authenticated a CLI, Claude Code can use it too.** It just runs the commands inside your session.

Extending the metaphor:

- **MCP** = a pre-made USB cable
- **API** = the wall outlet underneath
- **CLI** = a remote control you already own for the tool

---

## Why it matters for GTM engineers

CLIs are the **free leverage tier.** If you've already got the tool installed, there's no MCP to configure, no API key plumbing, no OAuth dance. Claude already knows the syntax for all the popular ones.

For GTM work, this matters most for:

- **Deploying landing pages** (Vercel CLI)
- **Version control** (GitHub CLI — creating repos, managing issues, opening PRs)
- **Pulling from your own database** (Supabase CLI)

---

## How it works

Three steps, one time each per tool:

1. **Install the CLI** — usually `brew install <tool>` on Mac or `npm install -g <tool>`
2. **Log in** — usually `<tool> login`, which opens a browser
3. **Done.** Claude can now use it.

You don't have to memorize the commands. Tell Claude what you want:

- *"Deploy this site to Vercel"*
- *"Pull the latest users from Supabase"*
- *"Create a new GitHub repo called 'enrichment-agent' and push this code to it"*

Claude runs the right commands. You confirm before anything destructive happens.

---

## GTM example: shipping a personalized landing page

1. Claude writes your landing page HTML.
2. You say *"Deploy this."*
3. Claude uses the **Vercel CLI** to deploy. Live URL in ~30 seconds.
4. You say *"Commit this and push to a new repo."*
5. Claude uses the **GitHub CLI** to create the repo and push.

No MCP installed. No API key set up. Just CLIs you had.

---

## Common pitfalls

- **Forgetting to authenticate.** If a CLI command fails with an auth error, you usually need to re-login. Claude will tell you when this happens.
- **Destructive commands (delete, reset, drop).** Let Claude warn you before it runs anything that can't be undone. Better: install Matt Pocock's `git-guardrails-claude-code` skill to block dangerous git commands automatically.
- **Outdated CLI versions.** If something breaks mysteriously, update the CLI (`brew upgrade <tool>` or `npm update -g <tool>`).
- **Assuming Claude knows your aliases.** If you aliased `gh` to something weird in your shell, Claude's default commands won't work. Tell it, or don't alias.

---

## CLIs worth having installed for GTM work

| CLI | What it does | Install |
| --- | --- | --- |
| **gh** (GitHub) | Repos, PRs, issues, releases | `brew install gh` |
| **vercel** | Deploy landing pages and serverless functions | `npm i -g vercel` |
| **supabase** | Database, auth, storage | `brew install supabase/tap/supabase` |
| **stripe** | Payments, webhooks (if you sell anything) | `brew install stripe/stripe-cli/stripe` |

Don't install all four at once. Install when you need them.

---

## Rule of thumb

**If the tool has a CLI and you've installed it, Claude can already use it. No MCP, no API plumbing — just ask for what you want.**

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [APIs](./17-apis.md) | [All Lessons](./README.md) | [MCP vs API vs CLI](./19-mcp-vs-api-vs-cli.md) |
