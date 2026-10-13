# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.
  Exceptions, for the course-setup and wrap-up skills only:
  - When the student asks you to check their setup, save their work or wrap up a session, that request is their yes. You may run the GitHub command-line program installed at ~/.ccpm/gh for those checks and saves, and look in that folder to find it.
  - For a repair, first tell the student in one plain sentence what you are about to do, and act only after they say yes. Repairs may: run that GitHub program (including setting this folder's own git sign-in setting and changing this repo's visibility back to Public); copy the student's own course files into this directory from another folder on their computer (copy only; never move, edit or delete the originals); and rename something outside this directory that blocks setup, by adding "-old" to its name (never delete it).
  Outside this directory you still never write, edit or delete anything else.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

Sources: rook-wiki (About Rook, Glossary, Team directory, Releases, Q3 roadmap,
product briefs, 4.2 page comments) and 00-rook/company/notes/handoff-from-priya.docx.
Wiki state as of its last edits (team directory 2 Sep 2026; roadmap last reviewed
30 Jun 2026). Today is mid-Oct 2026. I (the user) am the new PM for Rook Dispatch,
started ~24 Aug 2026, reporting to the Director of Product.

### Company and products
- Rook Industries: coordination and provisioning software for the protective-response
  sector. Customers are independent masked **responders** and the **handlers** and
  **quartermasters** who support them. Subscription, priced per active responder.
  HQ Site Aleph; offices Berlin, Singapore, Cornish lighthouse. 241 staff.
- **Rook Dispatch** (mine): incident -> rank available responders -> ping top-ranked
  responder's phone -> taken, or turned down/missed and it moves on. Handlers use the
  web console; responders use the phone app. Monthly release train, 4.x numbering.
  Routing config ships in the release; handlers cannot adjust it at runtime.
- **Rook Supply**: gear requisitions, maintenance, field failure reports. Handlers and
  quartermasters. Shares the Responder Availability Record (Dispatch writes, Supply reads).
- **Confidentiality (hard rule):** cover identities are never stored or mapped to legal
  identities. Never design anything that assumes such a mapping, and never try to work
  out who anyone is. Read Security Policy 4.1 before touching responder records.

### People (wiki role -> name)
Comments on the wiki use roles, not names:
- Engineering manager = **Marcus Oyelaran**, EM Dispatch, Site Aleph. First stop for anything unsure.
- Staff engineer = **Wen Li**, Berlin. Built the ping-ranking logic; no doc exists, so
  learn it by talking to them. Away 14-24 Aug.
