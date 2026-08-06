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
4. **Fit External to Body** — scales and places the garment onto the body, and removes
   the source game's rig.
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
