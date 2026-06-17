**[🏠 Course Home](./README.md)**  ·  Module 8 — Practical Use Cases  ·  Lesson 22 of 27

---

# Browser Navigation Use Cases for GTM

## **What Claude Code Can Do That Claygent & Scrapers Can't**

The differentiator: **multi-step navigation + reasoning across pages.** Claygent visits one URL and extracts. A scraper pulls static HTML. Claude Code clicks around, follows links, makes decisions about where to go next, and synthesizes across multiple pages in one session.

---

## **External Research & Intelligence**

### **Multi-Page Account Research in One Pass**

Visit a company's homepage → pricing page → case studies → careers, and produce a unified account brief. Claygent needs 4 separate calls that you stitch together manually. Claude Code does it in one prompt.

### **Discovery When You Don't Have the URL**

"Find where this company lists their integrations" or "find their SOC 2 compliance page." There's no direct URL to hand a scraper — you need an agent that explores the site and clicks until it finds it.

### **Dynamic & Interactive Content**

Sites with tabs, dropdowns, "show more" buttons, JS-rendered content. A scraper gets a blank page. Claude Code clicks and waits for content to load.

### **Multi-Site Synthesis**

Visit a prospect's website → check their G2 reviews → look at their LinkedIn company page → produce one research brief. One agent, one prompt, multiple destinations, one output.

### **Competitive Analysis With Judgment**

"Visit these 5 competitor pricing pages and tell me who's cheapest for a 50-seat team." That requires reading, comparing, and reasoning across sites — not just extracting fields.

### **Reverse-Engineering Site Structure**

Map out a competitor's content hub, resource library, or help center to find strategic gaps. You can't hand Claygent a URL for "figure out how their docs are organized."

---

## **SaaS & Tool Automation (the big one)**

This is the category Claygent and scrapers literally cannot touch. These tools are behind logins, have complex UIs, and the workflows are repetitive clicking that eats hours of your week.

### **CRM Busywork (HubSpot, Salesforce)**

- Bulk update deal stages, contact properties, or lifecycle stages that don't have a clean CSV import path
- Navigate to each contact record → check activity → update lead score or status based on what you see
- Audit your HubSpot workflows or Salesforce flows — click through each one, document what they do, flag broken ones
- Create a batch of tasks or follow-ups across multiple records without doing it one by one

### **Cold Email Inbox Setup**

- Log into your email infrastructure tool (Google Workspace admin, Microsoft 365, Instantly, Smartlead) → create new sending accounts → configure DNS settings → verify domains. The setup flow is 15 clicks per inbox. Claude Code does it while you get coffee.

### **Onboarding Workflows**

- Navigate internal systems like Slack → fill out intake forms → upload documents → configure settings. Every new team member is the same 30-minute click sequence. Automate it.

### **Clay Itself (Untested)**

- Build or duplicate tables with specific column configurations
- Navigate between tables to copy enrichment setups
- Audit your Clay tables — visit each one, document what it does, flag stale data or broken enrichments

### **Data Entry Across Tools**

- Take a spreadsheet of data and enter it into a SaaS tool that doesn't have a bulk import. Claude Code navigates the UI and fills forms row by row.
- Migrate data between tools when there's no native integration — read from Tool A's UI, enter into Tool B's UI.

### **Internal Wiki & Intranet**

- Navigate your company's Notion, Confluence, or SharePoint → find and extract specific information buried 5 clicks deep
- Audit internal documentation — click through every page, flag outdated content, produce a cleanup list
- Onboard yourself to a new tool by having Claude Code explore the UI and explain what everything does

### **Reporting & Screenshots**

- Log into multiple dashboards (Google Analytics, HubSpot, Stripe, ad platforms) → screenshot key metrics → compile into a weekly report
- Navigate your ad accounts → pull performance data from the UI when the API export doesn't give you what you need

### **SaaS Admin & Cleanup**

- Audit user permissions across tools — log into each platform, check who has access, flag ex-employees who still have seats
- Navigate billing pages across your tool stack → compile a single view of what you're paying for everything
- Cancel or downgrade unused subscriptions by actually clicking through the cancellation flows

### **Apps that don't have APIs**

Claude Code can go and log into cloud-based SaaS, using your username and password, and can extract data and perform actions on your behalf. Example, Clay, Monday.com, or legacy SaaS software.

---

## **Life Stuff (Yes, It Works for Personal Tasks Too)**

The same "navigate a website and do tedious clicking" skill applies to all the boring life admin you procrastinate on.

### **Forms & Applications**

- Fill out government forms, permit applications, school enrollment paperwork — anything where you're re-entering the same name/address/SSN across 15 fields
- Complete insurance claims, reimbursement forms, HR onboarding paperwork
- Apply to multiple apartments, programs, or memberships where each has its own portal

### **Taxes & Financial Admin**

- Navigate your bank and credit card sites → download all your statements for the year
- Log into your tax prep tool → enter deductions and income sources from a spreadsheet you already have
- Audit your subscriptions — visit every service you pay for, screenshot the billing page, compile what you're actually spending

### **Shopping & Price Comparison**

- Visit 5 insurance providers → get quotes with the same parameters → compare in a single table
- Navigate multiple travel sites → find the same flight/hotel → compare total prices including fees
- Check product availability across multiple stores

### **Appointments & Bookings**

- Navigate a doctor's office portal → find the next available appointment → book it
- Check availability across multiple service providers (dentists, mechanics, tutors) without calling each one

### **Moving & Life Transitions**

- Set up utilities at a new address — navigate each provider's site, enter your info, select plans
- Update your address across every account you have (banks, subscriptions, government, etc.)
- Research and compare daycare, schools, or senior care facilities — navigate each site, pull pricing and availability

### **Returns & Customer Service**

- Navigate a retailer's return portal → initiate returns for multiple items → print labels
- File warranty claims by navigating the manufacturer's support site and filling out their forms

---

| ◀ Previous | 🏠 | Next ▶ |
|:--|:-:|--:|
| [Security & Privacy Primer](./21-security-and-privacy.md) | [All Lessons](./README.md) | [Systems Design GTM Agent](./23-systems-design-gtm-agent.md) |
