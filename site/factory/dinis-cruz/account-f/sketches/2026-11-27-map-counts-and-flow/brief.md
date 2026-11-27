# First sketches: the map with counts, and local news flowing up (27 Nov 2026)

By cl-6.designer@PrompTugal.dinis, from Dinis's home page feedback (2) and (4) as the conductor relayed it at 00:58 UTC on 27 Nov (customers' brief 7 owns his words; I could not read it, so I worked from the conductor's summary). For cl-6.customers and cl-6.conductor; with cl-6.ontologist for the data shape; cl-6.dev builds. Everything below is drawn from the site's own data as built on 27 Nov: no figure is invented.

## 1. The map shows how many stories each place has

`map-counts-sketch.png`: the live home-page map with each pin turned into a count bubble: the number inside, the bubble's area following the count (the iOS app's way), no place names. What the sketch shows:
- It works away from the Algarve coast: counts from 5 to 15 read at a glance, and the largest stand out.
- It breaks at the bottom: the pins on the Algarve coast sit on top of each other (Faro's 28 is hidden under its neighbours). So the build needs the **Algarve inset** already planned as ptmap 1.1 (SM6): a second panel of the Algarve, enlarged, with the same count bubbles, and the mainland map shows one bubble for the whole region ("Algarve · N", the sum).
- Rules for the build: a place with no stories gets a small hollow ring with no number; the number is the story count the place's page shows (`ai_news` length); tapping a bubble goes to the place page; the bubble's accessible name is "Faro, 28 local stories". Region names are not drawn on the map.

## 2. Local news flowing upwards (first view)

`flow-sketch.png` (and `.svg`): per day, how many stories are filed under a local place, under the region (the Algarve) and under the country, three rows with local at the bottom flowing up to national, 1 Oct to 27 Nov 2026, with a dashed line where one story is filed under two levels.

What the data says today (from `data/by-place/*.json`, `ai_news`, read 27 Nov): 299 distinct stories; 276 are filed under a town, 19 under the Algarve and 22 under Portugal; **only 17 stories are filed under more than one place and only 11 under two levels**. So the "intersection" Dinis wants is almost empty today, not because the news does not connect but because each story is filed once. Also: the newest dated story is 17 Nov, ten days old, which bears on "news that visibly updates".

## 3. What I need from the ontologist (data shape; to agree, not decided)

- A story should carry **every place it concerns** (town, region, country), derived through each place's `parent`, so a Faro story is also an Algarve story and a Portugal story; one list, not three copies.
- A derived per-day file, for example `data/flow/by-date.json`: for each date, per place the count and the story ids, plus the stories that touch more than one level. Generated at build, never edited by hand.
- A dated `read_on` per story is already in `ai_news`; the view should show it, so readers can see what is new.

## 4. Other views Dinis named (a 3D view, a tree view, multiple graph views)

My recommendation, to be chosen with him: build the **tree** first (it is the honest shape of the data: Portugal, the Algarve, the towns, with counts, and the stories hanging on it), then this **per-day flow**, then consider 3D only if the first two do not show the intersection well. Not sketched yet: the tree, and any 3D view.

## What this does not claim

The sketches are from real data but are sketches: not built, not reviewed by cl-6.security, not on the site.
