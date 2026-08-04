# Shoes

Shoes go in the `feet` slot (component 6). Like `lowr` with the legs, a `feet` component
**replaces** the bare feet — the file carries the whole foot, not just a shell over it.

## Steps

1. **Build Full Body**.
2. Model or import the shoe over the body's feet.
3. **Convert to FiveM Drawable** if it came from outside GTA.
4. Select the **Base Body first**, Shift-select the shoe, **Auto-Weight (new garment)**.
5. **Set Shader** → `ped.sps` for most shoes.
6. **Set Clothing Slot / Name** → `feet`, and a number.
7. **Pre-Flight Check** — it measures the heel for you.
8. Export.

## Weighting

Shoes are the simplest thing in the add-on to weight. Across 21 working reference shoes,
only three bone pairs carry meaningful weight:

| Bone | Share |
| --- | --- |
| `SKEL_L/R_Foot` | 21–40% each |
| `SKEL_L/R_Calf` | 2–37% each, more the higher the shaft |
| `SKEL_L/R_Toe0` | 8–22% each |

Auto-Weight produces this from the body without help. Boots put more into the calves
simply because more of the mesh is up there.

## Heels

This is the part worth knowing, because it is not what you would guess.

A real high heel puts the wearer on the ball of the foot. **GTA shoes do not do that.**
All 21 reference shoes keep a flat sole — every one of them tilts less than 5 mm. A heel
in GTA is the whole shoe dropped straight down, not a pose.

Measured against the bare foot the body ships with:

| Kind | Sole below the bare foot | Files |
| --- | --- | --- |
| Flat | within 8 mm | 7 |
| Low heel | 27 mm | 1 |
| High heel | 68–125 mm | 13 |

Ten of the thirteen high heels sit between 82 and 87 mm. That is a convention, not a
spread — if you are building heels, **aim for about 85 mm**.

## The high-heels flag

Dropping the sole 85 mm would put the shoe 85 mm into the ground on its own. It works
because the clothing metadata carries a **high-heels flag**, which you set on the
component in **Durty Cloth Tool**. The game compensates for the offset when that flag is
present.

Without it, the shoe sinks by exactly the heel height, and no amount of remodelling fixes
it — the geometry is already right.

This add-on does not write the clothing metadata, so it cannot set the flag for you.
**Pre-Flight Check** measures the drop and reminds you when it looks like a heel.

## What Pre-Flight tells you

Run it with the Base Body in the scene and it reports one of:

* **Flat shoe: sole +9 mm from the bare foot** — nothing to do.
* **High heel: the sole sits 85 mm below the bare foot** — set the flag in Durty Cloth
  Tool.
* **The sole sits 30 mm ABOVE the bare foot — the shoe floats** — move it down.

## Common problems

**The shoe sinks into the ground in game** — the high-heels flag is not set on the
component. That is a metadata setting, not a modelling one.

**The character floats above the ground** — the sole is modelled too high. Pre-Flight
catches this.

**The shoe stretches oddly when walking** — weights. Re-run Auto-Weight with the
**Robust** method, and see [Weights](../tools/weights.md).

**Bare ankles show above the shoe** — the shoe is a `feet` component and replaces the
whole foot, so the join with the leg is up to you. Check it with
[Pose Test](../tools/pose-test.md), selecting the trousers as an under-layer.
