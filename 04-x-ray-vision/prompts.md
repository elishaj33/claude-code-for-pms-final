# 04 · X-Ray Vision — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. Last session the numbers showed you what happened: a
ping used to wait ninety seconds and now it waits sixty, people
missed pings they used to catch, and missing one counts the same as
turning one down — so four responders stopped hearing from us
altogether.

At the end of the session, type wrap up, and Claude Code saves the
prompts you wrote yourself below — not the starter prompt — updates
CLAUDE.md, and saves your work to GitHub. By Module 6 this file is a
prompt library built from your own questions.

---

### 1.
ok, can we look at the other code files to see if there is some factor in those other code files that would explain why the responders ping drop was so great?

### 2.
why do you think the pings are drying up and what is the root cause if you had to come up with an option to try to fix this

### 3.
Can we create a workflow for how the code works

### 4.
Can you tell me about supply and how that impacts availability

### 5.
1. Are there any engineering comments in the codebase worth evaluating further

### 6.
tell me more about the score for each responder and how that was hurting the four responders who lost pings over time. What about their data and this code combined, will answer how the routing or score rating should be adjusted

### 7.
There is a comment Engineering manager
Aug 14, 2:47 PM
Quick one, did the change to who gets asked first apply to responders who'd already been turning jobs down, or just new ones? Can't tell from the code and don't want to guess on this. Anyone know? 
Can you look through the data and the code and see if we can answer this question?

### 8.
Here is what we should adjust in the code so that we can help them recover
What I’d adjust

1. Charge a missed ping much less than a “no”, for example 0.03 instead of 0.12. A “no” says the responder chose not to go. A miss may just be a slow phone, and the 60s wait made misses common.
2. Reset the four’s scores to 0.5 once, when the new rule ships. Otherwise they stay at zero until they happen to get asked.
3. Revisit the weights and the 60s wait separately, once we have response times. A higher floor (say 0.3) would also cap how far anyone can be ranked down

### 9.
why do we think Marcus is asking his question? Is it because it seems like the code is targeting early misses or only some responders are getting that issue or is it all responders having that same ranking

### 10.
what does the code quietly not doing

### 11.
Which of the things in this list could impact the behavior of the system the most
