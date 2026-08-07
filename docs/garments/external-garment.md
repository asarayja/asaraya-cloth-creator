# External garment

You have a model from another game, from Marvelous Designer, or from a 3D store, and you
want it in FiveM.

The difference from a FiveM garment is that this one has **the wrong proportions** and
**no weights that mean anything** to the GTA skeleton. Both have to be dealt with.

## Steps

1. **Build Full Body**.
2. Import the garment into Blender the normal way (`.fbx`, `.obj`, `.blend` — whatever
   fits).

   Opening the source file and building the body **into** it works just as well, if the
   garment is already set up there. **Fit External to Body** removes the source rig for
   you either way — a Sims dress arrives bound to a 165-bone rig of its own, and leaving
   it would mean the garment is deformed by two skeletons at once after weighting.
3. Select the **Base Body first**, Shift-select the **garment**.
4. **Fit External to Body** — scales and places the garment onto the body, removes the
   source game's rig, and clears the body out of the fabric.
5. **Convert to FiveM Drawable** — turns the mesh into something the GTA format
   understands.
6. **Auto-Weight (new garment)** — the garment has no usable weights, so you build them
   from scratch here.
7. **Set Shader** → pick shader and surface. See [Shader and surface](../tools/shader-and-surface.md).
8. **Set Clothing Slot / Name** → pick the clothing slot. See [Clothing slot](clothing-slot.md).
9. **Pre-Flight Check**, fix anything marked ERROR, and export.

## It uses the source game's rig, if the garment still has it

A garment ripped from another game almost always arrives with that game's vertex groups
still on it — `b__L_Calf__`, `b__Spine1__`, `b__CAS_L_Breast__` for The Sims 4. Those
groups are the best fitting information available, because they say which body part every
vertex belongs to. A bounding box cannot know that.

**Fit External to Body** translates those names to GTA's, matches each shared bone between
the garment and the body, and solves for the scale, rotation and position that line them
up. It falls back to the old bounding-box method when a garment has no usable groups, and
the report tells you which it used.

The difference on three real Sims 4 garments, measured as the median distance from the
garment to the body surface:

| Garment | Bounding box | Bone groups |
| --- | --- | --- |
| Bikini set | 63 mm | **24 mm** |
| Dress | 67 mm | **13 mm** |
| Dress, full length | 85 mm | **21 mm** |

### Placing it is only half the job

A garment can be scaled and positioned perfectly and still have the body straight through
it, because the figure it was made for is a different shape. Measured on the same three
garments right after a good-looking fit, the share of garment vertices sitting **inside**
the body was 38%, 55% and 55% — the skirt collapsed onto the legs, the body showing
through the front.

So the button finishes the job: after placing the garment it pushes the body out of the
fabric. That takes those figures to 1%, 3% and 3%, with nothing deeper than a millimetre.

This is worth knowing about because the obvious way to measure a fit — distance from the
garment to the nearest point on the body — cannot see the problem at all. A garment buried
13 mm inside the body scores exactly the same as one sitting 13 mm outside it. The
measurement has to be signed.

### Meshes from a game are split along their seams

This is the single thing that most often destroys a garment, and it is invisible until it
happens.

A game stores UVs per vertex, so wherever the texture has a seam the mesh carries **two
vertices on the same point with no edge between them**. Across the Sims garments measured
for this add-on that runs from 21% of the mesh to **100%** of it. Nothing about the vertex
or face count reveals it.

Any tool that moves vertices then moves each side of a seam separately, and the seam opens
into a crack. Before this was handled, clearing the body out of a dress split 330 of its
718 seams, the worst by 118 mm — the straps came apart into ribbons.

**Fit External to Body**, the poke-through tools and **Drape** now all keep coincident
vertices together. Measured across 47 meshes, female and male: **zero** seams opened, and
no topology changed.

Coincident vertices are found by proximity rather than by a rounded coordinate. Rounding
looks equivalent and is not: a transform leaves about a ten-thousandth of a millimetre of
float drift, and two points either side of a rounding boundary land in different buckets.
On a male t-shirt that let 2 of 128 seams through, which opened by 8.5 mm.

### One outfit in several pieces

The Sims often splits an outfit — trousers and a belt, a top and its sleeves. Fit them
separately and they drift apart: a belt fitted on its own landed **161 mm** above the
trousers it belongs to, and 33 mm too tight, because a thin band carries too few bone
groups to fit reliably.

Join the pieces with **Ctrl+J first**, then fit once. The same belt then sat 4.5 mm out.

This applies to any file that opens with several objects — one male outfit arrived as
seven, including two four-vertex scraps that landed 160 mm off the body on their own.
Joined first, they inherit the main garment's placement and the problem disappears.

The join keeps one material per piece, so each keeps its own texture — that is normal for
GTA clothing, and Pre-Flight will confirm it rather than telling you to merge them.

### The last few millimetres are yours

The landmark fit lands within a few millimetres at every joint it can measure, and that is
not always the same as looking right — a least-squares fit leaves a small residual by
construction. On one sweater it read as the neck and cuffs sitting a touch low and the hem
a touch short, while the bust was exactly where it belonged.

**Nudge up** and **Size** in the redo panel (press **F9** straight after fitting) are the
last word. They re-apply without re-running the fit, so you can dial a number in and watch
it move.

**Size scales about the chest, not the hem.** That is deliberate: the bust is the landmark
the fit gets right and the one you notice when it is wrong, so growing the garment raises
the neck, lengthens the sleeves and drops the hem while leaving the chest alone. On that
sweater, 107% raised the neck 19 mm and dropped the hem 28 mm while the bust moved 3 mm.

Scaling about the hem was tried first and is wrong for the same reason — it lifts the bust
off the body.

What the fit still cannot do is change the garment's shape. A bandeau top cut for a
slimmer figure will sit below a larger bust however well it is placed; that is sculpting
or [Drape](../tools/drape.md), not fitting.

### About the scale

The scale estimates tell the same story. The bounding box guessed 1.64, 1.69 and 1.03 for
the three — wildly inconsistent, because a bikini's box says nothing about how tall its
wearer is. Matching bones gave 1.19, 1.02 and 0.91, which is what you would expect between
two human figures.

Why a bikini defeats a bounding box is worth spelling out: the box of a bra and briefs
tells you nothing about the body, and the garment arrives a metre away from where the body
is, so there is no overlap to measure against either. Bone names have neither problem — a
vertex in `Spine1` belongs at the body's `Spine1` whatever the scale or the origin.

## When it still does not fit

Steps 4 and 5 do the rough work. If it is nearly right but not quite:

* **Fit to Reference Garment** — if you have a FiveM garment that already fits perfectly,
  use that as the template instead of the body. This often lands closest.
* **Drape onto Body** — let the fabric fall into place with physics. See [Drape](../tools/drape.md).
* **Smooth-Fit Skirt/Dress (Lattice)** — for skirts and dresses that should follow the
  hips without being squashed flat.

## If the mesh is a "triangle soup"

Models ripped from other games often arrive as loose triangles with no connected surface.
It looks perfectly fine in Blender, but comes apart the moment you weight it.

**Pre-Flight Check** detects this and tells you. The fix is
[Repair Mesh](../tools/repair-mesh.md).

## Too many polygons

Models built for film, or for other games, are often far too heavy for GTA.
**Reduce Polys (FiveM limits)** brings them under the limits. See
[LODs and limits](../tools/lods-and-limits.md).
