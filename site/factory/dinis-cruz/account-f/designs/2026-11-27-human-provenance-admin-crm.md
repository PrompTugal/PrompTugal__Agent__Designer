# Human provenance, feedback, people, CRM and /admin/: the design (first draft, 27 Nov 2026)

Lead: cl-6.designer@PrompTugal.dinis. Shared document: cl-6.dev writes "Technical shape" and cl-6.security writes "Threat model" at the end, in this file or beside it. Design only: nothing is built or live. Source of the direction: Dinis's words as recorded by cl-6.decisions@dinis (record 2026-11-27__human-provenance-admin-crm, 1b0b1ac). What exists today (read 27 Nov 2026): PKI sign-in at /login/ (P-256 keys, public halves in `board/person-keys.json`, 2 keys), a signed-in area at /newsroom/, the append-lane pattern in `board/lanes/signups.json` (sealed, write-only, drained by an agent), and no /admin/ (404) and no /crm/ (404).

## 0. Rules this design keeps

- Static files only, no cookies, no tracking, no reader data sent anywhere except what a person chooses to send (a signed review, a feedback message).
- Public by default, sealed where it concerns a person: a signed review is public and verifiable; a feedback message, a contact, a CRM note and the admin's working data are sealed to a key and opened only in the browser of the person it is for.
- A person is named on the site only with that person's consent, recorded as a flag on their key entry. Without it, the site says "a reviewer" and the signature still verifies.
- Everything a reader sees about a person is a fact with its source (their signed record), never a claim by the site.
- Nothing is sent in Dinis's name without his line. Four things are his alone, listed in section 9.
- Two findings from cl-6.dev's reading of the live code (27 Nov), both before anything is built: (1) `/login/`'s `keyring.js` stores the private key in IndexedDB and a pointer in localStorage today, which breaks the first /admin/ condition (section 6), so the login must change first; (2) the signups lane's append token is public in the repository, so a feedback lane built the same way will be spammed unless the service rate-limits it (cl-6.infra's).
- People make their own keys on their own device. No agent ever generates or holds a person's private key (cl-6.security, 27 Nov). Dinis's anchor key signs the statement that enrols a key, and any revocation; the list of people is separate from the agents' list (`board/keys.json`).

## 1. Every story has an editor

On every article page, in the byline block under the title, one line before the review row:

> Edited by [Name] · [date of the edit]

- "Edited by" is the human who signed the review that put the story live (see 2). If none has, the line is not hidden: "Not yet edited by a person" in the muted style, so the gap is honest.
- The name is shown only if that person consented. Otherwise: "Edited by a PrompTugal editor (verified)".
- Agent authorship stays as it is ("agent-written · signed"). The editor line sits next to it, not in place of it.

## 2. Human review provenance per story

**What a reviewer does.** A signed-in person opens an article and sees, at the foot of the byline block, a quiet button: "I have read this and I agree". They can also choose "I have read this and I do not agree", with an optional one-line reason (sealed to the editors, not published). Neither is a vote or a rating; it is a signed statement about one version of one article.

**What is recorded (the review record).** A canonical statement, signed in a namespace of its own for reviews: the article's slug (its canonical path); the sha256 of the exact bytes of the article's markdown twin at the moment of signing (so a later edit is a new version and the old review says so); the reviewer's key fingerprint; the verdict (agree, disagree); the time; and the signature with that person's key. Nothing else: no IP, no browser detail.

**How it is shown.** A "Reviewed" row under the byline, with three states:
- "No human review yet" (muted).
- "Reviewed by 2 people: [Name], [Name]" (names only with consent; otherwise "2 verified reviewers"), each with the date; a small "Check" link opens a verify panel that shows the record, hashes the twin **as it is served now**, compares it with the signed hash, and checks the signature in the browser against the enrolled people list. An "Edited by" name renders only from a verified statement, never from a front-matter `editor:` line.
- "Reviewed before the latest edit" when the hash no longer matches: the old review stays visible, marked as of an earlier version. A reviewer can re-sign.

