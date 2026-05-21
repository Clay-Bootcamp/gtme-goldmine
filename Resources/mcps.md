# MCPs (Model Context Protocol)

## What it is

**MCPs are the USB cable for AI.**

Your laptop has USB ports. You plug in a mouse, a keyboard, a monitor, a hard drive — the laptop doesn't need to know anything special. It just works.

MCPs are the same thing for Claude Code. They're the universal plug that lets Claude connect to your tools — HubSpot, Gmail, Slack, Notion, your database, your CRM, whatever you actually use.

Without MCPs, Claude Code is a brain with no hands.
With MCPs, Claude can read from and write to the tools you live in every day.

---

## Why it matters for GTM engineers

**You stop copy-pasting.**

Right now, prospect research looks like:
Open HubSpot → copy company → paste into Claude → get output → copy back to Gmail → send.

With MCPs connected, prospect research looks like:
*"Research Acme Corp. Check if they're already in HubSpot. If not, draft three outreach emails in Gmail."*

One sentence. Claude reads HubSpot, pulls Exa for research, drafts in Gmail. Done.

Five tabs collapse into one conversation.

---

## You don't need to learn commands

Here's the best part: **you don't have to memorize any technical syntax to install an MCP.**

Just tell Claude Code in plain English what you want to plug in:

- *"Add the HubSpot MCP"*
- *"I want to connect Slack"*
- *"Help me install the Gmail MCP"*

Claude handles the rest. It knows the URL, it walks you through auth (usually a browser popup where you click "authorize"), and it confirms when you're connected.

To check what's plugged in, just ask:
*"What MCPs do I have connected?"* — or type `/mcp` in the session.

To disconnect:
*"Remove the HubSpot MCP."*

That's the whole interface. Natural language in, working connections out.

---

## GTM example: prospect research pipeline

With HubSpot, Exa, Gmail, and Slack plugged in:

> *"Check if Acme Corp is in HubSpot. If not, research them on Exa, find their top 3 decision-makers, draft personalized outreach emails in Gmail, and post in #outbound when ready."*
>

Claude does all four things in one turn.

That's the whole game.

---

## MCPs worth connecting for GTM work

| MCP | What Claude can do with it |
| --- | --- |
| **HubSpot** | Read contacts, deals, companies; update records |
| **Gmail** | Read inbox, draft and send emails |
| **Slack** | Read messages, post updates, search history |
| **Notion** | Pull from your wiki, update pages, search |
| **Exa** | AI-native web search for company/person research |
| **Postgres / Supabase** | Query your own databases |

Don't plug in all of them. Plug in the tools you actually copy-paste from.

---

## Common pitfalls

- **Don't install random MCPs from the internet.** Same rule as skills: untrusted MCPs can read your data and send it anywhere. Stick to official ones (HubSpot, Google, Slack, Anthropic, vendors you already trust).
- **If an MCP suddenly stops working**, type `/mcp` in the session. Usually it just needs you to re-authenticate — one click in the browser and you're back.
- **Don't plug in an MCP before you need it.** Copy-paste from a tool 3+ times first. Then connect it. Otherwise you're collecting cables for devices you don't own.
- **Don't put MCPs with sensitive credentials into team-shared configs.** If Claude asks you about scope, keep personal MCPs on your personal scope.

---

## Rule of thumb

**Tell Claude what you want to plug in — in plain English. Let Claude handle the technical stuff. Only connect MCPs for tools you actually use every week.**
