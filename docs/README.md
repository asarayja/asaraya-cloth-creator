# Asarayja Cloth Creator

A Blender add-on that gets clothing, jewellery and props ready for GTA V and FiveM.

It handles the parts of the job that otherwise require knowing the format by heart:
weights that keep a garment on the body, jiggle that follows movement, the right file
name for the clothing slot, the right shader, and the prop format for earrings and
bracelets.

## What do you want to do?

| You have | You want | Start here |
| --- | --- | --- |
| A finished FiveM garment (`.ydd`) | It to fit properly and move | [Existing garment](garments/existing-garment.md) |
| A model from another game or 3D program | To get it into FiveM | [External garment](garments/external-garment.md) |
| Nothing yet | To build clothing from scratch | [Your own clothing](garments/your-own-clothing.md) |
| Hair | It to move instead of being welded to the skull | [Hair](garments/hair.md) |
| Earrings or piercings | Them to sit in the ear | [Earrings and piercings](props/earrings-and-piercings.md) |
| Rings | Them on both hands | [Rings](props/rings.md) |

## First things first

If you have not installed the add-on yet, start with [Installation](getting-started/installation.md).
If you are unsure about the order of things, read [How it works](getting-started/how-it-works.md) —
that page shows the whole flow on one screen.

## One rule that solves most problems

**Build a Base Body first.** Almost everything in the add-on measures against the body:
weights are copied from it, jiggle comes from its skeleton, poke-through is measured
against its skin. With no body in the scene, most buttons will simply tell you one is
missing.

See [Base Body](getting-started/base-body.md).
