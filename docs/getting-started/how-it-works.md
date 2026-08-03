# How it works

The panel is laid out in the order you actually work, top to bottom. You rarely use all
of it — you follow the one row that matches what you are doing.

## The whole flow

```
1. Build Full Body            ← once per scene
2. Get the garment in         ← import, or model it yourself
3. Weights                    ← Auto-Weight or Add Jiggle
4. Shader and texture         ← Set Shader
5. Clothing slot / file name  ← Set Clothing Slot / Name
6. Pre-Flight Check           ← before you export
7. Export with Sollumz
```

Step 1 you do once. Steps 2–6 you do per garment.

## The three ways in

Where you start depends on what you have:

| Starting point | Route |
| --- | --- |
| A finished `.ydd` from FiveM | [Existing garment](../garments/existing-garment.md) |
| A model from another game or program | [External garment](../garments/external-garment.md) |
| A blank slate in Blender | [Your own clothing](../garments/your-own-clothing.md) |

Once the garment is in the scene, the rest of the flow is the same either way.

## How to select before you click

Almost every button that works on two objects wants them selected in the same order:

> **Select the body first, hold Shift and select the garment.**

The garment must be the **active** object — the one with the bright outline. If you get
an error saying something is missing, this is usually what is the wrong way round.

## Undo

Everything the add-on does is ordinary Blender work, so **Ctrl+Z** works. Tools that
change geometry (Repair Mesh, Fix Poke-Through, Drape) also have their own safety nets,
described on each page.

## Adjusting after you click

Many tools have settings that appear at the **bottom left** of the viewport right after
you run them. Fold that panel open, change a number, and the tool re-runs with the new
value. Click anywhere in the scene first and the chance is gone — then you have to run
the button again.
