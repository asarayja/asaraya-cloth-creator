# Fit and placement

Tools for getting a garment into the right place and the right shape on the body. Most of
them want the **body selected first** and the **garment second**.

## Getting it roughly right

| Button | What it does |
| --- | --- |
| **Fit External to Body** | Scales and places an imported garment onto the body. The first thing to try for anything from outside GTA |
| **Fit to Body (rough)** | A coarser fit for when the size is clearly wrong |
| **Fit to Reference Garment** | Fits to another garment instead of to the body. If you have a FiveM garment that already sits perfectly, this usually lands closest |

## Getting it exactly right

| Button | What it does |
| --- | --- |
| **Shrinkwrap to Body** | Pulls the garment onto the body surface. Good for tight clothing, wrong for anything loose |
| **Smooth-Fit Skirt/Dress (Lattice)** | Fits skirts and dresses to the hips without squashing them flat. Use this instead of shrinkwrap for anything with volume |
| **Drape onto Body** | Physics simulation — see [Drape](drape.md) |
| **Align Sleeves to Arms** | Lines sleeves up with the arm bones when they sit at the wrong angle |

**Conform Max** limits how far a vertex is allowed to move. Set it to 0 for no limit.
Useful when most of the garment is already right and you only want the strays pulled in.

## Small fixes

| Button | What it does |
| --- | --- |
| **Snap to Body** | Moves the garment onto the body when it was imported off to one side |
| **Recenter Origin** | Puts the object origin back in the middle. Fixes odd rotation and scaling behaviour |
| **Make Visible** | Un-hides a garment that was imported hidden, or hidden by accident |
| **Detect Garment Type** | Works out whether it is a top, dress, skirt, trousers or shoes. Other tools use this to pick sensible defaults |

## Picking the right tool

* **Tight clothing** — Shrinkwrap to Body
* **Skirts and dresses** — Smooth-Fit Skirt/Dress, or Drape
* **From another game** — Fit External to Body first, then refine
* **You have a garment that already fits** — Fit to Reference Garment

## Common problems

**The garment is flat against the body and lost all its shape** — you used shrinkwrap on
something loose. Undo and use **Smooth-Fit Skirt/Dress** or **Drape**.

**It moved somewhere completely wrong** — the origin is off. **Recenter Origin**, then try
again.

**The garment disappeared** — it may be inside the body. **Push Hidden Cloth Out**, or
**Make Visible** if it was simply hidden.
