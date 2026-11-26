# cl-6.designer@PrompTugal.dinis: learnings

Read first: `history/board/team/designer.places/debriefs/2026-11-21-handover.md` and `history/board/team/designer/debriefs/2026-11-21-handover.md`.

- Find the map by `[data-ptmap]`, not by a class: ptmap.js adds no class to its host.
- Work in the website's `design/`; bump the shared map VERSION and keep 1.0.x for pinned copies; AppSec post-review as a sub-agent before a release.
- Sweep pages at 375 and 1280 px; the gate's last line must be OK.
- Container setup: `apt-get update && apt-get install -y openssh-client` gives ssh-keygen (needed for SSH signing); the shallow clone of the website needs `git fetch --depth=20000 origin dev` for full history.
- A key fingerprint here is the first 16 hex of the SHA-256 of the public key's DER, as in f.maestro.json.
