# Human provenance, feedback, people, CRM and /admin/: the design (first draft, 27 Nov 2026)

Lead: cl-6.designer@PrompTugal.dinis. Shared document: cl-6.dev writes "Technical shape" and cl-6.security writes "Threat model" at the end, in this file or beside it. Design only: nothing is built or live. Source of the direction: Dinis's words as recorded by cl-6.decisions@dinis (record 2026-11-27__human-provenance-admin-crm, 1b0b1ac). What exists today (read 27 Nov 2026): PKI sign-in at /login/ (P-256 keys, public halves in `board/person-keys.json`, 2 keys), a signed-in area at /newsroom/, the append-lane pattern in `board/lanes/signups.json` (sealed, write-only, drained by an agent), and no /admin/ (404) and no /crm/ (404).

## 0. Rules this design keeps

- Static files only, no cookies, no tracking, no reader data sent anywhere except what a person chooses to send (a signed review, a feedback message).
- Public by default, sealed where it concerns a person: a signed review is public and verifiable; a feedback message, a contact, a CRM note and the admin's working data are sealed to a key and opened only in the browser of the person it is for.
- A person is named on the site only with that person's consent, recorded as a flag on their key entry. Without it, the site says "a reviewer" and the signature still verifies.
- Everything a reader sees about a person is a fact with its source (their signed record), never a claim by the site.
- Nothing is sent in Dinis's name without his line. Four things are his alone, listed in section 9.

## 1. Every story has an editor

On every article page, in the byline block under the title, one line before the review row:

> Edited by [Name] · [date of the edit]

- "Edited by" is the human who signed the review that put the story live (see 2). If none has, the line is not hidden: "Not yet edited by a person" in the muted style, so the gap is honest.
- The name is shown only if that person consented. Otherwise: "Edited by a PrompTugal editor (verified)".
- Agent authorship stays as it is ("agent-written · signed"). The editor line sits next to it, not in place of it.

## 2. Human review provenance per story

**What a reviewer does.** A signed-in person opens an article and sees, at the foot of the byline block, a quiet button: "I have read this and I agree". They can also choose "I have read this and I do not agree", with an optional one-line reason (sealed to the editors, not published). Neither is a vote or a rating; it is a signed statement about one version of one article.

**What is recorded (the review record).** Article id; the hash of the article's markdown twin at the moment of signing (so a later edit is a new version and the old review says so); reviewer key fingerprint; verdict (agree, disagree); time; the signature with that person's key. Nothing else: no IP, no browser detail.

**How it is shown.** A "Reviewed" row under the byline, with three states:
- "No human review yet" (muted).
- "Reviewed by 2 people: [Name], [Name]" (names only with consent; otherwise "2 verified reviewers"), each with the date; a small "Check" link opens a verify panel that shows the record and checks the signature in the browser against `board/person-keys.json`.
- "Reviewed before the latest edit" when the hash no longer matches: the old review stays visible, marked as of an earlier version. A reviewer can re-sign.

**Where it lives.** Signed records are appended by the reader's browser to a sealed write-only lane (the signups pattern), then a recorder agent verifies each signature and publishes the accepted ones as one public file per article (for example `data/reviews/<article-id>.json`), so the page reads a static file. A bad signature is dropped, not shown.

## 3. A feedback lane from the site

- A short form on every page foot and article page: a text box (up to 1000 characters), an optional "Your name or email, if you want a reply", and "Send". Labelled plainly: "Goes to the editors, sealed. We do not track you."
- Sent sealed to the editors' key through a write-only append lane, like signups. The page says "Sent." and nothing else: no reader count, no cookie, no "thanks for visiting".
- A signed-in person's feedback can be marked "as me" (signed); otherwise it is anonymous and untrusted by default.
- Everything that arrives is untrusted text. It is drained by one named agent (open question for Dinis, section 9) into the admin's Inbox.

## 4. Human journalists, researchers and validators as signers

- Each human gets a key entry in `board/person-keys.json` with a role: editor, reviewer, journalist, researcher, or source (an author or a source who validates a story about them). Dinis issues each key after the person agrees (his, section 9).
- A source or author asked to validate a story gets a review link for that one article. Their signed "this is accurate" or "this is not accurate, because..." is a review record of role "source". It is shown as "Checked by the source" (not by name unless they consent) and is the strongest line on the page.
- The request to them (who was contacted, when, how) is in the CRM, sealed. The page shows only the outcome.

## 5. The CRM, connected to Gmail

- Purpose: contact people about the site: sources to validate, journalists and researchers to invite, readers who sent feedback and asked for a reply.
- Design: a People list (name, role, how we know them, consent, key issued yes or no), a Threads list (per person, in date order), and a Drafts tray. Every outgoing email is a draft that Dinis approves; nothing is sent without his line.
- Gmail: read and send are separate switches, off by default (his, section 9). The connector, which agent holds it, and which mailbox are his decisions.
- Data location and who reads it are open (his, with cl-6.counsel, section 9). The design assumes the CRM data is sealed to Dinis's key and opened in his browser, never on a public page.

## 6. The /admin/ section

Constraint that shapes it: the site is static, so a page cannot hide anything by itself. /admin/ is a public shell with no data in it. Its data files are sealed to Dinis's key and decrypt in his browser after /login/ (the pattern of the observability pages under /newsroom/). Anyone else sees the shell and "Sign in with your key".

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
Edited by Maria Santos · 26 Nov      agent-written · signed
Reviewed by 2 people (Check)         [ I have read this and I agree ]
```
/admin/ Today (phone):
```
Today
Needs you (3)    > Gmail: read or send?
                 > Name Maria Santos as editor?
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

1. Issuing each person's key: for whom, and in what order (his: trust in keys, after each person agrees)?
2. May any named person (editor, reviewer) be shown by name on the site, and who has agreed (his: consent)?
3. Gmail: which agent holds the connector, which mailbox, and is it read or send (his: a connector)?
4. Where does the CRM data live and who reads it, with cl-6.counsel's view on data protection (his)?
5. Which agent drains the feedback lane into the Inbox?
6. Is "I do not agree" a verdict readers see, or only the editors?

## 10. Technical shape (cl-6.dev writes here)

## 11. Threat model (cl-6.security writes here)

## 12. What this design does not claim

It is a first draft. No file shape, key format, lane or page is final until cl-6.dev and cl-6.security have written their sections, and nothing is built.
