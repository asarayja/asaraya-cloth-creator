# Repairing the mesh

Some garments look perfect in Blender and fall apart the moment you weight them. That is
almost always the mesh, not the weights.

## Triangle soup

Models ripped from other games often arrive as loose triangles with no shared vertices —
every triangle is its own island. Visually identical to a proper mesh; structurally
useless, because weighting moves each triangle independently and the surface tears open.

**Pre-Flight Check** reports it as a ratio: roughly three vertices per triangle means
every triangle is separate.

### The fix

Select the garment and press **Repair Mesh (weld, keep weights)**.

It welds the duplicated vertices back together and keeps the weights that are there. If
welding would destroy real geometry, it rolls the whole thing back and tells you rather
than leaving you with a damaged mesh.

You can also do it by hand: **Edit Mode ▸ A ▸ M ▸ By Distance**.

> **Why the rollback exists.** An earlier version decided to weld based on how many
> duplicate vertices it found. That fires on every GTA file, because normal garments have
> plenty of legitimate duplicates at seams — and it deleted 3492 faces from one dress and
> 5503 from another. The trigger is now the soup ratio specifically, and the rollback is
> there in case that is still wrong.

## Merge Duplicate Groups

Vertex groups that appear twice under slightly different names. Usually the result of
joining objects that came from different sources. **Merge Duplicate Groups** combines
them.

## Fix Normals

Fabric that renders black, or inside-out after mirroring. **Fix Normals (recalc outside)**
points every face the right way.

## Add Inside (Solidify)

GTA does not draw the back of faces. A single sheet of fabric with no inside therefore
renders see-through in game — you look through the garment and see the inside of the
other side.

**Add Inside (Solidify)** gives the garment thickness so there is always a face pointing
at the camera.

**Pre-Flight Check** flags this when a large share of the mesh's edges are open, which is
what single-layer fabric looks like from the inside.

## Common problems

**Repair Mesh says it rolled back** — welding would have destroyed geometry, so it did
not. The mesh is untouched. The problem is probably not a triangle soup; run Pre-Flight
Check and read what else it reports.

**The garment got holes after welding** — undo. The distance threshold was too generous
for this mesh; weld by hand with a smaller distance in Edit Mode.