**Where it lives.** Signed records are appended by the reader's browser to a write-only lane (the signups pattern), then a recorder agent verifies each signature and publishes the accepted ones as one public file per article (for example `data/reviews/<article-id>.json`), so the page reads a static file. The recorder handles ciphertext and signatures only and never holds anyone's decryption key. It can drop a record but cannot forge one, so the lane carries a sequence or hash chain, and a reviewer can see that their own record was published (and, if it was not, say so). A bad signature is dropped, not shown.

## 3. A feedback lane from the site

- A short form on every page foot and article page: a text box (up to 1000 characters), an optional "Your name or email, if you want a reply", and "Send". Labelled plainly: "Goes to the editors, sealed. We do not track you."
- Encrypted in the reader's browser to a key only human readers hold, appended through a write-only lane, like signups. The page says "Sent." and nothing else: no reader count, no cookie, no "thanks for visiting".
- A signed-in person's feedback can be marked "as me" (signed); otherwise it is anonymous and untrusted by default.
- Everything that arrives is untrusted text, shown as plain text. **No agent reads or acts on a message's content**: it is read by people in the admin's Inbox (which humans hold the feedback key is an open question, section 9).

## 4. Human journalists, researchers and validators as signers

- Each human makes their own key on their own device and is enrolled by a statement signed by Dinis's anchor key, after the person agrees (his, section 9), with a role: editor, reviewer, journalist, researcher, or source (an author or a source who validates a story about them). Revocation is the same kind of signed statement.
- A source or author asked to validate a story gets a review link for that one article. Their signed "this is accurate" or "this is not accurate, because..." is a review record of role "source". It is shown as "Checked by the source" only with that source's consent, because the line itself reveals that a source exists; a confidential source never gets a public key entry. It is the strongest line on the page when it is allowed.
- The request to them (who was contacted, when, how) is in the CRM, sealed. The page shows only the outcome.

## 5. The CRM, connected to Gmail

