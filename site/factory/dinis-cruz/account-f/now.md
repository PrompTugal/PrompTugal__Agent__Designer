# cl-6.designer@PrompTugal.dinis: now

Updated 2026-11-26T02:36Z (date -u). Session https://claude.ai/code/session_016CrbJKnk1brEbFLeWGxmxT. Wake: 08:23 and 19:23 Lisbon.

Done today: key, full history (history/), area, area pass.

Stale since the role last ran (21 Nov), found on the website's dev at 02:35Z:
- ptmap is still 1.0.2 (design/shared-map/v1.0.2): 1.1 not built (SM6 crowded pins as one count pin, an Algarve inset, the 10m outline with the islands; spec board/spec-the-shared-map.md).
- Nothing else in design/ changed by others since 21 Nov except Vicky's publishing commits.
- Home-page feedback relayed by cl-6.maestro (material, unverified): a date on every article and headline; the Algarve town grid about twice the map's length with an empty column; the map should show which places have news; header buttons overflow at the top right; the "Design: The Front..." pill overlaps the town cards. To check at 375 and 1280 px and agree with cl-6.correspondent, who owns the front page. Any site change goes to cl-6.security first.

Blocked: my key entry in the website's board/keys.json (a one-way door; my commit was refused). Ready to ship: site/ready-to-ship/board-keys-entry.json.

Old asks from Dinis (unanswered since 21 Nov): the three specs waiting on dev builds (live data LD1-5, /values/, /media/); company spelling on investor pages; E's band green; where decision-page images live. They go to cl-6.conductor now.

## 2026-11-26T11:12Z wake pass
Reviewed the home page at v0.1.2306 (375, 768, 1280, 1440 px). Met: grid and map are both 792 px high at 1280 and 1440; every card and headline is dated; the header never passes the page width (the phone tabs scroll by design); Design is a 36 px icon. The legend shows 0 for 'this week' because the newest town story is 16 Nov: honest, not a bug. Suggested to cl-6.dev: the icon sits 12 px over the card edge at 1280 (content ends at 1240, icon starts at 1228); a fade on the phone tabs' right edge. Not asked for any more: pin size by count, sticky map.

## 2026-11-26T19:26Z evening wake
Checked the live build v0.1.2338. Live and right: the Design icon (x 1242 to 1274 at 1280), the phone tab fade, the Tube chart (api/v1/charts/tube-strikes-2026.svg, 200), the chip at 1280 and the /account/ top-up 'coming soon'. Faults sent to cl-6.dev: the chip has width 0 at 375 px (my spec keeps the figure on a phone); the ledger column still says 'Charged'; the ledger shows the old tagline 'Portugal town by town'. Next wake: re-check those three, then S4 (place pages) with cl-6.dev. Still open: Dinis's yes for my key entry and the ABP paths (P11, P5); /app/ (S3) with the conductor.
