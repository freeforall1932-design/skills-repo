Working habits borrowed from a field where a wrong move destroys the
artifact you were studying: game modding, where the running game is the only
authority and every install is one bad write from being unplayable.

## Search the notes before investigating

Before opening a target, search whatever record the project keeps — field
notes, investigation logs, ADRs, closed issues, the evidence ledger of the
last look at the same problem. A prior note hands over exact versions, the
route that worked and the dead ends, and repeating a recorded dead end costs
the same as finding it the first time. Cite the note you built on; where the
notes disagree with the target in front of you, the target wins and the note
gets corrected.

## Set up a reversible lab before anything invasive

Any change that writes over something working — a migration, a wide
refactor, a binary or save you cannot recreate — starts from a snapshot
taken first: a branch, a backup directory, a copy of the profile or world.
Work happens in the copy; the original stays pristine and restorable. State
where the snapshot is and how to put it back before the first edit, not
after the first surprise. Derived or extracted material (decompiled dumps,
generated files, scratch data) stays out of the committed tree, the same way
game files stay out of a mod's repository.

## Three identical failures: change approach, don't repeat

If the same approach fails the same way three times, stop re-running it. A
fourth attempt with more force produces a more confident wrong result, not
information. Change the route — a different tool, a different seam, a
smaller question — and write down what the three failures jointly rule out
before changing: that shared shape is usually the actual finding. Retrying
an unchanged call is only justified when something outside the approach
changed, and then it is a new attempt, counted fresh.
