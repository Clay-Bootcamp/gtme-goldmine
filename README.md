# GTM Engineering Goldmine

**Every GTM engineering project worth building, built live, in public, with Claude Code.**

This repo is the public companion to a multi-month build series. 38 projects across three tiers — from "ship a landing page" to "autonomous multi-agent outbound." Each one gets built live on stream. Code, prompts, notes, and giveaways land here as soon as the stream wraps.

---

## What's here

- **[`Foundations/`](./Foundations/)** — Start here. Install, smoke test, and the Golden Prompts Framework. Linear sequence — do them in order.
- **[`Resources/`](./Resources/)** — Reference docs on CLAUDE.md, context management, skills, agents, MCPs/APIs/CLIs, security, and GitHub. Lookups, not a curriculum. The [TOC](./Resources/README.md) groups everything by topic.
- **[`ROADMAP.md`](./ROADMAP.md)** — The list and the roadmap, in one. All projects with status checkboxes. ⬜ → 🟡 → ✅ as builds ship.
- **[`projects/`](./projects/)** — One folder per build. Each contains a `README.md` with the exact prompt to give Claude Code so you can build **your own version** — plus my reference implementation for show. Populated as each project ships live.

---

## New to Claude Code?

Start with **[Foundations](./Foundations/)** — install Claude Code, run a 2-minute smoke test, and learn the Golden Prompts Framework. Roughly 30 minutes end-to-end. Once those land, you're ready to follow any build in the roadmap.

---

## How to use this repo

> **Don't copy the code.** Copying my output teaches you nothing. The point is the *method*, not the artifact.

Every project folder has a `README.md` with a copy-pasteable prompt. Paste it into Claude Code, answer the 5 questions it asks you, approve the plan, and build *your* version — same project, your spec. The prompts run on the **Golden Prompts Framework**: **Think → Ask → Plan → Build**. ([Read the full framework →](./Foundations/03-Golden-Prompts-Framework.md))

Here's the loop:

- **Watch live** — every project starts as a live build. Code is messy. Decisions are made on camera. No edits.
- **Read the project README** — when a build wraps, the folder under `projects/` gets the prompt, the framework reference, and my reference implementation.
- **Run the prompt yourself** — open Claude Code in your own folder, paste the prompt, answer honestly. Claude grills you, plans, then builds *your* version. Ship something that's actually yours.
- **MIT-licensed reference** — the code is in the open if you want to peek under the hood. But don't ship mine as yours — it won't fit your circumstances and you won't have learned the method.

---

## Tiers at a glance

🟢 **Beginner** — Terminal comfort, file ops, simple scripts, deploys. No external orchestration.
🟡 **Intermediate** — APIs, MCPs, scheduled jobs, multi-step workflows.
🔴 **Advanced** — Multi-agent systems, autonomous loops, servers, production infra.

See [`ROADMAP.md`](./ROADMAP.md) for the full list.

---

## Get notified when builds go live

Subscribe to **[The New GTM Engineer](https://thenewgtmengineer.substack.com/about)** for a heads-up before every live stream. Drops straight in your inbox — no algorithm in the way.

---

## Connect

- 💬 **Connect with me on LinkedIn** → [Tanay Mishra](https://www.linkedin.com/in/tanay-mishra-ai-automation/) — say hi, share what you're building, ask anything.
- 🎓 **Want the structured version?** Check out **[Clay Bootcamp](https://www.claybootcamp.com/)** — the fastest way to go from zero to shipping GTM systems.

---

## Status

🟢 Live and shipping. Four builds are up — a landing-page generator, a CSV cleanup-and-enrichment pipeline, a CSV lead scorer, and a sales email personalizer that scales one winning template across many sites. See [`ROADMAP.md`](./ROADMAP.md) for what's shipped and what's next.
