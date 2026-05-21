# APIs

## What it is

**Every SaaS tool has an API.** An API is the official endpoint that software uses to talk to a tool — how your code reads from HubSpot, sends through Gmail, pushes to Slack.

Extending the USB metaphor:

- **MCP = a pre-made USB cable.** Plug it in, Claude uses the tool.
- **API = the wall outlet underneath.** When no MCP exists, you go straight to the outlet.

Three things you need to know about any API:

- **Endpoint** — the URL you hit (think: phone number for the tool)
- **API key** — your password (never share, never commit to git)
- **Docs** — where the API is explained

Claude handles the rest.

---

## Why it matters for GTM engineers

When no MCP exists, the API is your fallback. And APIs are more flexible — they can do anything the tool supports, not just what an MCP exposes.

More importantly: **APIs are how you build.** Nightly enrichment jobs, custom dashboards, automated outreach — they all sit on top of APIs.

Anything Zapier/Make can't do, an API probably can.

---

## You don't write API calls

**You never have to learn JSON, HTTP methods, auth headers, or query parameters.**

You give Claude:

1. The API docs URL (Claude reads them — or Claude already knows, for big APIs like HubSpot, OpenAI, Stripe)
2. Your API key (Claude sets up a `.env` file for you)
3. What you want in plain English

Example:

> *"Build me a script using the Clay API that takes a CSV of companies, enriches them with firmographic data, and writes to a second CSV. Run it nightly."*
>

Claude writes the code, sets up the schedule, ships it.

---

## Common pitfalls

- **Committing API keys to git.** The single biggest mistake. Always use `.env` + `.gitignore`. Claude will set this up — make it default. Ask Claude to add a pre-commit hook that blocks keys from ever being committed.
- **Hitting rate limits silently.** Every API caps how often you can call (e.g., 100 req/minute). Claude can add retry + backoff logic. Just ask.
- **Guessing at endpoints.** Don't. Paste the docs URL. Claude parses it faster than you'll read it.
- **Leaving test keys active.** Rotate keys after testing. Revoke old keys. Especially if you ever shared your screen while one was visible.

---

## APIs worth knowing for GTM work

| API | What it does |
| --- | --- |
| **HubSpot** | Contacts, companies, deals, custom properties |
| **Clay** | Enrichment, research, provider waterfalls |
| **Apollo** | B2B lead data |
| **OpenAI / Anthropic** | LLM calls (for your own AI features) |
| **Exa** | AI-native web search |
| **Gmail** | Drafting, sending, inbox reading |
| **Supabase** | Your own database and auth |

---

## Rule of thumb

**If there's no MCP, there's almost always an API. Paste the docs URL, give Claude your key, tell it what you want. Claude writes the code — you run it.**
