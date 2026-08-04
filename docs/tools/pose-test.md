# Pose Test

Finds clipping before the game does. It puts the figure through six poses and reports
where skin comes through the garment.

## Steps

1. Select the **Base Body first**.
2. Shift-select anything worn **underneath** — for a dress, the `lowr` trousers.
3. Shift-select the **garment** last, so it is the active object.
4. Press **Pose Test (find clipping)**.

You get a report like:

```
Worst: Legs forward (sitting), 59.6 mm through (46 vert(s))
Torso bent: 55 covered vert(s) come through, worst 57.7 mm
Arms raised: 1 covered vert(s) come through, worst 16.2 mm
Breast spring (running): clean
```

The poses cover sitting, bending, raising and swinging the arms, and the breast movement
that happens when running — the situations where garments actually fail.

## Reading the numbers

The test only counts vertices that are **covered when standing still** and **exposed in
the pose**. That is the definition that matters: a bit of skin that was always visible is
not a bug, and a bit that is only visible while sitting is.

The millimetre figure is how far the worst offender comes through. As a rough guide:

| Reading | What it means |
| --- | --- |
| `clean` | Nothing to do |
| Under about 10 mm | Minor. Often not visible in play |
| 10–60 mm | Real clipping. Worth fixing |
| Over 100 mm | Something structural is wrong, not just tight fabric |

## Select what is worn underneath

This changes the answer, and leaving it out is how a broken garment reports clean.

A `lowr` component **replaces** the legs — the file carries the leg geometry itself,
which is why every lowr file measured for this add-on runs from hip to ankle. So under a
dress, the surface that actually breaks through is the trousers' legs, not bare skin. The
bare legs are not even visible in game; the trousers cover them.

Measured on a test outfit, the same dress in the sitting pose:

| Selection | Result |
| --- | --- |
| Body + dress | **clean** |
| Body + trousers + dress | **5 vertices, 13.7 mm through** |

The report names which layer is at fault, so you know whether to change the dress or the
trousers.

## The garment must be bound to the Base Body

This is the one thing that makes the numbers meaningless if it is wrong. If the garment
is still bound to an armature it came in with, rather than to your Base Body, the test
poses one and measures the other — and reports enormous numbers that mean nothing.

The add-on checks this and warns you. If you see the warning, re-run the weighting step
with the Base Body selected first.

## Fixing what it finds

* **Fix Poke-Through** for the general case — see [Poke-through](poke-through.md)
* **Push Out Selected** when only one area is bad and you do not want to touch the rest
* **Fix Jiggle Clipping (running)** specifically for the breast-spring pose
* Sculpting by hand, then re-running the test

Expect to go around this loop a few times. Fix, re-test, fix again.

## Common problems

**Everything reads roughly the same number** — that is the sign the garment is bound to
the wrong armature. See above.

**The figure is left in a pose afterwards** — press **Ctrl+Z**, or set the rig back to
rest position.
