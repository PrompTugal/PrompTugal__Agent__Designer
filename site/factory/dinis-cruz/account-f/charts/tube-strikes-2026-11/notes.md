# The eight Tube strike windows: chart (cl-6.designer, 26 Nov 2026)

From cl-6.correspondent's visual spec and draft (facts 1 to 3, TfL press release PN-259, 23 Nov 2026, read 26 Nov 2026). Files: `tube-strikes-chart.svg` (640 wide, follows light and dark mode, text is live text in IBM Plex Mono and Newsreader with serif and mono fallbacks), light and dark PNGs at 2x, `strikes.json` (the data, for cl-6.dev).

- Calendar strip, one row per strike, dates in the mono style ("Thu 26 Nov to Fri 27 Nov"); each bar runs from 12:00 on the first day to 11:59 on the next, with a minimum width of 8 units so a one-day window stays visible. Filled: under way (strike 1, today). Outlined: announced. Footnote: "Filled: under way. Outlined: announced; dates after the first may change."
- Second panel: strike 1 by line, four rows, each with a distinct fill pattern as well as words (solid: no service; half: no service after 12:00; hatched: disruption; outline: expected to run), so no meaning depends on colour. Strikes 2 to 8: "Line detail ... to come: TfL has not published it." Nothing invented.
- No journeys-per-day figure: none is public. Neutral ink on paper, no red or green on either side; the green rule at the top is the brand's.
- Text alternative: the SVG's `<desc>` lists the eight dates and the strike 1 service picture. The article should repeat the dates in text.
- Weekdays computed from the dates (26 Nov 2026 is a Thursday, as TfL says).
- Not published by me: the article and any release go through cl-6.journalist, cl-6.dev and cl-6.security. The strike statuses ("under way" for strike 1) are as of 26 Nov 2026; dev should derive filled or outlined from the date at build time.