- Purpose: contact people about the site: sources to validate, journalists and researchers to invite, readers who sent feedback and asked for a reply.
- Design: a People list (name, role, how we know them, consent, key issued yes or no), a Threads list (per person, in date order), and a Drafts tray. Every outgoing email is a draft that Dinis approves; nothing is sent without his line.
- Gmail (cl-6.security's conditions): the smallest scope, read-only on one label. **Send stays off.** If it is ever on, the connector creates drafts only and Dinis sends them himself, because an agent holding the send scope could send as him whatever the approval screen says. The connector, which agent holds it, and which mailbox are his decisions.
- Data location and who reads it are open (his, with cl-6.counsel, section 9). The design assumes the CRM data is sealed to Dinis's key and opened in his browser, never on a public page.

## 6. The /admin/ section

Constraint that shapes it: the site is static, so a page cannot hide anything by itself. /admin/ is a public shell with no data in it. Its data files are sealed to Dinis's key and decrypt in his browser after /login/ (the pattern of the observability pages under /newsroom/). Anyone else sees the shell and "Sign in with your key". cl-6.security confirmed this on 27 Nov, on four conditions that are part of the design:
- /login/ never stores a private key in localStorage, IndexedDB or a cookie: the key is unwrapped per visit (a passkey via WebAuthn PRF, a hardware key, or a file he picks) and held in memory only; closing the tab forgets it.
- No token of any kind is in the shell, its script or a data file: no GitHub token, no Gmail token. It writes only signed objects, through the gate.
- A strict content-security policy: no inline or third-party script, `connect-src` limited to named hosts. Every decrypted field renders as plain text, and links pass the site's safe-URL check.
- The sealed files carry no plaintext metadata (names, emails, counts) beside the ciphertext.

Home ("Today"), in this order:
1. **Needs you**: the decisions marked "For Dinis", drafts waiting for his line, review requests, anything blocked.
2. **Since you were last here**: what changed (new articles, reviews signed, feedback received), each one line with a date.
3. **Stories**: each article with its editor, its reviews (count and state) and a "Request a review" action.
4. **People**: signers, their roles, key issued, consent, last review.
5. **Inbox**: the feedback lane, newest first, a "Reply via CRM" action.
6. **Contacts**: the CRM (section 5).
7. **Agents**: each agent's state from its area (agent.json), who is waiting on whom.
8. **Settings**: the switches (Gmail read, Gmail send), the keys, the lanes.

Look: the existing brand, the same type and tokens as /newsroom/, dates in the mono style, no new colour. Phone first: one column, a bottom bar with Today, Stories, People, Inbox.

## 7. Wireframes (low fidelity)

Article byline block:
```
Title
Edited by [Name] · 26 Nov      agent-written · signed
Reviewed by 2 people (Check)         [ I have read this and I agree ]
```
/admin/ Today (phone):
```
Today
Needs you (3)    > Gmail: read or send?
                 > Name [Name] as editor?
                 > Draft to a source, waiting
Since 26 Nov     > 4 reviews signed  > 7 feedback messages
[ Today | Stories | People | Inbox ]
```

## 8. Build order I recommend

1. The "Edited by" and "Reviewed" rows, reading a static reviews file (no sign-in yet).
2. Signing a review from /login/ with the verify panel.
3. The feedback lane and the admin Inbox.
4. The /admin/ shell with Needs you and Stories.
5. People, then the CRM, then Gmail last (the most sensitive).

## 9. Open questions for Dinis (one line each)

1. Enrolling people: whose keys does your anchor key sign, and in what order (his: trust in keys, after each person agrees; each person makes their own)?
2. May any named person (editor, reviewer) be shown by name on the site, and who has agreed (his: consent)?
3. Gmail: which agent holds the connector, which mailbox, and is it read or send (his: a connector)?
4. Where does the CRM data live and who reads it, with cl-6.counsel's view on data protection (his)?
5. Which humans besides you hold the feedback key and read the Inbox?
6. Is "I do not agree" a verdict readers see, or only the editors?

## 10. Technical shape (cl-6.dev, 27 Nov 2026; design only, nothing built)

Read first (27 Nov, website v0.1.2358): `board/person-keys.json` holds 2 keys for dinis (P-256 `encrypt` and `sign` JWKs, fingerprints, `status`; one is `replaced`). `assets/login/keyring.js` **stores the private key in IndexedDB and a pointer in localStorage today**: that breaks cl-6.security's first /admin/ condition, so the login must change before /admin/ exists (10.6). `board/lanes/signups.json` is an append lane whose **append token is public in the repository** (write-only by design, so anyone can append). Sealing is `ws-ecies-1` (observability, talk, `newsroom/tools/person-key.mjs`). The site's headers cannot be set (static hosting): a CSP is a `<meta>` tag, as `payments.mjs` and `principles.mjs` already do, and that cannot carry `frame-ancestors`.

### 10.1 The trust chain and its files

anchor key (Dinis's signing key) -> enrolment statement -> person key -> review record. One chain, verified by **one module, `newsroom/build/lib/review-verify.mjs`, written on WebCrypto**, which Node 18 and every browser both have, so the gate, the build and the page's "Check" panel run the same code and cannot disagree.

- **Anchor.** Listed as an operator in `newsroom/tools/operator-keys.json`, under the existing gate rule 18 (first entry by a commit signed with that very key, later changes by a listed key, never by an agent key). Nothing new to trust: this is the S13 anchor, reused.
- **`board/people-enrolments.json`** (new, public, append-only). Each statement is canonical JSON, signed by the anchor:
  `{v:1, kind:"enrol", person, role, signing_fingerprint, sign:{JWK}, encrypt:{JWK}, consent_name:true|false, display_name (only if consent_name), at}` and `{v:1, kind:"revoke", signing_fingerprint, at}`. The consent flag is **inside the signed statement**, so the site cannot claim a consent the person did not give; a name is rendered only from a statement with `consent_name:true`. Role is one of editor, reviewer, journalist, researcher, source. A source with no consent has no entry at all (a confidential source never gets a public key).
- **`board/person-keys.json` stays as it is** (the sealing keys for observability); enrolment is the new, separate list of who may sign reviews.
- A change to the enrolments file is a commit whose new statements all verify against the anchor; the gate refuses an unsigned or mis-signed statement, and refuses a removed one (revocation is a new statement, history is kept).

### 10.2 The review record, where it lives, how it is verified

Record (canonical JSON: keys sorted, UTF-8, no spaces; signed bytes are `"promptugal-review-v1\n"` + that JSON, so a review signature can never be replayed as anything else):
`{v:1, kind:"review", article:"articles/<slug>", twin_sha256, reviewer:<signing_fingerprint>, role, verdict:"agree"|"disagree", at:"<UTC, seconds>", reason_ref (optional: sha256 of a sealed reason blob, never the reason)}` + `sig` (ECDSA P-256 / SHA-256, IEEE P1363, base64url).
`twin_sha256` is the hash of the exact bytes of `/articles/<slug>.md` as served. A later edit changes the hash, so the old review is honestly "of an earlier version".

- **Where:** the browser appends the signed record to a lane (10.4); a **recorder agent** verifies it with `review-verify.mjs`, checks the reviewer is enrolled and not revoked at `at`, and writes the accepted ones to `data/reviews/<slug>.json` (`{article, records:[...]}`, newest last) and `data/reviews/index.json`. The recorder never holds any decryption key (records are public signed statements, not sealed). It needs an ABP write grant for `data/reviews/**` from cl-6.abp; no agent has it today, and which agent records is Dinis's call.
- **Tamper evidence:** each lane entry carries `seq` and `prev` (hash of the previous entry), the recorder publishes the head hash in `data/reviews/index.json`, and the gate re-verifies every record and the chain on every build. The recorder can drop a record but not forge one, and a reviewer can see that theirs is missing from the index.
- **On the page (works without JavaScript):** the build renders "Edited by" and "Reviewed by" statically from verified records, comparing `twin_sha256` with the twin it just built (a stale one is shown "reviewed before the latest edit"). The browser script only adds the "Check" panel: it fetches the record, the enrolments file and the twin from the same origin, hashes the twin as served now, verifies the chain and signature with `crypto.subtle`, and shows each step. No third-party request.
- **Front matter:** there is **no `editor:` key**. "Edited by" is derived from the latest verified editor review whose hash matches; the gate **refuses** an `editor:` or `reviewed_by:` key in front matter (the design says a name renders only from a verified statement). The derived `editor` (person id or "a PrompTugal editor") and `reviewed` (count, state) are added to the articles API listing next to the ontologist's `level`. An optional `review_requested: <person id>` front-matter key may name who was asked; it renders nothing.
- **Gate rules to add** (each its own `lib/*-cli.mjs`, so the prose-in-strings baseline does not rise): enrolments verify; every review record verifies, is by an enrolled and unrevoked key, names an existing article; no `editor:`/`reviewed_by:` front matter; no private key shape in any new file.

### 10.3 What the browser needs from /login/

Signing a review uses the person's own key, made on their own device. The browser signs with `crypto.subtle.sign`, prefixes nothing it was not given, and shows the person the exact record before signing. **/login/ must change first:** drop the IndexedDB and localStorage key storage; unwrap the key per visit from a file the person picks, or a passkey with WebAuthn PRF, and hold it in a non-extractable `CryptoKey` in memory only. **Amended by cl-6.security's review (see 10.7): the 2 keys already issued are not unaffected**; they were made by an issuing tool that kept the private half, so they are replaced, not kept. Browser support for PRF is uneven, so the file route is the baseline and PRF an addition. That is roughly a day of work and a security review; it blocks 10.2's signing and 10.5.

### 10.4 The feedback lane (same pattern as signups, three changes)

`board/lanes/feedback.json`: append endpoint, public append token, and a **list of recipient public keys** (the holders of the feedback key; open question 5). The browser makes a random content key, encrypts the message with AES-GCM, and wraps the content key to each recipient with `ws-ecies-1`, so adding or removing a reader is a change to the list, not a re-seal of old mail. Changes from signups: (1) the plaintext is padded to fixed sizes (1 KB or 2 KB buckets) so length leaks nothing; (2) a small client proof-of-work and the 1000-character cap are checked by the drainer, because the append token is public and the lane will be spammed (this is also a risk for signups today, to be raised with cl-6.infra: a rate limit at the service is the real fix); (3) "as me" puts a review-style signature inside the sealed payload, never outside it. The **drainer is an agent that moves ciphertext only**: it writes `data/inbox/sealed/<seq>.json` with a sequence number as its only metadata (no names, dates, sizes beyond the bucket, counts per sender). No agent decrypts, parses or acts on a message; the admin Inbox decrypts in a human's browser and renders plain text only, links through the site's safe-URL check.

### 10.4a Rate limiting the lane (cl-6.infra, 27 Nov 2026; design only, nothing changed)

cl-6.infra read `board/lanes/signups.json`: the service behind the lane is SG/Send (`dev.send.sgraph.ai`), which PrompTugal__IaC does not run, so there is no switch for infra to flip. Options, cheapest first:
1. **Ask SG/Send's operators** whether a vault or token can carry a rate or quota limit (per minute and per day). If it can, only a field in `lanes/feedback.json` changes. Costs nothing in AWS but is a request to another service, so it is Dinis's to make. Whether SG/Send offers it is not known.
2. **A thin append proxy we own** (for example at `lanes.promptugal.news`) in front of SG/Send: the browser posts the sealed payload to the proxy; the proxy holds the append token server-side, so it stops being public (the bigger win), and applies a per-IP rate rule and a global cap; the drainer's proof of work and the 1000-character cap stay as a second line. In AWS (the account IaC already uses for Route 53, not a new one) this is a small HTTP API with a Lambda, or CloudFront plus WAF with a rate-based rule; cost is small at this volume and must be priced from AWS's pages before it is asked for. It needs from Dinis: AWS spend; a new role or wider rights for CI to deploy it (today the IaC role can only create Route 53 records); a `policy/abp.json` change for the new pipeline; and the token moved into a secret. cl-6.security reviews it; cl-6.infra drafts it as IaC pull requests. The same proxy would also close the public-token risk on the signups lane.
3. A third-party bot check in front of the form: **not recommended**, because it costs readers' privacy against the "We do not track you" promise.

Recommendation (cl-6.infra): ask (1) first; if SG/Send cannot limit per token, do (2). Whichever route, the lane config names its limit, so the page can say "try again later" instead of failing silently. The design's reader wording for that case: "Too many messages are being sent right now. Please try again later." One more design point from me: the feedback form never shows a reader count or a success tally, so a limit message is the only place the page ever talks about volume.

### 10.5 What /admin/ can do with static files only

A built page `/admin/` (a new feature `admin.mjs`; the page and its one script are public). Strict CSP meta: `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; base-uri 'none'; form-action 'none'`, no inline script, no third-party host; `referrer: no-referrer`. Because a meta tag cannot set `frame-ancestors`, the script refuses to run if `window.top !== window` (clickjacking guard), and says so.
- **Public data needs no sealing.** Needs-you (the "For Dinis" decisions), Stories (editor, reviews), People (the enrolments: public by design), Agents (state files), Since-last-here: all are already public in the repository, so the page reads the public JSON directly and sealing them would add nothing. "Since you were last here" keeps one timestamp in `localStorage`, a per-viewer convenience in try/catch, never an identifier.
- **Sealed:** Inbox, Contacts (CRM), Drafts. These are `data/admin/<name>.sealed.json`, `ws-ecies-1` to the encrypt key of each person allowed to read them (from `board/person-keys.json`), no plaintext metadata beside the ciphertext, decrypted in the browser after sign-in. A CRM file is written by a sealer tool that runs where the plaintext is, never in CI, and never by an agent that would then also read it; where that is, and Gmail, remain Dinis's (his questions 3 and 4).
- **What it cannot do, said plainly:** it cannot hide anything from a person who has the key, cannot stop a fetch of the (public) shell and sealed files, cannot revoke a decrypted copy, and cannot write anything itself. Every write is a signed object appended to a lane or a commit through the gate. No cookies, no server, no token of any kind in the page, its script or its data (security's condition 2).

### 10.6 Order, effort and what blocks what

1. `/login/` key handling (10.3): blocks everything that signs or opens sealed files. About a day plus security.
2. `review-verify.mjs`, the enrolment file, the gate rules and the static "Edited by / Reviewed" rows, reading an empty `data/reviews/`: about a day, no sign-in. Nothing live changes until a record exists.
3. Signing from the page and the "Check" panel; the recorder agent (needs the ABP grant and Dinis naming it).
4. The feedback lane and drainer (needs `board/lanes/feedback.json`, a service-side rate limit from cl-6.infra, and Dinis's answer on who holds the feedback key).
5. `/admin/` shell, then Inbox, People, then CRM, Gmail last.

Needs from others, not mine to decide: the anchor key and each enrolment (Dinis); who records and who drains (Dinis, with cl-6.abp for the grants); rate limiting (cl-6.infra); consent and the data-protection view (Dinis, cl-6.counsel); the CRM and Gmail (Dinis). Every step goes through cl-6.security before it is live.

### 10.7 Amendments from cl-6.security's whole review of revision 3 (27 Nov 2026, 01:13 UTC)

Review: https://github.com/PrompTugal/PrompTugal__Agent__Security/blob/dev/docs/security/reviews/2026-11-27-human-provenance-design-r3.md (1c65fd1). Verdict: sound to build in the order of 10.6, on these changes. They bind the step each one touches; none is optional where marked "required".

Required before the step they touch goes live:
1. **The two existing keys are replaced.** They were made by `person-key.mjs`, whose issuing agent keeps the private half (security finding S17, medium, live). Dinis makes a new key in his own browser; the anchor key enrols it; the old two are revoked; `person-key.mjs` is retired. **Until then, nothing new that only Dinis should read is sealed to the current key.** (This replaces the sentence in 10.3 that said the 2 keys were unaffected.)
2. **/admin/ seals only to person-made keys** enrolled in `people-enrolments.json` (10.5), never to the keys in `board/person-keys.json` that an agent issued.
3. **The anchor is stated by Dinis, not only self-signed.** The first anchor entry is signed by itself (finding S13). Dinis must state the anchor key's fingerprint in his own words (a decisions record or his own session), and the gate checks the first entry against it.
4. **Revocation is judged by receipt, not by the signer's clock.** Order is the commit or receipt order, never the signer's own "at"; the gate refuses an "at" later than its commit (10.2).

Recommended:
5. The service-side rate limit for the public append token (10.4a), for the signups lane too.
6. A reviewer's key fingerprint is linkable, pseudonymous personal data: the consent text a reviewer sees, and cl-6.counsel's view, must cover it.
7. Wording: IndexedDB holds the private key today; localStorage holds only the person id (10 intro and 10.3 should say so).

Everything else in this document is confirmed as designed by cl-6.security.

## 11. Threat model (cl-6.security)

Unchanged, in cl-6.security's home: https://github.com/PrompTugal/PrompTugal__Agent__Security/blob/dev/docs/security/design/2026-11-27-human-provenance-threat-model.md (b8f397f). Its headline points are folded into sections 0 to 6 above. cl-6.security will review this document whole when section 10 is in.

## 12. What this design does not claim

Revision 4 (cl-6.security's amendments are in 10.7). Sections 10 and 11 are written (cl-6.dev's text is pasted unchanged; cl-6.security's is linked). Not final until cl-6.security has reviewed the whole document, and Dinis has answered the questions in section 9. Nothing is built.
