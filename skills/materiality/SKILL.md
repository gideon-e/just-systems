---
name: materiality
description: >
  Ranks the issues, facts, arguments, and procedural moves in a legal problem by how far
  each would move a named decision, so effort goes where the matter turns. Use when asked
  what matters, what is material, to rank or prioritize issues or arguments, or what to
  focus on, and when another skill or agent must decide where to spend effort, pages, or
  time. A thinking tool for the lawyer.
---

# materiality

## Goal

Find where the matter turns. Done is a short ranked list whose first item is the crux, each
item tied to the decision it moves, and a list of what to set aside. This is a thinking
tool for the lawyer's strategy: it ranks, and the lawyer decides. It does not assess merit
for the client, draft, or stand in for research. The ranking is strategy, so it stays with
the lawyer's work product.

It works on whatever it is given. Handed a list of issues, rank them. Handed raw facts,
name the issues plainly first, then rank; spotting and ranking are different acts, so keep
the list visible for the lawyer to check. The ranking says where time, pages, and
attention should go.

## Why the default reads junior

Models learn law from what gets written: opinions, treatises, exams. Published opinions are
selected for contested doctrine, and exams pay for every issue spotted. What a senior lawyer
weighs is mostly unwritten: verdicts, settlements, what judges skim past, what a partner
cuts. So the default weights **salience** (text, doctrine, heat), treats issues as equal
and independent, and keeps everything because cutting feels riskier than listing. Weight by
**swing** instead, and cut. Salience counts only as far as the decider runs on it, and a
jury, a mediator, or a hurried reader often does.

## Frame first

Every materiality test in the law asks one question: would this change a decision?
Summary judgment asks whether a fact might affect the outcome; securities law, whether it
would alter the **total mix**; fraud, whether it tends to influence the decider; harmless
error, whether it had substantial influence; defamation, whether it changes the **gist,
the sting**.

So materiality belongs to a frame, never to an item alone. Set the frame before ranking:

- **Goal.** What the client actually wants: money, vindication, speed, privacy, a
  reference, a relationship kept. Legal merit is one input to that goal.
- **Audience and decision.** Who decides what, by when: a judge on summary judgment, a
  jury, an arbitrator, a mediator, the other side's carrier, the client. The same fact
  ranks differently for each. Use the lawyer's decision when given; otherwise take the next
  irreversible one and say so.
- **The questions the jury will answer.** Every matter is priced against its end: the
  questions the instructions and verdict form will put to the jury, or to the judge or
  arbitrator where there is none. An item matters
  as far as it moves an answer to one of those questions, or decides whether the case
  reaches them. A settlement, a motion, and a discovery fight are each a forecast of those
  answers.
- **Truth.** What most likely happened, apart from what can be argued. A position the truth
  will not hold costs credibility on everything else.
- **Constraints.** Pages, words, minutes, money, deadlines, forum rules, the client's
  appetite for risk. Under a **budget**, materiality is opportunity cost: every point
  displaces another, and a weak point dilutes the strong ones, because a reader judges the
  whole by its worst part. A budget is a ceiling, not a target: in a ten-page brief the
  third-best argument can be the one to cut, and the pages it frees go to the best one.

When a piece of the frame is missing, ask once if the answer would change the crux;
otherwise proceed and mark that piece **assumed**.

## Rank by swing

- **Swing** is probability times magnitude: how likely the item goes against us, times how
  far the decision moves if it does. Ordinal words beat invented percentages. Ease is not
  swing: an item that is easy to argue or easy for the decider to rule on still ranks by
  its odds.
- **Total mix.** Rank the margin, not the item. Cumulative proof ranks low however vivid; a
  single point of failure ranks high however dull. A point the other side has already
  conceded or cured has no margin left: set it aside.
- **Gates.** Map what depends on what. A gate (forum, arbitration, limitations, standing, a
  dispositive element) multiplies everything behind it; an issue behind a gate is only as
  material as the gate lets it be, so resolve or price the gate first. Interdependent items
  rank as one bundle, and an item that concedes the premise of a stronger one subtracts from
  it. The crux is where most of the outcome's variance sits.
- **Proof, process, time.** A fact matters only if it can be proved, in this forum, before
  the deadline, at a cost the stake justifies. **Perishable** items (a witness leaving, a
  deadline, evidence that can be lost) rank by the cost of waiting. Irreversible before
  reversible: an argument that loses today may still need preserving, because waiver is
  permanent.
- **Burden and review.** Who must prove it, to what standard, and how much deference the
  ruling gets above. The same fact weighs differently when the other side carries the
  burden, and a ruling reviewed for discretion is won or lost below.
- **Disputed, ambiguous, unknown.** Disputed goes to the factfinder on credibility.
  Ambiguous means the rule or the meaning is unsettled. Unknown means find out, and an
  unknown ranks by the value of the answer against the cost of getting it.
- **Both seats.** Rank from the decider's seat and from the opponent's. What the other side
  fears is material to settlement whether or not it would win.
- **Story.** A fact that fits the theme the decider will carry into the room can outrank a
  stronger fact that fits nowhere.

When two items are close on swing, break the tie in this order: the gate before what sits
behind it, the irreversible before the reversible, the cheaper to act on before the
dearer.

When the swing sits outside the lawyer's focus, say so in one sentence at the top. That is
the most useful sentence this skill writes.

## Output

```
Frame: <goal> · <audience and decision, by when> · <binding constraint>.
<one sentence, only if the swing sits outside the lawyer's focus>

1. <crux> — <gate | swing | perishable>: <why it moves the decision>. Moves if: <what would change its rank>.
2. ...   (five at most)

Next: <three actions at most, ordered by swing per hour>   (only when a next step is wanted)
Set aside: <item> — <why it does not move the decision>.   (one line each)
```

The ranking is the deliverable: items in swing order, so the crux is always item 1; one
line per item, and depth only when asked. When the answer spends the whole budget, say in
one line why the last point earns its space. Every item names a fact from the record or is
marked **assumed**. Authority not checked this session carries `[unverified]`. When
another skill or agent calls this one, return the block alone; the caller decides what to
do with it.
