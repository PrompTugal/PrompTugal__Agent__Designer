# The newsroom dashboard: design note, loop 4 (28 Nov 2026)

By cl-6.designer@PrompTugal.dinis. Builds on loop 3 (`../loop3/note.md`, with its addendum). This loop reads cl-6.decisions' questions.json at a7fb864 (updated 28 Nov 02:24 UTC, 34 questions) and cl-6.maestro's briefing.json (`brief`, `changes[]`), through `mock-build.py` in this folder, which builds `mock.html` from those two files and nothing else (so the build for the real page can start from it). Screenshots: `mock-320-top.png`, `mock-375-top.png`, `mock-1280-top.png`.

## What changed since loop 3

- **New fields from decisions, all used:** `checked_at` ("Facts checked 28 Nov 02:24 UTC" on every card and row), `unblocks`, `recommended {answer, by}`, `where_url` (the "Where" label is a link when there is one), `options` (the alternatives, each its own line with its own Copy), and the short agent name before the first semicolon of `where`.
- **Recommended** is shown only where the file carries it, as a small line inside the answer box under the matching answer ("Recommended by cl-6.maestro"). Where `recommended` is null (Dinis's own calls, by decisions' rule) nothing is shown: the card never steers him.
- **Unblocks** moves under Details. On two of the three Now cards it repeated "If you wait" or "Why" ("The strikes page is ready and waits only on this" / "The page stays unpublished" / "The London strikes page goes live"); three lines of near-identical meaning is the thing the redesign removes. If a question's `unblocks` says something the other two do not, decisions can say so and I will show it on the face.
- **Numbering:** the soon and can-wait rows are numbered in the file's order, so "where am I in the list" is visible. Ranking is decisions' to set (asked in the addendum).
- Counts now: 3 now, 14 this week, 16 can wait, 1 answered (34 questions).

## Measures (same method: browser, 375 px, 812 px per screen, words in the page)

| | Live page | Loop 1 | Loop 2 | Loop 3 | Loop 4 |
|---|---|---|---|---|---|
| Phone screens | 18.4 | 4.7 | 3.1 | 3.5 | 3.7 |
| Words | 1,902 | 674 | 423 | 485 | 540 |

320 px: 4.2 screens, no sideways scroll. The page grew slightly across loops 2 to 4 because it now carries real content (the heartbeat, the briefing times, five "what changed" lines, the checked time on every card, and the recommended marks), not because the design grew.

## Scores

cl-6.synthetic's scores are in loop 3's addendum (baseline, loop 1, loop 2). Loops 3 and 4 are to be scored by them; I have not scored my own work.

## Still open

The "public" consequence (every question is `public: false`, so a public page honouring it shows no decisions until /admin/ exists) is in loop 3's addendum, with my recommendation, for the conductor, decisions, security and Dinis. Answered items show a title, not the answer (asked for `answer_given`). Ranking of the 14 "this week" rows is decisions' to set.
