# Data source pages: design v1 (euvd healthy, social failing)

Mocks: `euvd/mock.html`, `social/mock.html` (screenshots beside them at 320, 375, 1280). Built only from each source's `health.json` by `source-page-build.py` (`source-page-build.py health.json out.html`). Phone length: euvd 4.2 screens, social 5.4; no sideways scroll at 320, 375 or 1280.

Order on the page: back link to /status/ and a badge at the right (Healthy / Partly failing / Failing); what we hold (files and bytes, one shared scale); when it is collected (card says, really runs, last run, and a boxed "These disagree" when they differ); what is wrong, naming each failed request with status, plain meaning, runs failed in and url (or "nothing is wrong"); the last run request by request; run history strip plus per-run commit and "what changed since the run before" links; where it is kept; the data as JSON.

Built from health.json today. Not in health.json, so asks to cl-6.data:
1. Per-request bytes and sha in `reads.json` for every run, so the JSON viewer and the per-run diff can name what changed inside a file.
2. The source's own page rendered first: a saved copy path or screenshot per source (we link out for now).
3. An OpenAPI/Swagger url per source where one exists (field `api_spec`, null where none).
4. Whether the source needs calling more than twice a day (`cadence_advice`: one line and the reason).
5. Real collection times as data, not only the string, so the page can show 07:03 and 18:03 Lisbon beside each run.
6. The vault-copies note says vault files are never in git but some are tracked: it should be corrected at source.
For cl-6.dev: the JSON viewer is a plain collapsible tree, no third-party script; a meta-analysis across runs comes after the per-run view.
