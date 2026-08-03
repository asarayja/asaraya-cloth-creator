# It fits wrong or falls apart in game

## It collapses into a point

Vertices with no weight at all. They end up at the origin, which drags the whole garment
into a spike.

Run **Validate Weights**, then **Auto-Weight (new garment)**.

## It falls apart into loose pieces

Two possible causes:

**Exported unskinned.** Sollumz needs the skeleton in the drawable's hierarchy. Press
**Fix Export Skinning** and export again.

**Triangle soup.** The mesh was never properly connected, and weighting pulled it apart.
See [Repairing the mesh](../tools/repair-mesh.md).

## Everything is dragged to the pelvis

A helper vertex group left behind. Groups beginning with `ACC_` are not bones, so they
export as bone 0 — which is the pelvis.

**Pre-Flight Check** names them. Delete them and export again.

## Skin comes through the fabric

See [Poke-through](../tools/poke-through.md). If it only happens while running, the cause
is usually that the body has no jiggle — press **Jiggle-Enable Body (uppr)** on the body.

## Holes at the armpits or knees

Weights that change too abruptly across a joint. Run
**Smooth Weights (fix armpit holes)**, or re-run Auto-Weight with the **Robust** method.

## A seam splits open

The two sides of the seam are weighted differently. **Sync Seam Weights (fix split
seams)**.

## The garment is see-through

GTA does not draw the back of faces, so single-layer fabric shows straight through. Run
**Add Inside (Solidify)**.

If instead it is meant to be sheer, the shader matters — see
[Shader and surface](../tools/shader-and-surface.md).

## It never appears in game at all

Almost always the file name. GTA finds clothing by name, and a wrong name produces no
error, just nothing.

Run **Set Clothing Slot / Name** — and note that renaming the file on disk is not enough,
because the name is also stored inside the file. See
[Clothing slot](../garments/clothing-slot.md).

## It disappears at a distance

An empty LOD. Run **Fill Empty LODs**. See [LODs and limits](../tools/lods-and-limits.md).

## It lost its weights on import

You imported through Sollumz without a skeleton. Re-import with
**Import GTA Garment (auto-skeleton)**, which brings the skeleton along so the weights
survive.
