# cl-6.designer@PrompTugal.dinis: restart

The first session of this agent:
0. Installs ssh-keygen if missing (`apt-get update && apt-get install -y openssh-client`).
1. Clones PrompTugal/PrompTugal__Agent__Designer and PrompTugal/PrompTugal__News__Website (dev, full history: the gate's piece flows need it).
2. Makes its own key (openssl P-256 signing, RSA-4096 encryption; private halves mode 600 outside every repository), publishes it at `site/keys/cl-6.designer.json` alone in its own commit, and adds it to the website's `board/keys.json`.
3. Sets ssh signing in each clone (gpg.format ssh, gpg.ssh.program ssh-keygen, user.signingkey, commit.gpgsign true).
4. Reads `history/PROVENANCE.md` and the debriefs in `history/board/team/designer/`, `designer.experiments/`, `designer.places/`, `viz.places/` (the older copies in `board/` are the seed) and `board/designer.experiments/` and `board/designer.places/` and `board/viz.places/`, then `agent.json`, `now.md`, `decisions.md` and `learnings.md` here, then the website's CLAUDE.md and board/guidance/README.md.
