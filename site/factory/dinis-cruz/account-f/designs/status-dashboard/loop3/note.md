# The newsroom dashboard: design note, loop 3 (28 Nov 2026)

By cl-6.designer@PrompTugal.dinis. Loops 1 and 2 are in `../loop1/` and `../loop2/`. This loop answers the conductor's five fixes and the second round of advice (cl-6.synthetic's scores of loop 1, cl-6.customers, cl-6.sherpa, cl-6.maestro, cl-6.decisions), all received 28 Nov 02:20 to 02:22 UTC. The mock now reads the **real** files: cl-6.decisions' questions.json at e008059 (updated 28 Nov 02:21 UTC) and cl-6.maestro's briefing.json at 1d71b60 (updated 28 Nov 02:20 UTC). No text on the page is mine except labels. Files: `mock.html`, `mock-320-top.png`, `mock-375-top.png`, `mock-1280-top.png`.

## Scores and measures

cl-6.synthetic's scores (phone / desktop, 1 to 5), a to h as in the loop 1 note:

| | a top decision in 10 s | b clear unopened | c cost of waiting | d answer without hunting | e info vs decision | f next briefing | g nothing cut or hidden | h phone |
|---|---|---|---|---|---|---|---|---|
| Live page (baseline) | 2 / 2 | 2 / 2 | 1 / 1 | 2 / 2 | 1 / 1 | 1 / 1 | 1 / 1 | 2 / 3 |
| Loop 1 mock | 5 / 5 | 4 / 4 | 3 / 3 | 4 / 4 | 3 / 3 | 3 / 3 | 4 / 4 | 5 / 4 |
| Loop 3 mock | to score | | | | | | | |

My measures, same method each time (browser, 375 px, 812 px per screen, words in the page): live page 18.4 screens and 1,902 words; loop 1 4.7 and 674; loop 2 3.1 and 423; **loop 3 3.5 and 485** (more than loop 2 because it now carries the heartbeat, the briefing times, "what changed" with five real lines and the running-fine flags). 320 px: no sideways scroll.

## What changed, point by point

