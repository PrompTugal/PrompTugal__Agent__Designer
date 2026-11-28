# The newsroom dashboard: design note, loop 2 (28 Nov 2026)

By cl-6.designer@PrompTugal.dinis. Loop 1 is in `../loop1/note.md`. This loop folds in the advice of cl-6.synthetic (baseline scores), cl-6.sherpa, cl-6.customers, cl-6.maestro and cl-6.decisions (via cl-6.conductor), all received 28 Nov 02:18 to 02:19 UTC, and rebuilds the mock from the real questions file as cl-6.decisions now writes it (questions.json at 6671016, updated 28 Nov 02:19 UTC, with `title`, `why`, `cost_of_waiting`, `level` and `answer_line` on every question). Files: `mock.html`, `mock-320-top.png`, `mock-375-top.png`, `mock-1280-top.png`.

## Scores and measures

| | Live page (baseline) | Loop 1 mock | Loop 2 mock |
|---|---|---|---|
| Phone screens (375 px) | 18.4 (synthetic: 17.1) | 4.7 | 3.1 |
| Words on the page | 1,902 | 674 | 423 |
| First decision starts at | about 1.2 screens down | first screen | first screen |
| Synthetic, top decision in 10 s | 2 of 5 | to score | to score |
| Synthetic, items without internal ids | 2 of 5 | to score | to score |
| Synthetic, copy the full answer line | 2 of 5 | to score | to score |
| Synthetic, know when next briefed | 1 of 5 | to score | to score |

The synthetic scores for loops 1 and 2 are for cl-6.synthetic to fill in; I have not scored my own work. Measures are mine, same method each time (browser, 375 px, 812 px per screen, words in the page body).

## What each adviser said, and what I changed

| Advice | Change in loop 2 |
|---|---|
| sherpa 1, 2: first screen is one sentence of state, then counts | A state line at the top: "3 need you now · 11 soon · 14 can wait · 17 agents blocked · 6 data sources with a problem" (the agent and data counts are from the live page of 28 Nov); the built and read stamp under it |
| maestro 1: three bands, decide / know / later, at most five cards shown | Decide now (3 cards, at most 5), Decide soon (rows), Can wait (closed), then What changed (at most five lines) and Running fine |
| decisions: face is title, why, cost of waiting, level; answer_line full, in a copyable box; details behind a fold; answered items collapsed; "now" at the top | Done as specified; the card shows exactly those five fields; Details holds the full question, asked by, since, id; Answered is a short list of titles |
| sherpa 3, 4, 5: remove the intro paragraph, the 40-row agent table, "Known blockers", hashes and grant codes, "20 more" | All gone from the page; every item is on it (no "more" hidden); agents and data are two counts with links to their own pages |
| maestro 3: no per-agent tables, context %, cost per agent, cron times or dataset row counts; agents appear only when blocked on him, inside a decision | The agent and dataset pages stay linked, not repeated; a blocked agent is a decision card or nothing |
| sherpa 7: one urgency scale, sorted | The three levels now, soon, when-you-can, each with a word and a shape (● ◐ ○), oldest first within a level |
| customers 1, 3: a cold reader first; state in words; "unknown" or "stale since", never hidden gaps | "last briefed: not reported yet", "next briefing: not reported yet" are shown as such; no figure is guessed |
| sherpa 6, customers 5, 6: a public page must not look like it takes answers or show keys, money or private people | See "Public and private" below; the mock carries a one-line notice |
| sherpa 8: phone, test at 320 px | Measured at 320, 375 and 1280 px: no sideways scroll |

## Public and private (a decision for the conductor and Dinis, with cl-6.security and cl-6.decisions)

/newsroom/ is public; /admin/ is private and needs Dinis's yes and cl-6.security's conditions. cl-6.customers and cl-6.sherpa both say the decision cards (asks, blockers, "the line that answers it") belong behind sign-in, and that a public page should instead show the newsroom's state for a cold reader: last updated and checked, how many articles and places are live, whether the build and checks pass, agents with their roles, data freshness, each figure with its source and date.

My recommendation: **one design, two modes.** The same cards and bands, built from the same files. In **admin mode** (behind sign-in) it is this page: decisions, what changed, running fine. In **public mode** it shows only the state band, agents and roles, and data freshness, plus decisions that cl-6.decisions flags `public: true` (the default is false, so a question about keys, money, a private person, or an unreleased decision "For Dinis" is never public). Until /admin/ exists, the page keeps showing decisions as it does today (they are already public), minus anything not flagged public; that interim, and who flags, is for the conductor, cl-6.decisions and cl-6.security to settle.

## Data this needs (aligned between the two feeds)

- **questions.json (cl-6.decisions)** is the single source for decisions, with the fields it already has. Two more, please: `where` (where to say it, for example "in cl-6.maestro's session", with the session link in `where_url`, so `answer_line` is only the words and no session id appears on the card face); and `public` (true or false, default false). Optional: `deadline` and `options` (each with a label and a recommended flag), as cl-6.maestro proposes.
- **briefing.json (cl-6.maestro)** should not repeat decisions. It carries `know[]` (at most five plain lines, each with a date and hour, newest first), `last_briefed` and `next_brief`. cl-6.maestro proposed `decision`, `why`, `deadline`, `options`, `answer_line`, `category`, `since`, `details_url` on briefing items; if the decisions live in questions.json the two feeds should use the same names (`title`, `why`, `cost_of_waiting`, `level`, `answer_line`), and the briefing's decide items should be dropped in favour of questions.json.
- **Briefing cadence (cl-6.maestro)**: a morning brief around 08:30 Lisbon, an evening wrap around 18:30, and an immediate ping only for a deadline under 24 hours. The page shows "last briefed" and "next briefing" from the feed.

## Still open in the design

- "What changed since you last looked" is an example until the feed exists.
- Counts for agents and data are from the live page, not a feed; the build will read them from agents.json and the data-status file.
- Signed answer button for /admin/ (later); the Copy button needs a small script, and the line is selectable text without it.
- I have not scored the mock myself.
