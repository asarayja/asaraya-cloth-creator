# Poke-through

Poke-through is skin coming through fabric. There are four tools for it, and picking the
right one matters — the broad tool applied to a narrow problem is how straps get
destroyed.

| Tool | Use it when |
| --- | --- |
| **Fix Poke-Through** | Skin comes through in several places across the garment |
| **Push Out Selected (local fix)** | One area is bad and the rest is fine |
| **Push Hidden Cloth Out** | Parts of the garment are buried inside the body |
| **Fix Jiggle Clipping (running)** | Skin comes through only when the character runs |

## Select what is worn underneath

Same rule as [Pose Test](pose-test.md), and for the same reason: a `lowr` component
**replaces** the legs and carries the leg geometry itself. Under a dress, the surface the
fabric has to clear is the trousers, not the skin they cover.

Select the **Base Body**, then anything worn **underneath**, then the garment last. Each
layer gets its own pass, outermost last, and the report says how many vertices each layer
accounted for.

Measured on a test outfit, a dress over trousers: **0** vertices needed moving against the
body, **6** against the trousers. Without the trousers selected, the tool finds nothing to
do and reports success.


## Faces, not just corners

A vertex test finds cloth that has sunk into the body. It cannot find a **face** whose
interior cuts through while all three corners stay outside — and on a coarse garment that
is most of the problem.

Measured on a 1434-vertex sweater over the shoulders and bust: the vertex pass found and
fixed everything it could see, taking the deepest breach from 18.6 mm to 1.0 mm, and the
skin showing through **did not change at all**. The cloth was passing under the shoulder
between its vertices.

So each face's centroid and edge midpoints are sampled too, and the corners are lifted far
enough to carry the whole face clear. Counting the skin actually visible inside the
garment's silhouette in a render — which is what you see — that took the sweater from
**2.27 % to 0.65 % from the front** and **1.91 % to 0.52 % from the back**, with the
patches across the shoulders and bust gone entirely.

### A corner already clear of the skin can still be lifted

The corner's own nearest point on the body and the place its face cuts through are two
different places. A cuff hanging 40 mm clear of the hand can still have the thumb coming
through the middle of a face, and judged as an absolute distance from the skin that corner
looks like it needs nothing.

Those corners are lifted where they stand instead. On a measured sweater that took faces
still cutting through from 50 to 37, and the skin visible from the front from 0.65 % to
0.50 %.

### It runs three times

Lifting one face tilts its neighbours, which can open a shallow breach next door, so a
single pass leaves work behind. On that sweater the faces still cutting through went
**120 → 76 → 69 → 63** over three rounds and then stopped moving, so three is the default.
It stops early when a round moves nothing, and seams held at 0 throughout.

### The lift is capped at a quarter of the face

A triangle laid across a curved body dips below it by roughly its own span squared over
the body's radius, so a genuine coverage breach is always small next to the face: on that
sweater, edges of 37 mm and a median dip of 2.2 mm.

A face sunk deeper than a quarter of its own size is not failing to cover the body, it is
sitting **inside** it — a placement problem, not a coverage one. One test garment arrived
with 5594 faces a median 47 mm under the skin, and lifting each corner that far inflated
the whole garment 26 mm off the body. With the cap it settles 6 mm out instead, and the
vertex pass owns the rest.


## Fix Poke-Through

Select the **body first**, Shift-select anything worn underneath, Shift-select the
**garment**, and press **Fix Poke-Through**.

It finds vertices that are genuinely inside the body and pushes them out just far enough,
then smooths the result so the surface does not end up lumpy.

Three things it does deliberately, each because of a real failure:

* **Only vertices actually inside the body are moved.** An earlier version moved anything
  close to the surface, which meant 1913 vertices moved when 162 were the problem — and
  the straps on a lace dress were wrecked in the process.
* **Neighbours share the movement.** Pushing scattered vertices out on their own leaves
  visible bumps, so the offset is spread across the surrounding surface.
* **Anything still deep afterwards gets a second pass.** Isolated vertices buried far
  inside do not come out on the first attempt.
* **Vertices sharing a point move together.** A mesh from another game is split along its
  UV seams, and pushing each side out along its own normal opens the seam into a crack —
  330 of 718 seams on one dress, the worst by 118 mm, which shredded its straps into
  ribbons.

Adjust **Minimum depth** at the bottom left afterwards if it is being too eager or too
timid.

## Push Out Selected

When only one place is wrong — a strap, a hem, one shoulder — this is the safer tool.

1. In **Edit Mode**, select the vertices in the problem area.
2. Back in Object Mode, select the **body first**, Shift-select the **garment**.
3. Press **Push Out Selected (local fix)**.

Only your selection moves, and the movement fades out over the surrounding vertices so
there is no hard edge where the fix stops.

## Push Hidden Cloth Out

For the opposite problem: fabric that has ended up inside the body and is invisible.
Common after sculpting, and after importing a garment that was fitted to a different
shape.

## Fix Jiggle Clipping

If skin only comes through while running, the cause is usually not the garment at all —
it is that the garment has jiggle and the body does not. Press
**Jiggle-Enable Body (uppr)** on the body first. If it persists, **Fix Jiggle Clipping
(running)** widens the gap specifically in the poses where the movement happens.

## It fixes the resting fit, not the pose

Worth being clear about, because the name suggests more than it does. This tool clears
the garment where it clips **standing still**. It cannot fix a breach that only happens
in a pose.

On the same test outfit, the sitting pose leaked 48 vertices at 65.6 mm before the fix and
exactly the same afterwards. Nothing was broken — the thigh swings 70° forward and simply
exits the hem. No amount of resting clearance changes that; the garment needs to be longer,
wider, or reshaped in that area with **Push Out Selected**.

## The realistic workflow

1. [Pose Test](pose-test.md) to find what is actually wrong
2. **Fix Poke-Through** for the broad problems
3. **Push Out Selected** for whatever is left, area by area
4. Pose Test again

Two or three rounds is normal. Fixing everything in one pass usually means the tool moved
more than it needed to.

## The hands are left alone

A sleeve overlapping the hand is not a defect to repair. The hand is its own component in
GTA, and the cuff of a long sleeve is meant to hang around it.

Trying to fix it anyway does not work and does damage. Pressing the button **forty times**
on a bell-sleeved sweater left the thumb through the cuff exactly as it started, while the
cuff itself was dragged further out of shape on every press — it went visibly triangular.
The reason is geometric: the hand sits *inside* the bell, so pushing cloth off the thumb
pushes it nowhere useful, and the fix never converges.

So garment vertices and faces within 110 mm of the wrist joint are skipped. With that in
place the same forty presses move the cuff **0.0 mm** and everything else settles after
about five.

**Short sleeves are unaffected** — they never reach that far.

**Gloves are the exception.** A garment with most of its geometry at the hands *is* the
hands and has to conform to them, so it is detected by shape and fixed normally.

### If the cuff really is in the thumb

That is length, not penetration. Use `Lengthen` on
[Tighten Sleeves](sleeves.md) with a negative value — on the measured sweater **−20 mm
halved** the faces meeting the hand, from 20 to 10, and −40 mm took it to 7. How far to go
is a design decision about how much of the hand the sleeve should cover, which is why it is
a slider and not automatic.

## Common problems

**Straps or thin parts got mangled** — you used the broad tool on a narrow problem. Undo,
and use **Push Out Selected** on just that area.

**The surface has bumps after fixing** — raise **Minimum depth** so shallow vertices are
left alone.
