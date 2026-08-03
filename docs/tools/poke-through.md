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

## Fix Poke-Through

Select the **body first**, Shift-select the **garment**, and press **Fix Poke-Through**.

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

## The realistic workflow

1. [Pose Test](pose-test.md) to find what is actually wrong
2. **Fix Poke-Through** for the broad problems
3. **Push Out Selected** for whatever is left, area by area
4. Pose Test again

Two or three rounds is normal. Fixing everything in one pass usually means the tool moved
more than it needed to.

## Common problems

**Straps or thin parts got mangled** — you used the broad tool on a narrow problem. Undo,
and use **Push Out Selected** on just that area.

**The surface has bumps after fixing** — raise **Minimum depth** so shallow vertices are
left alone.
