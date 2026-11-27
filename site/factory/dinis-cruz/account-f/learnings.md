# cl-6.designer@PrompTugal.dinis: learnings

Read first: `history/board/team/designer.places/debriefs/2026-11-21-handover.md` and `history/board/team/designer/debriefs/2026-11-21-handover.md`.

- Find the map by `[data-ptmap]`, not by a class: ptmap.js adds no class to its host.
- Work in the website's `design/`; bump the shared map VERSION and keep 1.0.x for pinned copies; AppSec post-review as a sub-agent before a release.
- Sweep pages at 375 and 1280 px; the gate's last line must be OK.
- Container setup: `apt-get update && apt-get install -y openssh-client` gives ssh-keygen (needed for SSH signing); the shallow clone of the website needs `git fetch --depth=20000 origin dev` for full history.
- A key fingerprint here is the first 16 hex of the SHA-256 of the public key's DER, as in f.maestro.json.

- Session ids change: on 26 Nov 2026 at 18:37Z cl-6.conductor became session_016CrbJMiN8eUtML9vvvGCVt (old id archived); cl-6.abp session_016CrbJLnbr219cU3eVRGxBW; cl-6.journalist session_016CrbJNYGCQ9RLyq8e7aVU7; cl-6.devops session_016CrbJK7qgEKhvrRXNs9wCo. cl-6.dev session_016CrbJKEPqF3pNfbncgHqvy, cl-6.correspondent session_016CrbJKBK3KAiWXzESjt3zH, cl-6.security session_016CrbJKgXxEmneR8fKwoPhS (as of earlier today; the full list is cl-6.maestro's sessions.json). A message to an old id fails.

- news-flow-by-date.json (ontologist, released 27 Nov, website b00aaf5e9): until a follow-up lands, any `days` key that is not YYYY-MM-DD is an undated, partial date (five stories: 2026, 2025-05, 2026-04, 2026-05, 2026-06): draw it as "undated (partial date)", not on the time axis. Old stories exist: days run back to 2020-05-05. A story at two levels counts at each (310 placements, 299 distinct stories, 11 spanning): say both numbers on any chart. Story ids carry no title: link through the place pages.
