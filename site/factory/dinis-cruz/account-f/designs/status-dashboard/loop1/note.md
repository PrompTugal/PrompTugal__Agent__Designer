# The newsroom dashboard: design note, loop 1 (28 Nov 2026)

By cl-6.designer@PrompTugal.dinis, at Dinis's request via cl-6.conductor (his words: "this material is not readable and easy to consume ... a massive wall of text ... it should be very clear what decisions I need to make and what I need to know and when I need to be briefed. So think of this again as the dashboard of the newsroom."). Mock: `mock.html` (screenshots `mock-375-top.png`, `mock-1280-top.png`), built from the live questions file (cl-6.decisions, updated 27 Nov 10:36 UTC, 29 questions). Design for /newsroom/status/ now; the same design becomes /admin/ when Dinis says yes to it.

## Baseline: the live page, 28 Nov (v0.1.2412)

Measured with a browser at 375 and 1280 px:
- 18.4 phone screens (11.2 at 1280 px); 1,902 words in the main column.
- On a phone the first decision starts about one screen down (after the header); the open questions start 3.5 screens in; "Every agent" starts 7 screens in.
- A decision is one bold paragraph that mixes what, route, record ids and paths ("questions.json a7914b5", "P11 h"), followed by two bullets, "Urgency: ..." and "The line that answers it: ...", the latter cut off with "..." in places. There is no ranking, no grouping, no difference between a decision and a piece of information, and some items are hidden ("20 more").
- 29 questions in the file, average 208 characters; several are titles only an insider reads ("Sign-in fix S17", "Delete SIG_BOOTSTRAP_ANCHOR on News__Data", "Merge IaC #34, #35, #36, #37").
- Agents: 43 (17 blocked, 26 idle). Data: 30 datasets (23 fresh, 6 with a source problem, 1 archive).

## What the page must answer, in this order (Dinis's three questions)

1. **What do I need to decide?** Ranked, each with a plain title, one line on why it matters, what happens if he waits, and the answer line to give.
2. **What do I need to know?** What changed since he last looked, one line each, newest first.
3. **When am I next briefed, and what is running fine?** The next briefing's time; everything healthy collapsed to two counts and links.

## The decision card

Anatomy (top to bottom): urgency mark and rank ("● Now · 1 of 5") · a plain title that is a task or a question, under 80 characters, no ids · **Why it matters** (one or two sentences) · **If you wait** (one sentence) · **Your answer**: a box holding the exact words and, above them, where to say them, with a Copy button (later a signed Answer button in /admin/) · a closed **Details** fold: who asked, since when, the id, the full original question, links.

Rules: the answer line is never cut; internal ids, commits, session ids and paths live only in Details; one card is one decision (the seven-question provenance item becomes seven short cards or one card with a short numbered list); urgency is a word and a shape ("● Now", "◐ This week", "○ Can wait"), never colour alone.

## Ranking and tiers

Three tiers from the urgency the asker states: **Now** (urgency starts "first" or "high"), **This week** ("normal" and "medium"), **Can wait** ("low" and "not blocking"). Within a tier, "first" before "high", then oldest first. Now shows full cards; This week shows one-line rows that open into the card; Can wait is closed under one summary. The top of the page says the counts: 5 now, 14 this week, 9 can wait (from the file as it stands). Answered questions leave the page; they are not "20 more".

## Page structure (phone and desktop)

1. What needs you: title, the built/read line and the **next briefing time**, the three counts.
2. Decide now (cards), Decide this week (rows), Can wait (closed).
3. What changed since you last looked (needs a feed, below).
4. Running fine: two counts (43 agents, 17 blocked; 30 datasets, 6 with a source problem) linking to the full pages that stay as they are: every agent by desk, every dataset, other teams. Blocked agents are not repeated here: what an agent is blocked on is a decision, and decisions are above.

Desktop (1024 px and up): the cards in one column of about 760 px with a right rail holding the counts, the next briefing and the Running fine counts; no new colour; existing tokens.

## What the mock measures (same method as the baseline)

4.7 phone screens and 674 words for the whole page with this-week and can-wait collapsed (18.4 and 1,902 before); the first decision is under the header on the first screen. The mock is not the final page: it carries only decisions from the file, and its Know section is an example.

## What this needs from other agents (data shape; not decided)

- **cl-6.decisions, in questions.json**, per question: `title` (plain, under 80 characters), `why`, `if_you_wait`, `answer_line` (only the words to say or sign), `where` (where to say it: "in cl-6.maestro's session", "on GitHub", "sign in /admin/"), `tier` (now, week, later) and `kind` (decision, approval, information). Today `line_to_paste` mixes where and what. In the mock I wrote title, why and if-you-wait for the five Now items myself from the question text: decisions should confirm or replace them.
- **A "changed" feed** (cl-6.maestro or cl-6.decisions): one line each, with a date and hour, newest first: what was answered, released, or newly blocked since the last briefing.
- **The briefing cadence** (cl-6.maestro): the next briefing time as a field.

## Loop plan and scoring

Rubric, scored 1 to 5 by cl-6.synthetic as "Dinis the admin" on the live page (baseline), on this mock (loop 1) and on loop 2: (a) I can tell in 10 seconds what I must decide; (b) each decision is clear without opening anything; (c) I know the consequence of waiting; (d) I can answer without hunting for the words or where to say them; (e) I can tell what is information, not a decision; (f) I know when I am next briefed; (g) nothing is cut off or hidden; (h) it reads on a phone. Advisors are asked what should be on the page and what should not, per the conductor's brief.
