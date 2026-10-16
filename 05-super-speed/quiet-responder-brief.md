# Quiet-responder recovery — product brief (one-pager)

Rook Dispatch · for Helen Achebe (Director of Product) · from the Dispatch PM · mid-Oct 2026 · DRAFT, not for build yet

**What Helen asked for:** what we would build instead of quietly changing a number, seen from the person it happens to. Something a handler like Kip would notice, and something a responder who has gone quiet would feel differently about.

---

## The problem, in one paragraph

Since 4.2 (12 Aug), four of 16 responders went from 10-14 pings a week to 0-1: Farlight, Meteor Mite, The Undertow, Vesper. Each missed 4-6 pings in the first week after the ping wait dropped from 90s to 60s. The ranking then pushed them down, and the code gives no way back up except being asked and saying yes. When they *are* pinged first they miss 70% (28 of 40) vs 16.5% for everyone else. **Stated:** the 4.2 changes and the numbers above. **Inferred:** that the ranking is what turned early misses into a lasting loss of pings. Wen Li has not confirmed this, and we have no response-time data.

## Who it is for

**1. The responder who has gone quiet** (Meteor Mite, Vesper, The Undertow, Farlight). Their phone sits silent for days. They have done nothing they chose; they missed pings under a wait that got 30 seconds shorter. They cannot see why, and nothing they do changes it.

**2. The handler watching them** (Kip, Aunt Dot, and the handlers of the other two). Kip has two cards on one screen: Meteor Mite "texting me all week asking if something's broken", The Gale "hasn't stopped". Kip's words: "I just want it to look less like a coincidence." Aunt Dot cooks for "whoever's home" and can't say why.

*Also affected, not the target:* handlers of the other 12, who lost callouts to a missed ping (13 tickets). Their ask, a fair race, is a separate fix (the 60s wait).

## What changes for them once it exists

**For the quiet responder**
- A missed ping no longer counts the same as turning one down. A slow phone is not a "no".
- A missed ping on an **out-of-area** ping doesn't count against them at all. Those pings were never taken before 4.2 (0% taken, 68% missed since) and caused 51% of the four's lost points in the replay.
- A responder already pushed to the bottom is put back at the middle (neutral) starting point once, at release, and is pinged again on the next callouts in their area. They don't have to do anything or be asked.
- Success to them looks like: the phone goes off again within days, and one missed ping doesn't send them quiet for weeks.

**For the handler**
- An alert is raised when a responder has had no pings for 7 days (the threshold is a proposal), and Dispatch starts recording how long each responder takes to answer. Today neither is recorded.
- The coverage card says plainly when a responder has gone quiet and why, e.g. "No pings for 9 days. Recent missed pings are holding this responder's ranking down." Kip then has a true answer for Meteor Mite besides "hang in there".
- While a callout is live, the console shows who has the ping and how long they have left, and **who is next if it times out or is turned down**, with the order after that. Today a handler can't see where a ping goes next, and the database records who was pinged but not the ranking. The order is fixed when the callout comes in.
- It is information only. Handlers still can't change routing at runtime.
- *Design is a proposal.* Sofia Marino owns the console and should shape the wording and where it sits. No such flag exists today: the code never records response times or logs score changes, so this needs a small engineering ask too.

## What it deliberately does not do

