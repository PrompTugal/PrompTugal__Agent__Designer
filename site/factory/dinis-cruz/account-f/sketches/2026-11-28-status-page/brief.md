# Status page: layout sketch (28 Nov 2026)

By cl-6.designer@PrompTugal.dinis for cl-6.dev, from cl-6.maestro's cell 2026-11-28-promptugal-status (Dinis's word: "the current status of everything happening and all the mapping of every single agent ... what is everybody doing and what's the status of the data"). Layout only. Files: `status-sketch.png` and `.svg`. Every name, state, count and date in the sketch is an example, not a fact.

Order on the page, top to bottom (Dinis's order: waits on him first, then agents by desk, then data freshness):
1. Title "Status of PrompTugal" and one line: "Built <date, hour UTC> · agents read <hour> · data read <hour>".
2. **Waits on Dinis**: a boxed list (heavy border), same items as his briefing page, each "what · who is waiting".
3. **Agents**: a count ("41 agents, 9 desks"), two filter buttons (all, only blocked), then desks. Each desk is a heading with its count and states ("Newsroom (6) · 4 working · 1 waiting") and a row per agent: name, a state chip, last activity (absolute date and hour, what), next step, blocked on, home repo link. Below 768 px each desk is a closed `details` that opens on its blocked rows; blocked rows have a heavy border and come first in their desk.
4. **Data**: a count ("12 sets · 3 stale"), stale first, each row: name, owner, last read (absolute), source, rows, verdict chip (fresh, stale, failed) with the threshold shown on the page (older than 13 hours for hourly data, Dinis 19 Nov).

Rules: a state is a word in a chip (working, waiting, blocked, idle, archived), never colour alone; every date absolute with its hour in UTC, no relative times; the page says when it was built and when each feed was read; no sideways scroll at 320 px; existing site classes and tokens, no new colour, no new host. On desktop (1024 px and up): the waits box full width at the top, agents as a table per desk with sortable columns in two columns of desks, a left rail of the desks as anchors with the number of blocked agents beside each, data as a table.

Feeds named in the cell brief: agents.json (cl-6.observability), a data-status file (cl-6.data), the briefing and questions files. Anything the feeds do not carry is shown as "not reported", never guessed.
