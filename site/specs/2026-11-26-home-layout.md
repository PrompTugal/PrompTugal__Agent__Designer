# Home page layout spec (26 Nov 2026), from cl-6.designer@PrompTugal.dinis

Measured on the built site, v0.1.2294, at 375, 1024 and 1280 px (Chromium). For cl-6.dev (layout code: `front-e.mjs`, `home.mjs`, `design-kit.mjs`) and cl-6.correspondent (data in `front-page.json`). Reaches the site only through cl-6.security.

## What I measured

1. **Town grid against the map (1280 px).** The map column is about 800 px high; the town grid beside it is 1263 px (three columns, six rows of long cards), so the grid is about 1.6 times the map and the column under the map is empty. Each card is a name, a counts line, a 3 to 6 line blurb and a headline.
2. **Map.** Every pin is the same dark green dot; nothing shows which town has news.
3. **"Design: The Front Page" button.** It is a fixed `button.ptd-btn`, 199 x 38 px, at the bottom right of the viewport at every width (x 553 to 752 at 768 px; x 1065 to 1264 at 1280 px). It floats over whatever is under it: at 1280 px it sits on the Quarteira card.
4. **Header.** I could not reproduce buttons overflowing the page: the page is never wider than the viewport from 320 to 1280 px. What I did see: at 414 px and below the section tabs scroll sideways inside the masthead (the last tabs are cut off, with no hint that it scrolls), and at 375 px and below the Portugal tab is cut. Dinis's window may be a width or a browser I did not try.
5. **Dates.** The town cards carry no date on their headlines. cl-6.correspondent has put `date` on the lead, top and briefing items already.

## Changes I recommend

- **Town grid:** four columns from 1100 px wide (three at 768 to 1099, two on a phone). Cut each card to the name, the counts line, one headline with its date, and the blurb clamped to two lines. Target: grid height no more than the map's (about 800 px at 1280 px). Make the map column `position: sticky` so it stays beside the grid while a reader scrolls.
- **Map pins:** a town with news gets a filled pin sized by story count, with its count; a town with none gets a small hollow pin. Needs, per town in `front-page.json`: `stories` (count), `latest_date`, `latest_headline`. The "has news" count is `stories > 0`.
- **Design button:** take it out of fixed position. Put it in the masthead's utility row beside Search and Ask on desktop, and hide it below 768 px. It must never sit over content.
- **Header tabs on a phone:** keep the sideways scroll, add a fade on the right edge so a reader sees there is more, and scroll the current tab into view.
- **Dates:** every headline on the page shows its date in the same small mono style (`26 Nov`), on the cards and the lists.

## Check after the change

Sweep at 320, 375, 768, 1024, 1280 and 1440 px: no page-level horizontal scroll; the grid no taller than the map at 1280 and 1440; nothing under the Design button; every headline dated; the gate prints OK.
