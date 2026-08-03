# Existing garment (.ydd)

You have a finished FiveM garment and want it to fit properly and move naturally.

## Steps

1. **Build Full Body** — skip if you already have a body in the scene.
2. **Import GTA Garment (auto-skeleton)** → pick the `.ydd.xml` file.
3. Select the **Base Body first**, Shift-select the **garment**.
4. Press **Add Jiggle (keep existing)**.
5. Press **Pre-Flight Check** and fix anything marked ERROR.
6. Export the `.ydd` with Sollumz.

That is the whole job. Step 4 is where the jiggle work is finished.

## Why "Add Jiggle" and not "Auto-Weight"

A garment from the game already has good weights — it fits properly because somebody
worked on it. You want to keep those.

* **Add Jiggle (keep existing)** keeps the original weights and only adds breast jiggle
  on top. This is the right choice for an imported garment.
* **Auto-Weight (new garment)** throws the weights away and builds new ones from the
  body. Use it only when the garment has no usable weights to begin with.

If the garment has no weights at all, Add Jiggle notices and runs a full Auto-Weight for
you instead. You do not have to think about it.

## Important for running: give the body jiggle too

The garment moves now, but the body underneath does not. When the character runs, that
means the skin stays still while the fabric swings — and then the skin pokes through.

Select the body and press **Jiggle-Enable Body (uppr)**. You do this **once per body**,
not per garment.

## Fix Export Skinning

This runs automatically when you use the weighting buttons, so in the normal flow you do
not need it. The button is there as a manual safety net — for garments you set up outside
the add-on, or to double-check before exporting.

Without it, Sollumz exports the garment **unskinned**, and then it falls apart in game.

## Common problems

**The garment lost its weights on import** — you used Sollumz's own import without a
skeleton. Re-import with **Import GTA Garment (auto-skeleton)**.

**Holes at the armpits** — run [Smooth Weights](../tools/weights.md).

**Skin pokes through when the character runs** — see [Poke-through](../tools/poke-through.md).