- Product designer = **Sofia Marino**, Site Aleph. Owns console and phone app; ran the September interviews.
- Support lead = **Nadia Hoffmann**, Berlin. Owns tickets; worth a standing 15 minutes.
- Director of Product = **Helen Achebe**, Site Aleph. My manager; owns roadmap and commitments.
- Data analyst = **Ravi Menon**, Singapore. Owns the numbers; weekly report on ping acceptance.
  (Priya's handover says ask the EM for numbers; the directory says Ravi. Go to Ravi.)
- **Priya Raghunathan**: previous Dispatch PM (14 months, sole PM), left 21 Aug 2026. Not reachable by default.
- Handlers named in the interview/briefs: Halloran (Sgt. Bulwark; Supply user, requisitions),
  Aunt Dot (Vesper), Mr. Ambrose (Captain Vantage), Kip (Meteor Mite, The Gale).

### Vocabulary
- **Callout**: request for a responder to attend an incident; unit of work in Dispatch.
- **Ping**: a callout offered to one responder. **Taken** / **Turned down** / **Missed**
  (ping wait ran out). Turned down and missed are recorded separately; both move it on.
- **Ping wait**: how long a ping sits before it counts as missed. Same for everyone, set in the release.
- **Acceptance rate**: share of pings taken (vs turned down or missed). Headline metric.
  Others: **time-to-accept** (median seconds ping sent -> taken); **coverage gap**
  (no available responder had the required tags; a gap is not a low acceptance rate).
- **Routing priority**: ranking score. Inputs: proximity (travel-time estimate), availability,
  capability match, recent acceptance history. Turning down or missing pings lowers the
  recent-acceptance part, so lowers later ranking.
- **Capability tags**: flight, structural-entry, hazmat-tolerant, cold-weather, aquatic,
  crowd-management, de-escalation.
- **Mutual aid**: cross-area cover; unsupported, on the Q4 exploration list.
- Supply: requisition, field failure report, service interval.

### Releases (Dispatch)
- 4.0 (7 Apr): new console nav, responder profile redesign, routing override audit log.
- 4.1 (16 Jun): proximity uses travel-time estimate; bulk callout; push delivery reliability.
- 4.2 (12 Aug): proximity weighted up vs recent acceptance history; **ping wait 90s -> 60s**;
  console filters persist; three defect fixes. Went out clean, no rollback.
- The Releases db omits deferred items. The audit log and bulk callout briefs predate 4.0/4.1,
  which shipped them, so those briefs are historical, not open work.

### Where things stand: the 4.2 problem
- Since 4.2: callout tickets ~3x normal, still elevated on 26 Aug (Nadia). Roughly two thirds
  "phone never goes off", one third "gone before I could answer".
- The one-third theme is explained by the 60s ping wait. The two-thirds theme is **unexplained**.
- Priya's read (handover and 19 Aug comment): mostly seasonal (August is soft), recovers in
  September; don't turn this into a revert-4.2 debate. That is an assertion, not data; nobody has
  checked it. The seasonal claim and the "proximity change is right" claim are hypotheses to test.
- Marcus asked on 14 Aug whether the proximity change was meant to apply equally to responders who
  have been turning jobs down; the config doesn't distinguish. Unanswered (Wen was away, then buried).
  Mechanically plausible concern: lower acceptance -> lower rank -> fewer pings, but 4.2 changed
  the weighting, so check who is losing pings before drawing a conclusion.
- Marcus and Nadia agreed (28 Aug) to regroup with me on the 4.2 picture. Don't hand me a
  conclusion; show the evidence. Real weekly acceptance numbers have not been posted anywhere I've seen.
- No written description of the ping/ranking logic exists. Priya asked me to write it.

### Roadmap (Q3, last reviewed 30 Jun, so stale)
| Item | Target | Status | Notes |
| --- | --- | --- | --- |
| Change to who gets pinged | 4.2 | Committed | Shipped |
| Ping timeout tuning | 4.2 | Committed | Shipped (90s -> 60s), presumably |
| Availability Confidence | 4.2 | Committed | Not in 4.2 notes; likely one of the items "squeezed out" |
| Requisition approval chains | 4.3 | Committed | Supply; see briefs |
| Handler phone app | Q4 | Exploring | Owner is Sofia |
| Shared cover between responders | Q4 | Exploring | Handle carefully against cover-identity rule |
All owners listed as Priya, so owner fields need reassigning. Priya flagged that I must
confirm with Helen which squeezed-out items are still Q3 commitments; that conversation
has not happened. Committed items change through Product, not directly.

### Product briefs
- **Bulk Callout** (12 Jan, Dispatch): send same callout to several responders at once;
  each still accepts individually. Shipped in 4.1; brief never got a time-to-full-coverage baseline.
- **Routing Override Audit Log** (5 Mar): log manual overrides (who, when, who instead, reason).
  Shipped in 4.0. Useful for tracing handler overrides when investigating complaints.
- **Requisition Approval Chains** (14 Jul, Supply): second approval over $2,000. The brief
  scope-creeps (bypass, dashboard, status view, replace spreadsheet): treat as one ask plus a wishlist.
- **Handler Phone App** (8 Sep): notifications, status view, one-tap contact; exploring for Q4.
  Scope tight. Motivated by Aunt Dot's request for alerts.

### Other notes
- The wiki also has Research > Customer interviews (read mid-Oct; see below) and Rook database tools.
- Priya: console filter persistence tickets are noise; don't let them eat month one.
- Working style: separate what the sources state from what is inferred; flag stale or conflicting data.

### Findings from the Rook database (pings, responders, callouts; data 29 Jun to 6 Sep 2026)
- Four of 16 responders went to about zero pings after 4.2: Farlight (Uptown), Meteor Mite (Eastgate),
  The Undertow (Harborside), Vesper (Old Town). Pre-4.2 they got 10-14 pings a week; by week of 31 Aug, 0-1.
- Not explained by low prior acceptance (69-81% vs 72-85% for the other 12) or by distance: their areas are
  among the busiest. Meteor Mite and The Gale share Eastgate and handler Kip, yet The Gale's pings rose.
- What they share: they missed pings on 12-16 Aug (Undertow 5, Farlight 3, Meteor Mite 4, Vesper 4), then a
  collapse (about 3-5 pings/wk vs 11-14; share of first pings 28% -> 9%; the other 12 rose 20-40%).
- After 12 Aug, pings to out-of-area responders rose from 14% to 39% of all pings (0% taken before, 36% since).
  This contradicts Priya's "seasonal" read, since the drop is concentrated, not spread.
- Open: what happened in September (data ends 6 Sep); actual ranking weights; no distance data, only area names.

### Updated hypothesis for 4.2 (revised mid-Oct; supersedes the earlier "60s wait then ranking" wording)
Stated: 4.2 shipped 12 Aug with a 60s ping wait (was 90s) and proximity weighted up vs recent acceptance.
Inferred: the two changes compounded. The 60s wait caused a system-wide rise in missed pings from 12 Aug; for
the four responders, who missed a much larger share of their pings, the ranking turned early misses into a lasting
loss of pings, partly by sending them out-of-area pings they can't take. Seasonality explains at most a small part
of the volume dip, not the concentration. Unproven; needs Wen Li (ranking) and response-time data.
- What changed from the earlier hypothesis: the break is exactly 12 Aug (10 and 11 Aug were clean: 0 and 1 missed;
  then 7, 12, 8 on 12-14 Aug), not "the week of 10 Aug". The wait hit all 16 responders (missed pings ~2% -> 13-21%,
  easing to 13% by week of 31 Aug), not just the four. The four missed 53% of their in-area pings vs 6% for the
  other 12: unexplained, the biggest hole. Their out-of-area pings: 0% taken, 68% missed.
- Callouts per week fell about 10-20% (138 -> 110/121/124/127), abruptly on 12 Aug, while pings/wk stayed flat (~160-175)
  and pings per callout rose 1.23 -> 1.39. Callouts with a taker: 94.5% -> 88.9%. A release should not change incident
  counts: ask Ravi/Wen whether counting changed on 12 Aug. Weekly reports should be cut at 12 Aug, not Mondays.
- Confidence: wait -> missed pings high on timing/breadth (no response-time data); ranking -> starvation moderate;
  why these four missed more unknown; seasonal mostly ruled out for the concentration.
- Would change it: response times mostly under 30s (weakens the wait); Wen saying acceptance window is long or
  proximity dominates regardless (changes ranking part); September data showing the four recovering.

### Customer interviews and support tickets (read mid-Oct)
- Interviews (2-5 Sep; Dot, Ambrose, Halloran, Kip; console-redesign research): lost callouts 3 of 4; handler can't tell a
  callout is live or which responder 3 of 4; quiet/uneven work 2; small text 2; filter silent reset, tag legend, dark mode
  1 each; Halloran's Supply complaints (requisition queue, failure reports, catalog search). Interviews state symptoms only;
  none mentions 4.2, ping wait or ranking.
- support_tickets (147, 29 Jun-7 Sep): quiet responders 30, console features 32, gear/Supply 24, saved filters 18,
  callout gone 15, account/access 14, display comfort 8, duplicate notifications 6. Nothing in the lost-callout or quiet
  groups before 12 Aug (first 12 Aug and 17 Aug); all still open. Tickets ran 5-8/wk, then 20, 27, 32, 25 (about 3-4x),
  not recovering by 31 Aug. Lost:quiet is 15:30, matching Nadia's one-third / two-thirds.
- Piles are nearly different people: Dot, Kip, Halloran filed 0 tickets, Ambrose 1; heavy filers (Desmond Okafor 21,
  Linda Pruitt 19, Simone Fischer 15, Yusuf Demir 14) were not interviewed. Worth asking Sofia/Nadia about follow-up
  calls with Desmond (The Undertow) and Linda (Farlight).
- Loud in interviews, rare in tickets: handler wanting to be told a callout is live (2 tickets, alert sound only), small
  text (2). Heavy in tickets, absent from interviews: console feature gaps, gear logistics, account/access, duplicate
  notifications. Disagreements: Halloran praises maintenance scheduling vs tickets 3054/3109 (booked marathon day);
  Ambrose's near-miss is "two weeks ago" in interview but "yesterday evening" (12 Aug) in ticket 3043.
- Caveat: several tickets repeat interview wording and one another almost verbatim, so the sources may not be independent;
  ticket counts rest on my own grouping.

### Ping checks run mid-Oct (matched peers, ping order, callouts by area)
- Matched peers: in 12-18 Aug, every responder with 4+ missed pings collapsed (Undertow 6, Farlight 4, Meteor Mite 4,
  Vesper 4); nobody with 3 or fewer did (Nightwell, Stormwrack 3 each). Looks like a threshold in the ranking: inferred, small numbers.
- Ping order: the four got 40 first pings/wk before and 11 after (-72%); the other 12 went 103 -> 112. When the four are
  pinged first they miss 28 of 40 (70%) vs 66 of 400 (16.5%) for the others. Biggest unexplained number.
- New candidate, untested: the four may be habitually slower answerers whom a 90s wait hid and a 60s wait exposes.
  Needs response times from Ravi (none in the database).
- Callouts fell in 14 of 15 areas (only Southport flat); the four's areas fell just 9-17%. Northfield (-31%) and Westbury
  (-30%), Ashgrove's and Halfmoon's areas, likely explain their milder dips. Callout types were not analysed (free text).
- Next asks: Ravi for response times (the four vs the rest, before/after 12 Aug), September data, and whether callout
  counting changed on 12 Aug; Wen for the missed-ping threshold, window, and why out-of-area pings were never taken pre-4.2.
