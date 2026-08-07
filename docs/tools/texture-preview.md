# Preview Texture

See a texture on the garment while you work, without touching what gets exported.

## Steps

1. Select the garment.
2. Press **Preview Texture** and pick a `.png` or `.dds` file.
3. Switch the viewport to Material Preview to see it.

To remove it, press the **X** next to the button.

## Why it is a separate button

Simply swapping the image on the material's texture node changes the exported file. GTA
records the texture name, and that name is derived from the file path — so pointing the
node at a different image silently changes what the export references.

Preview Texture avoids this entirely by adding a node of its own, named `ACC_Preview`,
which feeds the viewport only. Nothing in the export path is touched.

**Pre-Flight Check** notices when a preview is active and says so as INFO, so you never
mistake it for a real texture assignment.

## What it is good for

* Checking a texture lines up with the UVs before committing
* Trying several colourways quickly
* Showing someone what the garment will look like

## What it is not

It is **not** a texture assignment. When the garment is finished you still have to assign
the real texture — see [Assigning textures](textures.md), which does the diffuse, normal
and spec in one go.
