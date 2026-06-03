# Install Claude Code

## Why You Need This

Claude Code is an AI assistant that runs in your terminal. You'll have conversations
with it—literally talking out loud—and it will write code, create files, and build
your tool for you.

## Installation

### **Step 1: Get Claude Pro ($20/month)**

Claude Code requires a paid Claude Pro or Max subscription.

1. Go to [https://claude.ai](https://claude.ai/)
2. Sign up or log in
3. Click on your profile → **Upgrade to Pro** ($20/month)

Max ($100/month) also works if you want higher limits, but Pro is sufficient to start with.

### **Step 2: Install Claude Code**

**Mac / Linux:**

1. Open Terminal (search "Terminal" in Spotlight on Mac)
2. Paste this command and press Enter:

    `curl -fsSL https://claude.ai/install.sh | bash`

3. Close Terminal completely (Cmd+Q) and reopen it
4. Type `claude` and press Enter
5. Follow the prompts to log in with your Claude.ai account

**Windows:**

1. Open PowerShell (search "PowerShell" in Start menu)
2. Paste this command and press Enter:

    `irm https://claude.ai/install.ps1 | iex`

3. Close PowerShell completely and reopen it
4. Type `claude` and press Enter
5. Follow the prompts to log in with your Claude.ai account

## ✓ Verify It Worked

After logging in, you should see the Claude Code interface—a chat-like prompt where
you can type messages.

**✓  Success looks like:** You see a `>` prompt and can type to Claude.

Type "hello" and press Enter. If Claude responds, you're all set.

## **Troubleshooting**

**"command not found: claude"**

- Close your terminal completely (not just the tab—quit the app) and reopen it
- Try `claude` again

**"permission denied"**

- Mac/Linux: Run with sudo:
`sudo curl -fsSL https://claude.ai/install.sh | bash`

**Windows: "script is blocked" or "execution policy" error**

1. Close PowerShell
2. Right-click PowerShell → **Run as Administrator**
3. Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
4. Type `Y` to confirm
5. Now run the install command again

**Authentication issues**

- Make sure you're logged into [claude.ai](http://claude.ai/) in your browser first
- Then run `claude` and follow the login prompts

**Something else broken?**

- Run `claude doctor` to diagnose issues
- Or paste your error into [claude.ai](http://claude.ai/) and ask for help
