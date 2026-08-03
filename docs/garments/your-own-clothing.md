# Your own clothing, modelled from scratch

This is the longest route, but also the one where you have full control. The add-on
covers the whole stretch from mesh to finished `.ydd`.

## Steps

### 1. Build the body

**Build Full Body**. You model on top of it, so it has to exist first.

### 2. Model the garment

Ordinary Blender work. Two things save you a lot of trouble later:

* **Model on top of the body**, not beside it. Then you do not have to move it afterwards.
* **Give the garment an inside.** GTA does not draw the back of faces, so a single sheet
  of fabric renders see-through in game. The **Add Inside (Solidify)** button handles it.

If you use sculpt tools, it is easy to drag geometry into the body without noticing. You
fix that in step 6.

### 3. Turn it into a GTA garment

**Convert to FiveM Drawable**.

This creates everything the format requires: the drawable, the drawable dictionary, the
UV maps `UVMap 0` and `UVMap 1`, and a material if the mesh has none. Anything already in
place is left alone.

### 4. Weights

Select the **Base Body first**, Shift-select the garment, and press
**Auto-Weight (new garment)**.

The method above the button is usually best on **Robust (anti-clipping)** — slower, but
much cleaner at armpits and crotch. **Fast (Data Transfer)** is quicker if you are just
testing.

### 5. Shader and texture

**Set Shader**. Pick `ped.sps` for ordinary fabric, `ped_alpha.sps` if the texture has
real transparency — lace, mesh, tulle. See [Shader and surface](../tools/shader-and-surface.md).

To see the texture on the garment while you work, use
[Preview Texture](../tools/texture-preview.md). It does not change the file.

### 6. Test and fix

The garment is now complete enough to test:

* **Pose Test (find clipping)** puts the figure in six poses and reports where the fabric
  fails. See [Pose Test](../tools/pose-test.md).
* **Fix Poke-Through** corrects places where skin comes through. See
  [Poke-through](../tools/poke-through.md).

Go back and forth between the two until Pose Test is happy.

### 7. File name

**Set Clothing Slot / Name**. Without the right name the garment simply never appears in
game, with no error to explain why. See [Clothing slot](clothing-slot.md).

### 8. Final check

**Pre-Flight Check**. Fix everything marked ERROR, consider anything marked WARN, and
export with Sollumz.