| From | Said | Change in loop 3 |
|---|---|---|
| conductor 1, maestro 4, customers 3, sherpa, synthetic | The answer box held internals (session ids, "P11 h", paths, "add_repo") | The box holds only the words (decisions' `answer_line`); where to say it is a plain label under it, from `where`; scope notes, hashes, ids, security requirements and the full question live under Details |
| synthetic, sherpa | Two answers behind one Copy | Alternatives (the " \| " in `answer_line`) are separate lines, each with its own Copy, under "Say one of these" |
| decisions | Approvals with no words are actions, information is passed on | A line starting "(" or a "For information" item shows "Do this yourself" or "Pass this on" in a dashed box, no Copy |
| decisions, customers 5 | Tag each item | Every card and row carries Decision, Approval or For information, and "since <date>" |
| conductor 3, synthetic | "If you wait" must say what it costs | Taken from decisions' `if_you_wait`, which they have rewritten; the card shows it as it is |
| conductor 2 | Card facts go stale | The page shows "decisions checked 28 Nov 02:21 UTC" from the file; the card text is the file's, not mine. Per-card check times need a `checked_at` field from decisions (asked) |
| conductor 4, maestro 1 | "(example)" for the next briefing | Real: last briefed 28 Nov 01:47 UTC, next briefing 28 Nov 08:30 UTC (08:30 Lisbon), from `brief` in briefing.json |
| maestro, loop 1 | "What changed" was an example | Real: the five newest lines of `changes[]` in briefing.json, with date, hour and kind |
| customers 1 | Heartbeat line first | "Last article published 26 Nov · 117 articles live · build v0.1.2412, checks passed at the build": read from the articles list and the build, not typed |
| customers 4 | "Running fine" must not hold blockers or problems | Counts only (43 agents, 26 idle, 17 blocked; 30 datasets, 23 fresh, 1 archive) with links; the 6 data sources with a problem are a separate "Needs a look" flag |
| sherpa | Counts look like buttons; 5+14+9 is not 29 | Counts are a plain line: "3 need you now · 11 this week · 14 can wait · 1 answered" (29) |
| sherpa | After answering elsewhere the card stays | "Answered somewhere else? This page catches up at its next build." |
| sherpa, decisions | Age of each ask on the face | "since 27 Nov" on every card and row, absolute dates |
| conductor 5, customers 6, sherpa 6 | Public versus private | See below |
| customers 6 | Remove the mock banner | Gone: the page carries no design wording; the mock is labelled in this note and the file names |
| customers 2, maestro 2 | A recommended default per card | Not in the data yet; asked (below). The card has no space reserved for it until the field exists |

## Public and private (my proposal; for the conductor, Dinis, cl-6.security and cl-6.decisions to settle)

cl-6.customers and cl-6.sherpa agree: a public page should show what a cold reader and the public can use, and the decision cards belong behind sign-in. My recommendation, as in loop 2, is one design in two modes.
- **Public /newsroom/status/ (and the reader-facing newsroom):** the heartbeat line, the counts, every agent with its role and state, data freshness with sources and dates, and corrections. No decision cards, no answer lines, no "waits on Dinis", no money, keys, vault ids, lanes or private conversations.
- **Behind sign-in, /admin/ (Dinis's dashboard):** this page in full: decide now, this week, can wait, what changed, running fine, with signed answers later.
- **Until /admin/ exists** (it needs Dinis's yes on the admin-build question and cl-6.security's conditions): the cards currently on the public page are already public, so the interim is the status quo minus anything cl-6.decisions does not flag `public: true`. The default is not public. This interim, and who flags each question, are for the conductor, cl-6.decisions and cl-6.security.

## Data asks (to the owners; not decided)

- **cl-6.decisions:** per question `checked_at` (when its facts were last confirmed), `public` (true or false, default false), `recommended` (the answer you recommend, if any, and who recommends it: the page says "Recommended: yes, by cl-6.maestro") and `unblocks` (one line on what the answer unblocks). Their current fields (title, why, if_you_wait, tier, kind, answer_line, where) are enough for everything above.
- **cl-6.maestro:** nothing more; the feed already carries `brief` and `changes[]`. Decisions in briefing.json (`decision`, `options`, `category`) are not read by this page.
- **The build (cl-6.dev):** reads the two files above, the articles list for the newest article date and count, the agents file and the data-status file for the counts and flags; and prints its own built-at time.

## Still open

- Not yet scored by synthetic (loop 3). Sherpa's note says five full "now" cards at once is too much; there are three today, and decisions says more than five means their triage needs fixing, not the page.
- The Copy button needs a small script; the line is selectable text without it.
- Desktop right rail (counts and next briefing) is described, not yet drawn in the 1280 px shot, which is one column.
- Signed Answer button for /admin/ is later work, after Dinis's yes.

## Addendum, 28 Nov 02:30 UTC: questions.json at 74d57b3, and cl-6.synthetic's loop 2 scores

**cl-6.decisions' newer file (74d57b3, updated 28 Nov 02:22 UTC)** adds `where_url` (the link behind the "Where" label), `options` (the " | " alternatives as a list, so each is its own line with its own Copy: same result as the mock), `deadline` (null everywhere) and `public` (false on every item until /admin/ exists; the rule is in card_schema). `recommended` is false throughout: the calls are Dinis's, and decisions does not steer them, so the page shows no "Recommended" mark.

**cl-6.synthetic's loop 2 scores** (baseline / loop 1 / loop 2, phone and desktop equal): top decision in 10 s 2 / 5 / 5; items without ids 2 / 2 / 3; copy the full line 2 / 4 / 4; know when next briefed 1 / 2 / 2 (loop 1 revised from 3, because its time was an example); nothing cut or hidden 1 / 4 / 4; consequence of waiting 1 / 3 / 4; information versus decision 1 / 3 / 3. Their open points on loop 2, and where loop 3 stands: (1) session ids, "P11 h" and a fallback in the answer box: fixed in loop 3 (words only; "Where" is a label); (2) two answers behind one Copy: fixed; no recommended one, by decisions' rule; (3) the 11 "soon" rows cannot be ranked and some are topics, not asks: not fixed; I have asked decisions to order the file by what blocks most and word each title as an ask; (4) "17 agents blocked" beside "3 need you now" alarms without guiding: moved to "Running fine" as counts; (5) the notice said keys are not shown while two rows are about keys: the notice is gone; whether a key item is shown at all is the `public` flag; (6) Answered shows a title, not the answer: not fixed; asked decisions for `answer_given`.

**A consequence to settle (conductor, cl-6.decisions, cl-6.security, Dinis):** with `public: false` on every question, a public /newsroom/status/ that honours the flag shows **no decisions at all** until /admin/ exists, so Dinis loses his decisions list on that page before he has the admin that replaces it. Options: (a) honour the flag now, and Dinis reads decisions in the maestro's briefing until /admin/ is built; (b) decisions flags `public: true` on the items that are safe to show (today the three "now" items, which are already public: the comment box, the journalist session, the London strikes session) with security's agreement, so the top of the page stays for Dinis now, and the rest wait for /admin/. I recommend (b), as the smallest change that keeps the dashboard useful, and building /admin/ next (it waits on the admin-build question).
