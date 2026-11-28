# The newsroom dashboard: result so far (28 Nov 2026)

Design: cl-6.designer@PrompTugal.dinis, at Dinis's request via cl-6.conductor. Advisers: cl-6.synthetic (scores), cl-6.sherpa, cl-6.customers, cl-6.decisions, cl-6.maestro, cl-6.security, cl-6.abp, cl-6.infra. Five loops, each with a note and a mock built from the real files: `loop1/` to `loop5/` (loop 5 has `admin/` and `public/`). `loop5/mock-build.py` builds both modes from cl-6.decisions' questions.json and cl-6.maestro's briefing.json and nothing else.

## What it is

- **Public mode** (/newsroom/status/, built by cl-6.dev now): what the newsroom is, the heartbeat (last article, articles live, build and checks), the items waiting on Dinis that cl-6.decisions flags public (title, a plain summary, what happens if he waits), counts and links to the existing agent and data pages. Never an answer line, key, id, money, private name or finding. 1.3 phone screens, 170 words.
- **Admin mode** (/admin/, waits for Dinis's yes): Decide now (full cards: plain title, why, if you wait, the grant text where there is one, the exact words with Copy, where to say them, a one-way-door mark and line where it applies), Decide this week (rows), Can wait (closed), what changed, Needs a look, Running fine, Answered with the answer given. 4.4 phone screens, 712 words.

## Scores (cl-6.synthetic, phone / desktop, 1 to 5: a top decision in 10 s; b clear unopened; c cost of waiting; d answer without hunting; e information versus decision; f next briefing; g nothing cut or hidden; h phone)

| | a | b | c | d | e | f | g | h | Phone screens | Words |
|---|---|---|---|---|---|---|---|---|---|---|
| Live page, 28 Nov | 2/2 | 2/2 | 1/1 | 2/2 | 1/1 | 1/1 | 1/1 | 2/3 | 18.4 | 1,902 |
| Loop 1 | 5/5 | 4/4 | 3/3 | 4/4 | 3/3 | 2/2 | 4/4 | 5/4 | 4.7 | 674 |
| Loop 2 | 5/5 | 4/4 | 4/4 | 4/4 | 3/3 | 2/2 | 4/4 | 5/4 | 3.1 | 423 |
| Loop 3 | 5/5 | 4/4 | 4/4 | 4/4 | 4/4 | 5/5 | 4/4 | 5/4 | 3.5 | 485 |
| Loop 4 | 5/5 | 4/4 | 4/4 | 3/3 | 4/4 | 5/5 | 4/4 | 5/4 | 3.7 | 540 |
| Loop 5 (f138f53) | 5/5 | 5/5 | 4/4 | 4/4 | 5/5 | 5/5 | 4/4 | 5/4 | 3.9 | 584 |
| **Loop 5, final (b812aa3)** | 5/5 | 5/5 | 4/4 | 4/4 | 5/5 | 5/5 | 4/4 | 5/4 | 4.4 | 685 |

Public page, read cold (loop 5): what it is 4, what is waiting 4, nothing that should not be public 4, phone 5. Their per-loop tables are in cl-6.synthetic's repository, status-dashboard-scores-loop*-2026-11-28.md. The page height and word count rose after loop 2 because it carries real content (heartbeat, briefing times, "what changed", grant text, one-way lines, checked times), not because the design grew. I have not scored my own work.

Final read (cl-6.synthetic, b812aa3): 685 words, 4.4 phone screens (6.1 at 320 px, 3.4 at 1280), no sideways scroll, Copy copies exactly the words. d is 4 only for the comment-box card's generic "where" (the data); g is 4 because rows need a tap and 16 are folded (a deliberate choice: Can wait is closed). The words and screens rose from loop 3 to 5 because the page carries real content (heartbeat, grant text, one-way marks, checked times), not because the design grew.

## What is left

- cl-6.dev: build public mode from questions.json at 0e31813 or later (snapshot drops non-public items, with a test; Copy copies only `answer_line`; the strikes line carries no date and no link until the page is live).
- Data (cl-6.decisions): `where` is still generic ("any session (conductor's or cl-6.decisions')") on most items; per-card `checked_at`, `unblocks`, `recommended` are in the file.
- Dinis: yes to /admin/ (the admin-build question) so admin mode can be built; signed answers are a later step with cl-6.security.

## Live public page scored by cl-6.synthetic (28 Nov, v0.1.2414)
Synthetic personas, not Dinis's view. Operator a to h: 3/3, 4/4, 4/4, 2/2, 3/3, 1/1, 3/3, 3/4. Cold reader: what it is 4, what is waiting 4, nothing that should not be public 3, phone 3. The live page is 8.8 phone screens and about 1,070 words, against the public mock's 1.3 screens and 170: it is still the old long page (tab row, agents by desk, other teams, the full dataset list, a Talk-to-us form) with the waiting list inserted 1.4 screens down. Gaps: the London strikes card names the unpublished address in full (sent to cl-6.security); no pointer to where the operator answers; no right rail at 1280 or 1440 px; two cut-offs and bare numbers in the Data cards. Table: PrompTugal__Agent__Synthetic, site/factory/dinis-cruz/account-f/status-live-scores-v0.1.2414-2026-11-28.md.
Design reading: the public mock is the target; the live page has not yet dropped the old sections.
