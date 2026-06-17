**[🏠 Course Home](./README.md)**  ·  Module 2 — Setup & Installation  ·  Lesson 6 of 27

---

# Your First Claude Code Project (Smoke Test)

> ## 📺 Video Lesson
> **▶️ [Watch the Supercut walkthrough](https://supercut.ai/share/claude-code-gtm/3Q6pF1sZY4-VAttCgP82_O)**
>
> This lesson has a video. Watch it first, then follow the steps below.

## What this is

This is a smoke test — a quick check to make sure Claude Code is installed correctly and working on your machine. If this works, you're fully prepped to start building.

**Time needed:** ~2 minutes

## Before you start

Make sure you've completed the setup pre-work from the earlier lessons in this module:

- ✓ Claude Code is installed → [Lesson 4](./04-install-claude-code.md)
- ✓ You're logged into your Anthropic account
- ✓ You can launch Claude Code from your terminal

## Step 1: Create a project folder

**Mac:**

1. Open Finder
2. Go to your Documents folder (or Downloads—wherever you prefer)
3. Click the New Folder icon and name it `hello`

**Windows:**

1. Open File Explorer
2. Go to your Documents folder
3. Right-click → New → Folder and name it `hello`

## Step 2: Open terminal **in that folder**

**Mac:**

- Right-click on the `hello` folder → Services → New Terminal at Folder

**Windows:**

- Open PowerShell
- Type: `cd Documents\hello` (adjust the path if you put it somewhere else)

Make sure your terminal shows `hello` in the path—this confirms you're in the right place.

## Step 3: Launch Claude Code

- In your terminal, type: `claude`
- Press Enter.

If everything is working, you'll see the Claude Code interface with a prompt ready for your first command.

## Step 4: Your first command

- Type (or speak) this to Claude:

    Create a file called test.txt that says "Hello world from Claude Code"

- Press Enter.
- Claude will ask for permission to create the file. Click **Yes** or **Allow**.

## Step 5: Verify it worked

1. Go back to Finder/File Explorer
2. Open your `hello` folder
3. Double-click on `test.txt`

You should see: **Hello world from Claude Code**

## 🎉 You did it!

You've just had your first real conversation with Claude Code, and it followed through on your instructions. Everything from here builds on this exact loop: tell Claude what you want, approve the actions, verify the result.

## Something not working?

Common fixes:

- **"command not found: claude"** → Close and reopen your terminal, then try again
- **Claude won't create the file** → Make sure you're in the `hello` folder (check your terminal path)
- **Authentication issues** → Run `claude` again and follow the login prompts

If you're still stuck, paste the exact error into [claude.ai](https://claude.ai) and ask it to help you troubleshoot — it knows Claude Code's install flow better than any FAQ can document.

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Set Up Speech-to-Text](./05-setup-speech-to-text.md) | [All Lessons](./README.md) | [The Golden Prompts Framework](./07-golden-prompts-framework.md) |
