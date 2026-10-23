# materiality eval: expected behavior

Two invented fixtures. In a fresh session with the skill installed, paste or point Claude
at each one. Run each on every model the skill should serve; it was tried on Haiku and
Sonnet on 2026-10-22. Grade by hand: each line below is pass or fail.

## fixture-brief.md (a ten-page opposition to a motion to compel arbitration)

Without the skill, a Sonnet run led with E, the fee-splitting argument, and filled all ten
pages. Acme's motion already offers to pay the fees, so E is close to moot. With the first
draft of the skill, Haiku led with D because the docket decides it cleanly; the line "Ease
is not swing" fixed that. Two more lines fixed the rest: a full budget
must say why its last point earns its space, and the crux is always item 1. On
2026-10-23 one Sonnet run and two Haiku runs passed every line; an earlier Haiku run had
ranked D above A, so line 4 is the one to watch on small models.

| # | Expected | Why it is there |
|---|---|---|
| 1 | A (no agreement formed) ranks first | Gate: it is the only argument that ends the motion on facts the judge cannot sever around |
| 2 | E (fee-splitting) is set aside, or ranked last, because of Acme's offer | Total mix: the record already answers it |
| 3 | C (class waiver) is set aside because Doe sues alone | Immaterial to this decision |
| 4 | D (waiver by one set of interrogatories) does not rank above A | Ease is not swing |
| 5 | The answer treats ten pages as a ceiling, or says why it fills them | Budget |
| 6 | Opens with a Frame line naming the judge and the page limit | Frame first |

## fixture.md (mediation number, three weeks out)

| # | Expected | Why it is there |
|---|---|---|
| 1 | Arbitration enforceability ranks first, as a gate on every other item | Gate |
| 2 | Poe's statement ranks in the top three and is called perishable | Perishable, single point of failure |
| 3 | The rude emails are set aside as not moving the decision | Salience trap |
| 4 | The expert deadline appears in Next or the ranking | Process and time |
| 5 | Five ranked items at most, three Next actions at most | Output shape |
| 6 | No authority asserted without `[unverified]` | Never invent authority |
