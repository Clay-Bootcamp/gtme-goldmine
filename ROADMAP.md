# GTM Goldmine — Roadmap

Every GTM engineering project I'll build live, in public, with Claude Code. Checkbox flips when the build ships.

**Legend:** ⬜ queued · 🟡 building · ✅ shipped

Tiers reflect skill level needed to build, not value delivered.

- 🟢 **Beginner** — terminal, file ops, simple scripts, deploy. No external orchestration.
- 🟡 **Intermediate** — APIs, MCPs, scheduled jobs, multi-step workflows.
- 🔴 **Advanced** — multi-agent systems, autonomous loops, servers, production infra.

---

## 🟢 Beginner

1. ⬜ **First Claude Code Project: Install to "It Works"** — Install CC, navigate the terminal, run your first prompt. The zero-to-one onboarding for total newcomers.
2. ⬜ **Landing Page / Portfolio Website in Under an Hour** — Scrape your LinkedIn, generate a personal or business site, deploy free to Vercel/Netlify.
3. ⬜ **CSV Cleanup & Enrichment** — Dedupe, normalize fields, basic enrichment on messy spreadsheets. Replaces hours of manual list cleaning.
4. ⬜ **Lead Scoring from a CSV** — Slash command that scores a lead list against ICP criteria and outputs a prioritized file.
5. ⬜ **Sales Email Personalizer** — Visit a prospect's site, extract signals, draft a personalized email, push to Instantly/Smartlead.
6. ⬜ **LinkedIn Content System: Inspiration + Drafting** — Pull top-performing posts in a niche, extract hooks/formats, draft new posts in your voice using `CLAUDE.md`.
7. ⬜ **Transcript Mining (3 Flavors)** — Drop transcripts (sales calls, support tickets, webinars) into a Claude Project and mine them. Same build, three outcomes:
   - **Sales** — objections, winning phrases, competitor mentions, pricing discussions, deal-killers.
   - **LinkedIn content** — pull real customer language and turn it into hooks, posts, and angles.
   - **Customer support FAQ** — surface recurring questions and the best answers, build an internal knowledge base.
8. ⬜ **Client / CRM Reporting Dashboard** — Take campaign or CRM data and produce a branded HTML dashboard with charts. No-code feel.
9. ⬜ **Claude Code Controls Google Chrome** — Headless browser tasks, including the "grab hidden YouTube channel emails" trick.
10. ⬜ **Build n8n Workflows With Claude Code** — Use CC to scaffold and edit n8n flows instead of clicking through the GUI.
11. ⬜ **Edit a Video with Claude Code (FFmpeg)** — Trim, caption, splice clips by talking to CC instead of learning FFmpeg syntax.
12. ⬜ **Deanonymize Website Visitors → Warm Email** — RB2B-style visitor identification → research → semi-cold-semi-warm outreach.
13. ⬜ **Apify / Firecrawl Web Scraping** (incl. Google Maps via Serper/RapidAPI) — Pull public directory and map data at scale for lead lists.
14. ⬜ **ICP Scoring & Account Qualification Machine** — Account-level fit scoring + enrichment + ranking in one workflow.

---

## 🟡 Intermediate

15. ⬜ **Job Posting Scraper → Sequence Add** — Track hiring signals, scrape hiring managers, auto-add to outreach sequences. The cleanest signal-based outbound play.
16. ⬜ **Deep Prospect Research Agent (Exa MCP)** — Person/company name in → deep research out: news, funding, hiring signals, exec moves, recent activity.
17. ⬜ **Signal-Based Outbound Engine** — Monitor hiring, funding, tech stack changes, leadership moves. Score and prioritize accounts automatically (SignalBase-style).
18. ⬜ **Trello / Project Tool Controller** — Create cards, move tasks, comment from the terminal via MCP.
19. ⬜ **Pipeline Hygiene Automation** — Weekly job that flags stale deals, suggests next actions, surfaces forecast risk.
20. ⬜ **Proactive Churn Detection** — Monitor usage drops, support ticket spikes, payment issues. Assign risk scores, alert CS.
21. ⬜ **Content Engine from Conversations & Webinars** — Ingest sales/support calls or webinars → blog posts, LinkedIn content, customer success docs, email sequences.
22. ⬜ **Playwright Browser Automation** — Form filling, data extraction, screenshots for sites without APIs.
23. ⬜ **Daily Website Observer → Slack Alerts** — Crawl target accounts daily, diff for meaningful changes, post outreach angles to Slack.
24. ⬜ **LinkedIn People/Company Watchlist → Slack Digest** — Track job changes, posts, company updates across a watchlist; daily "why this matters" digest.
25. ⬜ **AI Phone Call Handler** — Voice agent for scheduling, confirmations, basic inquiries. Async phone calls.
26. ⬜ **AI News Daily Digest (Cron)** — Scheduled job that monitors AI/industry developments and posts a signal-not-noise summary.
27. ⬜ **Slack → OpenAI → Notion Content Pipeline** — Classic three-stage workflow: Slack message (voice memo, raw idea, transcript) triggers the run, OpenAI processes and structures it, output lands as a draft page in Notion. Easy to retarget to other inputs/outputs once the pattern clicks.
28. ⬜ **Claude Code as Proactive Project Manager** — CC tracks projects, nudges you, surfaces blockers (likely needs OpenClaw / async loop).
29. ⬜ **Attio Invisible CRM** — Auto-populate fields by stage, detect data decay, flag stale deals, generate loss reasons from calls — directly in Attio.
30. ⬜ **Copywriting Agent (Your Voice, No Slop)** — General-purpose copywriter trained on your own writing. Emails, LinkedIn, blog, landing pages — same voice, no AI tells.
31. ⬜ **Automate Client Onboarding** — Intake forms, onboarding docs, project scaffolding, client briefs in one chain.
32. ⬜ **Social Listening & Content Gap Finder** — Track competitor C-suite LinkedIn activity, surface content gaps and engagement opportunities.
33. ⬜ **Claude Code + Clay: Programmable Tables** — Use CC to launch, optimize, and run Clay tables. Bridge between Clay GUI and code.

---

## 🔴 Advanced

34. ⬜ **Cold Email Machine** — Multi-agent pipeline: research → qualify → write → send. Give CC an ICP doc, get back validated leads with verified contacts. *Check with Kushagra first — he may already be building this.*
35. ⬜ **Build Your Own n8n / Trigger.dev Workflow Orchestration** — Either roll your own orchestrator or wire CC into n8n/Trigger.dev as the "brain" with retry, observability, self-healing.
36. ⬜ **Webhook Receiver Server** — Server that listens for external webhooks and kicks off CC workflows.
37. ⬜ **Customer Listening Engine → Product Roadmap** — Ingest support, calls, CRM notes; extract feature requests; auto-populate roadmap.
38. ⬜ **Async Project Architect (Background Agents)** — Long-running agents that monitor repos, run competitive research, prep morning briefings while you sleep.
39. ⬜ **Agents SDK for Your Business** — Custom agents built on the Anthropic Agents SDK for internal company workflows.