- **Does not change the 60s ping wait.** Not touched until we have response times from Ravi Menon. If the four are simply slower answerers, 60s is the real problem and this brief only treats the symptom.
- **Does not change the ranking weights** (proximity 0.60 / acceptance 0.25 / skills 0.15). 4.2's proximity change was long requested; this brief does not reopen it or revert 4.2.
- **Does not guarantee anyone a turn** or set a quota of pings per responder.
- **Does not let handlers tune routing**, and does not use or infer who anyone is. Cover identities only; nothing here assumes a mapping to legal identities (Security Policy 4.1).
- **Does not stop out-of-area pings from being sent**, or explain why they were never taken before 4.2. It only stops a miss on one from counting against the responder. Open question for Wen.
- **Does not rely on easing scores back toward neutral over time.** In the replay, easing alone did not lift the four. At most it is a safety net, and it answers the 2019 TODO only in part.
- **Does not address** the console wishes from the interviews (dark mode, per-responder alert sounds, Aunt Dot's phone alerts). Those belong to the Handler Phone App and console briefs.
- **Not a one-line config change.** The draft code fix (miss penalty 0.03 plus a reset) is local and untested, and is one part of this.

## How we will know (proposed, to agree with Ravi)

| Measure | Baseline | Target |
| --- | --- | --- |
| Responders with zero pings in 14 days | 4 of 16 (week of 31 Aug) | 0 |
| Weekly pings for the four | 0-1 (was 10-14) | back toward 10-14 within 4 weeks |
| First-ping share for the four | 28% before, 9% after | back toward 28% |
| *Guardrail:* overall acceptance and time-to-accept | cut at 12 Aug, not Mondays | no worse |
| *Guardrail:* The Gale's weekly pings (Kip's other responder) | rose after 4.2 | not carrying more of the load than it should |

Replay of 12 Aug-6 Sep pings: cheaper misses alone lifts the four to about 0.5-0.6 on the acceptance score, and so does ignoring out-of-area pings alone; both together reach about 0.84. A fresh start alone does not help, and neither does easing scores back toward neutral. An approximation with real outcomes but not real travel times.

## Options to decide (reasoned, not tested)

- **Grace window for late answers:** keep a ping answerable until someone else takes it. Aimed at the "gone before I could answer" tickets (about a third). Needs Wen.
- **Daily loss cap:** no responder loses more than a set number of points in a day, so one bad evening can't send anyone to the floor.
- **Delivery check:** the code never checks that a push arrived. "Phone never goes off" is two thirds of the tickets and is still unexplained.

## Rollout

- Who runs the one-off reset (`reset_to_neutral`), and when. Start with the four quiet responders.
- Confirm that scores survive a restart. They are held in memory only, so the fresh start could be wiped.
- A way to switch the change off.
- Baselines cut at 12 Aug, not Mondays, and a check on whether callout counting changed that day.
- Availability Confidence was a committed Q3 item that never shipped. Helen needs to say whether it is still owed. Gear-away status, time zone and missing leave status (tickets 3035, 3050, 3116, 3143) may also change who counts as available.

## What we don't know yet (and who answers)

- Do the four answer slowly, or does the phone not alert them? **Ravi Menon** (response times, September data, whether callout counting changed on 12 Aug).
- Is there a miss threshold in the ranking, and do scores survive a restart? **Wen Li**, plus Marcus's 14 Aug question about whether the 4.2 change was meant to apply to responders who turn jobs down. Still unanswered.
- What happened after 6 Sep: do the four still sit at zero? **Ravi Menon.**
- **Assumption in the prototype:** the live ping names the responder's handler ("Callout from your handler: Kip"), and the idle phone screen shows "Your handler". Nothing in the wiki or code says what the phone shows today, and Dispatch ranks and sends pings, not the handler personally. **Sofia Marino** to confirm.
- Does the wording on the card help Kip? **Sofia Marino**, with a follow-up call with Kip and Aunt Dot via Nadia Hoffmann.
- The 2019 TODO in `history.py` (should scores ease back toward neutral on their own?) is the "come back to it" Helen mentions. This brief answers part of it: a one-off reset now, a decision on automatic easing after we see September.

## Decision asked of Helen

Agree that this is the thing we build, in this scope, with the 60s wait explicitly left for a second step once response times arrive. Then Marcus and Wen review the code, and Sofia sketches the card.

*Next for Helen: a clickable mock of the coverage card (Kip's view) and the responder's phone, if you want it.*
