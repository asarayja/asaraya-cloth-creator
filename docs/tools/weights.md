# Weights

Weights are what keep a garment on the body when the character moves. Get them wrong and
the garment stretches, tears at the joints, or collapses to the floor.

## The two main buttons

Select the **Base Body first**, Shift-select the **garment**, then:

* **Auto-Weight (new garment)** — builds weights from scratch. For garments with no
  usable weights: modelled from scratch, or imported from another game.
* **Add Jiggle (keep existing)** — keeps the weights that are there and adds breast
  jiggle on top. For garments imported from FiveM, where the existing weights are good.

Choosing wrong is recoverable — Ctrl+Z — but Add Jiggle on a garment with no weights
falls back to a full Auto-Weight automatically, so you rarely have to think about it.

## The method

Above the buttons there is a method selector:

* **Robust (anti-clipping)** — checks confidence and surface direction, then fills in
  uncertain vertices from their neighbours. Slower, and much cleaner at armpits and
  crotch. **This is the default and usually what you want.**
* **Fast (Data Transfer)** — Blender's nearest-face transfer. Quick, but clips at joints.
  Fine while testing.

## Jiggle-Enable Body (uppr)

Select the body and press this **once per body**.

Without it the garment jiggles and the body does not, so when the character runs the skin
stays still while the fabric swings — and pokes through. This is the single most common
cause of "it looks fine standing still and breaks when running".

## Empty vertex groups

Weight transfer copies the body's **whole** group list, not just the groups that end up
carrying weight. Auto-weighting a pair of trousers used to leave 95 groups of which 84
were empty — the entire facial rig among them. They carry nothing and break nothing, but
they follow the garment into the export and make the group list useless for seeing what
the garment is actually bound to.

**Auto-Weight** and **Add Jiggle** now drop them automatically and tell you how many.
Jiggle bones are kept even when still empty, because a later step fills them in.

Pre-Flight Check reports leftovers on garments weighted before this, or set up outside
the add-on.

## Vertex groups from another game

A garment ripped from another game arrives wearing that game's vertex groups —
`b__L_Calf__`, `b__CAS_R_Breast__` and so on in other engines.
[Fit External to Body](../garments/external-garment.md) reads them as landmarks, which is
what makes the fit work, but they must not reach the export: Sollumz refuses a file
carrying a group that names no bone, and until then part of the garment is weighted to
nothing.

**Auto-Weight removes them**, because it has just rebuilt the skinning from the body — so
anything that is not a bone is left over by definition. It then renormalises, which is not
optional: those groups were carrying weight, and on one imported sweater the weights summed to
**0.50** after the removal. Left like that the garment would deform at half strength and
collapse toward the origin in game.

**Add Jiggle does not remove them**, because it keeps existing work rather than replacing
it. Pre-Flight will name them.

## Repair tools

| Button | Use it when |
| --- | --- |
| **Smooth Weights (fix armpit holes)** | Holes or tearing at armpits, elbows, knees |
| **Sync Seam Weights (fix split seams)** | A seam splits open because the two sides are weighted differently |
| **Make GTA-Compliant** | A vertex uses more than 4 bones — GTA's hard limit, and the extras are dropped silently |
| **Validate Weights** | Check for unweighted vertices and groups matching no bone |

## Fix Export Skinning

The weighting buttons run this automatically, so in the normal flow you never press it.

It puts the skeleton into the drawable's hierarchy, which is what makes Sollumz export
the garment **skinned**. Without it, the garment exports unskinned and falls apart in
game.

Press it manually if you set a garment up outside the add-on, or to double-check before
exporting.

## Common problems

**The garment collapses to a point in game** — vertices with no weight at all. Run
**Validate Weights**.

**Sollumz refuses to export** — a vertex group matching no bone. **Validate Weights**
names the offenders.

**Everything drags to the pelvis** — a helper group left behind. Groups beginning with
`ACC_` are not bones, so they export as bone 0. Pre-Flight Check catches these.

**Holes at the armpits** — **Smooth Weights**, or re-run Auto-Weight with the **Robust**
method.
