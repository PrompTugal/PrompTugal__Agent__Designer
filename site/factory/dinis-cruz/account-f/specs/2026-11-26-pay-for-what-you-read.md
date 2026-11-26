# Pay for what you read: the masthead chip and /account/ (spec, 26 Nov 2026)

By cl-6.designer@PrompTugal.dinis, from the conductor's brief of 26 Nov (Dinis's word: every reader starts with £5; at zero they keep reading; we see whether they top up). For cl-6.dev to build in `assets/meter/meter.js` and `meter.css` (switch `SHOW_CHIP`), through cl-6.security. Brand unchanged: existing tokens, `.tool.meter`, `.balance-card`, `.btn`, `.notice`. No new colour.

The chip was switched off on 26 Nov because it contradicted /account/'s "Nothing is charged" (synthetic's N1). This spec removes the contradiction: one model, said the same way everywhere. The words below are the whole set; nothing else on the page may say "charged" or "paywall".

## The one sentence (used on the chip's tooltip, /account/ and the explainer page)

"You start with £5.00 of reading credit, kept in this browser. It goes down as you read, by how much of a page you read. When it runs out you can still read everything."

## The masthead chip (`a.tool.meter`, in the tools row)

Shape: as today: 34 px high, mono figure, the label "Pay for what you read" shown from 768 px, hidden below (figure only on a phone). It always links to /account/.

| State | Balance | Chip text (768 px and up) | Phone | Look |
|---|---|---|---|---|
| Full | £5.00 down to £1.00 | Pay for what you read · £4.20 | £4.20 | as `.tool.meter` today |
| Low | under £1.00, above £0.00 | Pay for what you read · £0.60 | £0.60 | existing `is-low` border (warn colour) |
| Zero | £0.00 or less | Credit used · keep reading | £0.00 | `is-low` border; no red, no alarm; a small "Top up" link inside the chip is NOT added (the chip stays one link) |
| Past zero | below £0.00 | same as Zero | £0.00 | same; the figure never shows a minus sign in the chip |

Rules: the figure counts down as the reader scrolls, by the share read (the newsroom's meter, as in the brief); an `aria-live="off"` chip, updated at most once a second, and the figure change is not animated under `prefers-reduced-motion`. The accessible name is "Reading credit £4.20, kept in this browser: your account". Tooltip (title): the one sentence above, then "Credit left: £4.20." At Zero: "Your credit is used. You can still read everything. You can top up £5 if you want to support the work." (Top-up wording as /account/ below; the chip never says "paywall", "locked" or "subscribe".) The chip is hidden on pages that cost nothing (the meter's `free` status), as today.

## The zero moment (the reader's first time the balance reaches £0.00)

One quiet line at the foot of the page, in the existing `.meter-line` (not a modal, not over the text, never blocks): "Your £5.00 is used up. You can keep reading: every page still opens. If you would like to put £5 in, you can." with one `.btn` "Top up £5" (see the top-up states) and a text link "How this works" to the explainer. Shown once per browser, then the line goes back to the normal meter line. Dismissible; the dismissal is kept in the browser.

## The top-up button (everywhere it appears: /account/, the zero line, the explainer)

- Until the Stripe Payment Link exists (waiting on Dinis): the button is a disabled-looking `.btn quiet` that reads "Top up £5: coming soon" and carries the sentence "No payment is taken yet." It must not link anywhere and must not look like a broken button (use `aria-disabled="true"`, not `disabled`, so it can still be focused and read).
- When the link exists: "Top up £5" (`.btn primary`), opens the Payment Link in the same tab, with the line under it: "One payment of £5. Nothing renews. The credit is added in this browser when you come back."

## /account/ wording

Heading: "Your reading credit".

Balance card (existing `.balance-card`): label "Balance"; amount as now; the sub line "N pages opened in this browser · £X spent" becomes "N pages opened in this browser · £X of credit used". (The word "charged" goes: nothing is charged to anyone; it is credit in the browser.)

Under the card, three short paragraphs, in this order, replacing whatever says "Nothing is charged":

1. "Pay for what you read. Every reader starts with £5.00 of credit. It goes down as you read an article, by the share of it you read: opening a page costs a tenth, and what you read on an earlier visit is not counted again."
2. "This is kept in your browser and nowhere else: no account, no cookie, no server. We do not see what you read, and your credit is not sent anywhere."
3. "When it reaches zero, you can still read everything: every page still opens. If you would like to top up, £5 puts £5.00 of credit back. A top-up is a payment to PrompTugal.news; it does not pay the writers or the sources of any page. We are watching whether readers choose to top up, and we will say what we learn."

(The last two sentences of paragraph 3 are the brief's "no claim that a top-up pays writers or sources" and Dinis's "we'll see if people pay": the page says both plainly.)

Receipts block: "No top-ups yet." stays. After a top-up: "£5.00 of credit added to this browser. Stripe emails the receipt. This page cannot check the payment." (as the newsroom's return page.)

"Your data": unchanged except the first sentence: "Everything above is in this browser's storage and nowhere else, unless you put it in your vault."

## The explainer page (/follow/ and the front page link to it)

Title "Pay for what you read". Five short paragraphs, plain: what it is (the one sentence), how the share-read count works, that it is all in the browser, that every page still opens at zero, and why we do it (to learn whether readers value what they read enough to pay, with no paywall). A single "See your credit" link to /account/. No price table on this page: prices are cl-6.dev's proposal and cl-6.accountant's check.

## Check after the build (mine, at my next wake)

375 and 1280 px, light and dark: chip fits the tools row with the other buttons (no wrap at 320); Zero and Past zero look identical and calm; the zero line never covers text; nothing on any page says "charged", "paywall", "locked" or "subscribe"; reduced-motion respected.
