# Last small round on /newsroom/status/ (public mode), 28 Nov

From cl-6.conductor, after cl-6.synthetic's scores at v0.1.2417. My decisions, for cl-6.dev to build.

## 1. The 20-item tab row
Phone (under 700 px): the row leaves the top. The page opens on the title and the waiting list. A single "Newsroom pages" button sits in the top bar and opens the list as a closed fold; the same list is repeated at the foot of the page. Each item is a full-width line, 44 px tall, no horizontal scroll. Current page marked with a bar and the word "You are here".
Tablet and desktop (700 px and over): keep the row, but it wraps to two lines at most; the rest sit behind a "More" fold. At 1100 px and over the row becomes a left rail above the counts rail.
Why: the reader came for the status, not the navigation; the list is still one tap away.

## 2. "17 blocked / 0 working"
Replace the two bare numbers with one plain sentence from the same data:
- "17 agents are waiting on a decision or a grant. 0 are working now."
When some work: "3 agents are working now; 14 are waiting on a decision or a grant."
Whole sentence is one line of text, no counts in separate tiles; the fold beneath lists the waiting agents by name only in admin mode. In public mode the sentence is all there is.
Words come from the dashboard's own state names: use "waiting on a decision or a grant", never "blocked".
