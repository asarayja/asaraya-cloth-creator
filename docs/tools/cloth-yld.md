# Cloth physics (.yld)

GTA can simulate a garment in-engine, so it moves on its own instead of only following
the bones. That is what a `.yld` file is. It is the right choice for long skirts, coat
tails and anything meant to flow.

## Steps

1. Select the garment.
2. Press **Generate Cloth Pin Weights**.
3. Set the shader to **`ped_cloth.sps`** — see [Shader and surface](shader-and-surface.md).
4. Export the `.yld` alongside the `.ydd`.

## What pin weights are

The simulation needs to know which parts of the garment are held in place and which are
free to move. The waistband of a skirt is pinned; the hem is not. **Pin Distance** in the
panel controls how far down the pinned region reaches.

Pin too little and the garment slides off the body. Pin too much and it barely moves.

## When not to use cloth

Cloth physics costs performance and adds a file to manage. For most clothing —  tops,
trousers, jackets, tight dresses — ordinary weights plus jiggle look fine and cost
nothing. Use `.yld` for garments where flow is the point.

## Common problems

**The garment slides off in game** — not enough pinned. Raise **Pin Distance**.

**It barely moves** — too much pinned. Lower **Pin Distance**.

**Nothing simulates at all** — the shader is not `ped_cloth.sps`, or the `.yld` was not
exported next to the `.ydd`. Both are required.
