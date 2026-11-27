# Human provenance, feedback, people, CRM and /admin/: the design (first draft, 27 Nov 2026)

Lead: cl-6.designer@PrompTugal.dinis. Shared document: cl-6.dev writes "Technical shape" and cl-6.security writes "Threat model" at the end, in this file or beside it. Design only: nothing is built or live. Source of the direction: Dinis's words as recorded by cl-6.decisions@dinis (record 2026-11-27__human-provenance-admin-crm, 1b0b1ac). What exists today (read 27 Nov 2026): PKI sign-in at /login/ (P-256 keys, public halves in `board/person-keys.json`, 2 keys), a signed-in area at /newsroom/, the append-lane pattern in `board/lanes/signups.json` (sealed, write-only, drained by an agent), and no /admin/ (404) and no /crm/ (404).

## 0. Rules this design keeps

- Static files only, no cookies, no tracking, no reader data sent anywhere except what a person chooses to send (a signed review, a feedback message).
- Public by default, sealed where it concerns a person: a signed review is public and verifiable; a feedback message, a contact, a CRM note and the admin's working data are sealed to a key and opened only in the browser of the person it is for.
- A person is named on the site only with that person's consent, recorded as a flag on their key entry. Without it, the site says "a reviewer" and the signature still verifies.
- Everything a reader sees about a person is a fact with its source (their signed record), never a claim by the site.
- Nothing is sent in Dinis's name without his line. Four things are his alone, listed in section 9.
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

## 10. Technical shape (cl-6.dev writes here)

## 11. Threat model (cl-6.security)

Unchanged, in cl-6.security's home: https://github.com/PrompTugal/PrompTugal__Agent__Security/blob/dev/docs/security/design/2026-11-27-human-provenance-threat-model.md (b8f397f). Its headline points are folded into sections 0 to 6 above. cl-6.security will review this document whole when section 10 is in.

## 12. What this design does not claim

It is a first draft. No file shape, key format, lane or page is final until cl-6.dev and cl-6.security have written their sections, and nothing is built.
