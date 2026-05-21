# Project Hierarchies & CLAUDE.md

## How to organize multi-part projects without burning your context window

[https://supercut.ai/share/claude-code-gtm/AD0SXeJaGJTvVgxwpW9YIc](https://supercut.ai/share/claude-code-gtm/AD0SXeJaGJTvVgxwpW9YIc)

---

> ⚠️ Watch the video above, then read this document, and finally watch the project organization example video **AT THE END** to be able to master project hierarchies using CLAUDE.md.

## Why this guide exists

This guide teaches you how to organize bigger projects — projects with subfolders, shared context, and multiple workstreams **when one folder isn't enough.**

---

## What Claude can access by default

When you `cd` into a folder and run `claude`, Claude starts with access to **that folder and everything below it**. It does not, by default, look upward at parent folders. This is a guardrail, not a wall.

### What goes inside CLAUDE.md

CLAUDE.md is **instructions and a map**. It is not where your ICP content lives. It is where Claude learns *where to find* the ICP content and *when to read it*.

---

## The core principle

> **CLAUDE.md is a signpost. Content files are content files. Never merge the two.**
>
- Your ICP lives in `icp.md`.
- Your value prop lives in `value-prop.md`.
- Your brand voice lives in `brand.md`.
- Your `CLAUDE.md` tells Claude: *"These files exist. Here's where they are. Here's when you should read them."*

That's it. If you remember nothing else, remember this.

When you follow this principle, two things fall out automatically:

1. **You update content in one place, and every folder that references it sees the update.** No syncing, no copying.
2. **Your context window stays lean**, because Claude only reads the specific files it needs for the task at hand — not the whole document dump every time.

---

## Two patterns, and when to use each

Most GTM projects fit one of two shapes. Pick the one that matches your work, not the one that sounds fanciest.

### Pattern A: Single-project root

One folder, one CLAUDE.md, content files alongside it. Use this when the project is focused and self-contained.

```
sarah-campaign/
├── CLAUDE.md          ← instructions + map
├── icp.md             ← content
├── value-prop.md      ← content
├── brand.md           ← content
├── prospects.csv      ← data
└── pages/             ← outputs
    ├── sarah.html
    └── marcus.html
```

CLAUDE.md here is short. It says something like: *"You're building personalized landing pages for the prospects in prospects.csv. Read icp.md for audience context, value-prop.md for the offer, brand.md for voice. Output pages into the /pages folder."*

**Use this for:** one-off campaigns, single-purpose builds, the landing pages project.

---

### Pattern B: Multi-workstream root

One parent folder holds shared context. Subfolders each run a different workstream, and each subfolder has its own CLAUDE.md that references the shared files by path.

```
company-sales/
├── CLAUDE.md                   ← master map (high level only)
├── icp.md                      ← shared content
├── value-prop.md               ← shared content
├── brand.md                    ← shared content
│
├── marketing/
│   ├── CLAUDE.md               ← "read ../icp.md, ../brand.md. Handle content."
│   ├── content-calendar.md
│   └── posts/
│
└── outbound/
    ├── CLAUDE.md               ← "read ../icp.md, ../value-prop.md. Handle sequences."
    ├── sequences.md
    └── prospects.csv
```

The ICP file lives in exactly one place. Both subfolders reference it. When you update `icp.md` in the root, both marketing and outbound instantly see the new version next time they run. No copying, no syncing.

**Use this for:** ongoing operations, client work with multiple workstreams, agency work, anything with shared context across projects.

---

## How the "update once, flows everywhere" mechanism actually works

When a subfolder's CLAUDE.md says something like:

> *"For audience context, read `../icp.md`. For offer positioning, read `../value-prop.md`."*
>

…Claude will go up one level and read those files **when you open Claude in the subfolder**. The `../` is the key. It tells Claude: *this file lives one level up from where you are*.

So the flow is:

1. You're working in `outbound/` and discover something new about the ICP during a campaign.
2. You say: *"Update the ICP file with this new insight about mid-market buyers."*
3. Claude updates `../icp.md` — the file in the root folder.
4. Next time you or anyone else opens Claude in `marketing/` or anywhere else that references `../icp.md`, **they get the new version automatically**.

One source of truth. No duplicate files. No sync problems.

---

## The context window trap (and how to avoid it)

If your CLAUDE.md says *"ingest every file in every subfolder before doing anything"*, you will burn your context window before Claude does any real work.

The fix: **CLAUDE.md should tell Claude when to read files, not force it to read everything upfront.**

Good CLAUDE.md instruction:

> *"Shared context files live in the root: icp.md, brand.md, value-prop.md. Read them only when the task requires that context."*
>

Bad CLAUDE.md instruction:

> *"At the start of every session, read all files in the root folder and all subfolders."*
>

The first lets Claude pull in only what's needed for the current job. The second dumps everything into context on every run and leaves you with nothing left for the actual work.

---

## Decision framework: where does this file go?

When you're about to create a new `.md` file and you're not sure where it belongs, run this check:

1. **Is this shared across multiple workstreams?** → Root folder. Reference from subfolders via `../`.
2. **Is this specific to one workstream only?** → That workstream's subfolder.
3. **Is this CLAUDE.md itself?** → Every folder that someone will open Claude inside of. Root and each subfolder.
4. **Is this a one-time reference or progress tracker for a specific build?** → Subfolder where the build happens.

---

## When to open Claude at the root vs. in a subfolder

**Open Claude at the root when:**

- You're planning across workstreams
- You're updating shared context (ICP, brand, positioning)
- You're orchestrating work that spans multiple subfolders

**Open Claude in a subfolder when:**

- You're executing a specific task in that workstream
- You want a focused, lean context window
- You don't need Claude reasoning about unrelated workstreams

The rule of thumb: **open Claude at the lowest level of the tree that still contains everything you need.** Going higher gives more context but costs tokens. Going lower costs less but may miss things.

---

## Common mistakes to avoid

| Mistake | Why it breaks | What to do instead |
| --- | --- | --- |
| Dumping ICP content directly into CLAUDE.md | Pollutes every session with the same 2,000 words whether needed or not | Keep CLAUDE.md short. Put ICP in icp.md. Reference it. |
| Copying shared files into each subfolder | Updates in one place don't flow to others; you end up with stale duplicates | Keep one copy in root, reference via `../` |
| Writing CLAUDE.md as an essay | Claude has to ingest the whole thing every session | Short, structured, map-like. Bullets and paths. |
| Listing every single file in CLAUDE.md | Same context window problem at scale | Only list files Claude needs to know exist. Omit build outputs and data files it can discover itself. |
| No CLAUDE.md in subfolders | Claude doesn't know it's in a sub-context, treats the subfolder as a fresh project | Every folder you'll open Claude in gets its own CLAUDE.md, even a short one |

---

## A concrete example end-to-end

Let's make Pattern B real with an example.

**Root `CLAUDE.md`:**

```
# Company Sales — Master

This folder contains all sales-related work for this company.

## Shared context (read when needed)
- `icp.md` — target customer profile
- `value-prop.md` — positioning and offer
- `brand.md` — voice and tone guidelines

## Workstreams (subfolders)
- `marketing/` — content, social, inbound
- `outbound/` — sequences, prospecting, cold outreach

When you need shared context, read the relevant root file.
When working on a specific workstream, open Claude inside that subfolder instead.
```

**`outbound/CLAUDE.md`:**

```
# Outbound Workstream

You are working on outbound campaigns for a company.

## Context files (read when relevant)
- `../icp.md` — who we target
- `../value-prop.md` — what we lead with
- `../brand.md` — how we sound
- `sequences.md` — active campaign sequences
- `prospects.csv` — current prospect list

## Your job
Build and iterate on outbound sequences. Personalize based on prospect data.
```

**`marketing/CLAUDE.md`:**

```
# Marketing Workstream

You are working on marketing content for a company.

## Context files (read when relevant)
- `../icp.md` — audience
- `../brand.md` — voice
- `content-calendar.md` — what's scheduled

## Your job
Draft content aligned to the calendar and brand voice.
```

Now watch what happens:

- Update `../icp.md` once → both workstreams read the new version next session.
- Open Claude in `outbound/` → focused session, small context, only reads ICP if the task requires it.
- Open Claude at root → cross-workstream orchestration, aware of everything.

## **CLAUDE.md — visual hierarchy**

Here is a walkthrough of a demo GTM agency & how the files are organized with maximum efficiency.

[https://supercut.ai/share/claude-code-gtm/LAtVRDxmAqwjw6KMw3Hmtd](https://supercut.ai/share/claude-code-gtm/LAtVRDxmAqwjw6KMw3Hmtd)

---

## FAQ

**"If I update ICP while working in outbound, does marketing automatically get it?"**
Yes — as long as you update `../icp.md` (the one in root), not a copy inside outbound. That's why we don't copy files between folders.

**"Do I need a CLAUDE.md in every single folder?"**
Every folder where you'll open Claude, yes. Folders you never open Claude in (like `pages/` or `outputs/`) don't need one.

**"How do I stop Claude from reading everything and blowing up my context?"**
Don't instruct it to. Your CLAUDE.md should say *"read X when you need Y"*, not *"read everything at startup."* Trust Claude to pull in files as tasks require.

**"What about for one-off questions — should I still use this structure?"**
No. For quick questions, brainstorming, and one-off research, stay in Claude.ai (the chat interface). This structure is for building things you'll come back to.

**"What if my projects need to share info but aren't really sub-parts of one bigger thing?"**
Then either (a) create a parent folder anyway and treat them as workstreams, or (b) keep them separate and accept that you'll update shared context in multiple places. Option (a) is almost always cleaner.

---

## Takeaway

> CLAUDE.md is a map. Content lives in separate files. Put shared content at the root and reference it from subfolders with `../` — update once, flows everywhere.
>
