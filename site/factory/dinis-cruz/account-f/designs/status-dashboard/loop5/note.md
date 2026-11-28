# The newsroom dashboard: loop 5 (28 Nov 2026), public mode and the confirmation of cl-6.security's ruling

By cl-6.designer@PrompTugal.dinis. Builds on loops 1 to 4. Inputs: cl-6.security's ruling on loop 3 (28 Nov 02:30 Z: acceptable, four conditions, relayed by the conductor), cl-6.decisions' questions.json at a6dad97 (public:true on three items; `public_summary`, `rank`, `answer_given`, `answered_at`), cl-6.maestro's briefing.json. `mock-build.py` builds both modes from those two files: `public/mock.html` (this page, as dev builds it now) and `admin/mock.html` (behind sign-in; waits for Dinis's yes to /admin/). Screenshots in each folder.

## Confirmation of the four conditions (as design rules)

1. **Default deny at sync.** `public` is false unless cl-6.decisions sets it true. The build step that writes `assets/newsroom/status-snapshot.json` (the site's repository is public, so everything in the snapshot is published) drops every non-public question before writing. There is a test: a `public:false` item never reaches the snapshot, and a card built for the public page cannot be given a field the contract below does not list.
2. **Behind sign-in is decluttering, not secrecy.** A static /admin/ cannot hide what it ships. Admin mode reads questions.json at run time from its public source (later from something sealed to Dinis's key), never from data built into the site.
3. **Only cl-6.decisions sets public:true**, item by item, in its own signed commit; public items still go through the clean-up step.
4. **The public page never carries:** keys, tokens, sealed values, vault names or ids, access state; session or scheduled-task ids, claude.ai links; private people's names or contacts; money; the answer or authorisation lines and the options to paste (the question, not the words that grant it); open security findings; internal hosts, network settings, gate or ruleset gaps.

## The public page: the contract for the build

Public mode shows, in this order: "The newsroom today" (one plain sentence: how the newsroom is doing, in public, run by AI agents, operated by Dinis Cruz); the heartbeat line (last article published, number of articles live, build version, checks passed at the build); the built time; **Waiting on Dinis**, one card per item with `public:true`: the status tag, the `title`, the `public_summary` and `if_you_wait` (cl-6.security's 02:34 Z note, relayed by cl-6.decisions, allows title, public_summary, why, if_you_wait, unblocks and the agent name in `where`; the design uses three of them, because `why` and `unblocks` repeat the summary), and nothing else: no Copy box, no answer line, no options, no `where_url`, no id, no checked time, no since date, no session or task id; **Agents** (the count and a link to the existing every-agent page, which carries roles and states); **Data** (counts and a link to the existing dataset page, which carries each source and date). It does not show: the three counts of now, this week and can wait (they would reveal how many non-public items exist), the briefing times, the "what changed" lines (maestro's feed is not flagged public), or any non-public question.
Measures (375 px, 812 px per screen): public page 1.5 screens, 190 words; admin mode 4.0 screens, 588 words (it now carries real answered text and ranks). 320 px: no sideways scroll in either.

Checked by grep on the built public page: no session id, no claude.ai link, no Copy box, no "answer" (0 matches).

## Admin mode (later, after Dinis's yes)

Unchanged from loop 4, with two changes from the newer file: rows follow `rank` (lower blocks more; the file is sorted by tier then rank), and an Answered item shows the answer given ("content-owner": Dinis's own words of 27 Nov 10:33 UTC). Until /admin/ exists, the full list stays on Dinis's briefing page, as decisions says.

## Scores

cl-6.synthetic's scores (baseline, loop 1, loop 2) are in loop 3's addendum; loops 3 to 5 are for them to score (loop 5 admin mode is the loop 4 design plus ranking and answers). I have not scored my own work.

## For cl-6.dev (build now) and what waits

Build now: public mode as above, with the snapshot drop and its test. Waits for Dinis's yes: /admin/ mode, the Answer button and signing.

## Update, 28 Nov 02:30 UTC (questions.json at 06ea0a6)

cl-6.decisions confirmed the public-card rule above (card_schema.public_rule) and that all three of my asks are in the file (ask-wording and rank, `answer_given`, `public:true` on the three Now items). The mock was rebuilt from 06ea0a6. The page must honour `public` only once cl-6.dev's sync filters non-public items out, with its test.

## Update, 28 Nov 02:40 UTC: cl-6.synthetic's loop 3 scores, and admin mode revised (questions.json at 254c240)

cl-6.synthetic's scores, phone / desktop, 1 to 5 (a top decision in 10 s; b clear unopened; c cost of waiting; d answer without hunting; e information versus decision; f next briefing; g nothing cut or hidden; h phone). Loop 1's f was revised by them from 3 to 2, because its time was an example.

| | a | b | c | d | e | f | g | h |
|---|---|---|---|---|---|---|---|---|
| Live page | 2 / 2 | 2 / 2 | 1 / 1 | 2 / 2 | 1 / 1 | 1 / 1 | 1 / 1 | 2 / 3 |
| Loop 1 | 5 / 5 | 4 / 4 | 3 / 3 | 4 / 4 | 3 / 3 | 2 / 2 | 4 / 4 | 5 / 4 |
| Loop 2 | 5 / 5 | 4 / 4 | 4 / 4 | 4 / 4 | 3 / 3 | 2 / 2 | 4 / 4 | 5 / 4 |
| Loop 3 | 5 / 5 | 4 / 4 | 4 / 4 | 4 / 4 | 4 / 4 | 5 / 5 | 4 / 4 | 5 / 4 |

Their table: https://github.com/PrompTugal/PrompTugal__Agent__Synthetic/blob/dev/site/factory/dinis-cruz/account-f/status-dashboard-scores-loop3-2026-11-28.md . Loops 4 and 5 are not yet scored.

Changes made in admin mode after their loop 3 read and the conductor's two points:
- **Blocked has its own line.** "Running fine" no longer holds the 17 blocked agents or the 6 data sources with a problem: a boxed "Needs a look" group above it carries "17 agents are blocked" and "6 data sources have a problem", each with a link to see which. "Running fine" is only what is fine (26 agents idle, 23 datasets fresh, 1 archive).
- **No Copy on a template.** An answer with a fill-in (for example "/app/ is now: <one sentence>") shows "Write your own" in a dashed box and no Copy button.
- **Public mode** is rebuilt from 254c240; the three summaries no longer end "Waiting on Dinis" (the tag says it); 1.4 phone screens, 179 words; admin mode 4.0 screens, 599 words.

Open, and not mine to change in the design (the data): (1) the "this week" answer lines are long paragraphs (cl-6.decisions is shortening them: a short `answer_line` plus a scope line under Details); (2) `where` says "any session (conductor's or cl-6.decisions')" on most items: it should name the one agent the answer goes to; (3) no recommended answer on Dinis's own calls, by decisions' rule.

## Update, 28 Nov 02:50 UTC: grant text beside the short line (cl-6.abp's condition; questions.json at a29c0fc)

cl-6.decisions shortened six grants to a short `answer_line` by reference ("yes to talk-drain as written in decisions questions.json at <full commit hash>") and, on cl-6.abp's condition (card_schema.grant_rule), added `grant_text` and `grant_commit`. A short line binds to the grant text at that commit, so **admin mode shows `grant_text` in full on the card, beside the short line**: a heavy-bordered "What you are approving" block above the "Say" box. It is on the face, not under Details, because it is what Dinis approves. The full commit hash stays in the line itself (it is part of the words he says) and under Details; the page never shows a different text than the file's. Screenshot: `admin/grant-row-375.png` (the talk-drain row). The public page never carries grant text. A change to `grant_text` needs a new yes at a new commit, so the card shows what the commit says, never an edited summary. The page height is unchanged for rows that are closed; an open grant row is about one screen at 375 px.

## Update, 28 Nov 03:00 UTC: cl-6.synthetic's loop 4 scores, a regression fixed, one-way doors marked

Loop 4 scored by cl-6.synthetic (phone / desktop): a 5/5, b 4/4, c 4/4, **d 3/3 (was 4: a regression)**, e 4/4, f 5/5, g 4/4, h 5/4. Table: https://github.com/PrompTugal/PrompTugal__Agent__Synthetic/blob/dev/site/factory/dinis-cruz/account-f/status-dashboard-scores-loop4-2026-11-28.md .

- **Regression fixed.** In loop 4 the "Recommended by cl-6.maestro" mark was inside the element the Copy button copies, so the button copied "yes, start the strikes session Recommended by cl-6.maestro". The mark now sits below the answer line, outside it; checked in a browser that each Copy button copies exactly the words and nothing else (the first six buttons were read back).
- **"Facts checked" on every card with the same time** read as the file's time, not a per-question check. The time now shows on a card only when it differs from the file's own date; the page-level stamp says when decisions checked. Per-question checks will show up when they differ.
- **One-way doors (cl-6.abp, 02:29 UTC).** A card for a one-way door carries a visible mark in its header ("One-way door") and a plain line on its face: "One-way door. Only your own words in cl-6.abp's session count: type or paste the line there. An answer button on this page does not count." A Copy button is fine (pasting the line into that session himself arrives as his message); a button that records the answer for him, or a relay by another agent, does not count until the signed-admin-answer design is adopted and security passes it, after which the card can say a signed answer also counts. This needs a flag in the data (`one_way: true`), asked of cl-6.decisions; the mock marks s17 as the example.
- The loop 5 mocks are rebuilt: admin mode 3.9 phone screens and 584 words; the public page is unchanged.

Not yet scored: loop 5. Still open and the data's: five answer lines are templates with a blank (they now show "Write your own", no Copy); longest "this week" answer 55 words (grants now by reference, with the grant text shown beside).

## Update, 28 Nov 03:10 UTC: cl-6.synthetic's loop 5 scores

Admin mode, phone / desktop: a 5/5, b 5/5, c 4/4, d 3/3, e 5/5, f 5/5, g 4/4, h 5/4 (loop 4: 5, 4, 4, 3, 4, 5, 4, 5/4; baseline 2, 2, 1, 2, 1, 1, 1, 2/3). Public page read cold: says what the newsroom is 4, what is waiting 4, nothing that should not be public 4, phone 5. Table: https://github.com/PrompTugal/PrompTugal__Agent__Synthetic/blob/dev/site/factory/dinis-cruz/account-f/status-dashboard-scores-loop5-2026-11-28.md . Their d of 3 is the Copy bug, which they read in the mock built before the fix in the previous update; the fixed mock copies only the words (read back in a browser). The conductor asked for the fix to be in dev's build contract: **Copy copies only the card's `answer_line` (or an alternative from `options`), taken from the data, never from the page text around it**; a test reads each Copy button's value and checks it equals the question's `answer_line` or one of its `options`.
Public page: "Waiting on Dinis" now appears once (the heading), not on every card (it was four times). Notes left for others: "session" and "journalist" are unexplained to a cold reader (wording for cl-6.decisions' public_summary); the public cards carry no "since" because it is not on the allowed list; card 3 names a page that is not yet published ("the London strikes page is ready"): for cl-6.security.

## Update, 28 Nov 03:15 UTC: cl-6.security's two conditions on the public strikes line

cl-6.security (02:42 UTC, relayed by the conductor): naming `strikes.london.place.agent.promptugal.news` on the public line is acceptable, on two conditions: (1) say plainly that the page is **not published yet**, with **no date** unless one is decided; (2) **no link until the page is live.** Design rule and build contract: a public card whose subject is an unpublished page says so in its `public_summary` ("not published yet"), carries no date and no link; the page links it only when the page is live (the build checks that the target exists in the built site before it renders a link). Wording is cl-6.decisions' (public_summary).

## Update, 28 Nov 03:25 UTC: one-way doors from the data (questions.json at 72f1492)

cl-6.decisions set `one_way` on 13 items, each with a `one_way_reason`, and made `checked_at` real per item (date only where no time is known). card_schema.one_way_rule says which session counts for each kind: cl-6.abp's for keys, rules and merges; cl-6.maestro's for session starts and resets; for legal and money calls, any session where decisions can verify his words. A pasted line counts; words relayed by an agent do not, until signed admin answers are adopted.

The card now builds its line from the data: a header mark ("One-way door"), and a boxed line "One-way door: <reason>. Only your own words, typed by you in <the session in where>, count. A line you paste yourself counts; words relayed by an agent, or an answer button on this page, do not." "Facts checked" shows on every card again, now with the item's own time (or date). Admin mode: 4.4 phone screens, 712 words (the three Now cards are longer by the one-way line and the checked time); public page 1.3 screens, 170 words. The one-way line is the only new text: it replaces nothing and is worth the length because the route is the point of the card.
