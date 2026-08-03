# External garment

You have a model from another game, from Marvelous Designer, or from a 3D store, and you
want it in FiveM.

The difference from a FiveM garment is that this one has **the wrong proportions** and
**no weights that mean anything** to the GTA skeleton. Both have to be dealt with.

## Steps

1. **Build Full Body**.
2. Import the garment into Blender the normal way (`.fbx`, `.obj`, `.blend` — whatever
   fits).
3. Select the **Base Body first**, Shift-select the **garment**.
4. **Fit External to Body** — scales and places the garment onto the body.
5. **Fit to Body (rough)** if it is still clearly too large or too small.
6. **Convert to FiveM Drawable** — turns the mesh into something the GTA format
   understands.
7. **Auto-Weight (new garment)** — the garment has no usable weights, so you build them
   from scratch here.
8. **Set Shader** → pick shader and surface. See [Shader and surface](../tools/shader-and-surface.md).
9. **Set Clothing Slot / Name** → pick the clothing slot. See [Clothing slot](clothing-slot.md).
10. **Pre-Flight Check**, fix anything marked ERROR, and export.

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
