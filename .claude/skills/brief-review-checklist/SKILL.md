---
name: brief-review-checklist
description: Reviews a product brief against a fixed four-point checklist before it goes any further. Use when the user asks to review, check, sanity-check or "run the checklist on" a brief, PRD, one-pager or proposal, or points at a brief file or wiki page and wants it checked before sharing or sign-off.
---

# Brief review checklist

Run the same four checks on any product brief, every time. The user should not have to explain the checks again.

## Input

The brief is a file path, a wiki page, or pasted text. If the user did not say which brief, ask once. Read the whole brief before judging it.

## The four checks

For each check, give a verdict of **Pass**, **Partial** or **Fail**, then one or two lines of evidence.

1. **Owner named.** The brief names who owns it: a person or a clearly accountable role, not "the team". Quote where it says so. If the owner is a person who has left or whose role has changed, mark Partial and say so.
2. **Success measure stated.** The brief says how we will know it worked: a metric, a target or direction, and ideally a baseline and a date or review point. "Improve the experience" is a Fail. A metric with no baseline or target is Partial.
3. **Scope matches start to end.** Compare what the brief promises at the start (problem, goals, scope) with what it ends up proposing or listing (requirements, solution, next steps). List anything that appears at the end but not at the start (scope creep) and anything promised at the start that never gets picked up. Pass only if both lists are empty.
4. **Problem before fix.** The problem is explained before any solution is proposed. Note the first point where a solution appears and check that the problem and who has it are described above it, with evidence where available. A brief that opens with the solution is a Fail, even if the problem is explained later.

## Output

Use this shape:

```
Brief: <title / path>

| # | Check | Verdict | Evidence |
|---|-------|---------|----------|
| 1 | Owner named | ... | ... |
| 2 | Success measure | ... | ... |
| 3 | Scope start = end | ... | ... |
| 4 | Problem before fix | ... | ... |

Fix before it goes further:
- <one line per Partial/Fail, saying what to add or change>
```

If all four pass, say so in one line and skip the fix list.

## Rules

- Judge only what the brief says. Do not fill gaps from other documents, and do not invent an owner, metric or scope item.
- Separate what the brief states from what you infer. If you are inferring, say so.
- Do not rewrite the brief unless asked. Report, then offer.
- Keep it short. One review should fit on a screen.
