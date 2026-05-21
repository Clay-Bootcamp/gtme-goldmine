# 01 — landing page / portfolio site

apple notes–themed personal site for [tanay mishra](https://www.linkedin.com/in/tanay-mishra-ai-automation/). plain html + css + js. no build step, no install.

## run locally

double-click `index.html` — opens in your default browser. done.

(or from the terminal: `open index.html`)

## files

- `index.html` — markup + every note's content lives inline
- `styles.css` — dark-mode notes-app styling
- `app.js` — click handler that swaps the visible note

## edit your notes

all note copy is inside `index.html`. each note is two pieces that share a `data-note` id:

1. a `<button class="note-item">` in the sidebar
2. an `<article class="note-content" data-note="X">` in the main pane

to add a new note: copy an existing sidebar `<button>` and content `<article>`, pick a new `data-note` value, change the title, icon, and body.

## deploy later

when you like what you see locally, drop the folder onto [vercel.com](https://vercel.com) (drag and drop) or run `vercel` inside this directory.

## known limits (v1)

- search bar is visual only — not wired up yet
- light mode toggle not implemented
- desktop-first; mobile layout collapses sidebar above content
