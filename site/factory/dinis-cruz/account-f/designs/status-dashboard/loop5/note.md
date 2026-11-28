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
