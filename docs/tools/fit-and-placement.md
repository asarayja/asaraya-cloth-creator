# Fit and placement

Tools for getting a garment into the right place and the right shape on the body. Most of
them want the **body selected first** and the **garment second**.

**Select anything worn underneath too.** A `lowr` component replaces the legs and carries
the leg geometry itself, so a dress has to end up outside the *trousers*, not just outside
the skin. Shrinkwrap without them buried a test dress 24.6 mm inside the trousers across
56 vertices; with them selected, 81 vertices were lifted clear and 2 remained at 0.2 mm.

The conform itself is still done against the **body** — that is the shape a tight garment
should follow — and the under-layers are cleared afterwards. Conforming straight onto the
trousers would print their seams and creases into the garment.

## Getting it roughly right

| Button | What it does |
| --- | --- |
| **Fit External to Body** | Scales and places an imported garment onto the body, and strips the source game's rig. The first thing to try for anything from outside GTA. It matches the source rig's bone groups where it can — see [External garment](../garments/external-garment.md) |
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

## An outfit that comes in pieces

Select every piece and press the button once. They are measured and moved **together**.

That matters more than it sounds. Selecting all of them used to fit only the active one
and leave the rest behind in the source file's coordinates — on a three-piece outfit two
pieces ended up **442 mm and 1065 mm** out of place. Fitting them one at a time is no
better: each gets its own best fit and the outfit pulls apart, by 42 mm and 67 mm on the
same test.

Measuring together also fits better than any piece could alone. A choker carries `Neck`
and nothing else, a garter carries `Thigh`; neither has enough landmarks to place itself.
Between them they span the body.

Everything that follows the placement — poke-through, the hem lift — runs on every piece
too. When it did not, the active piece came out 1.0 % inside the body while the two that
were skipped sat at **79 % and 31 %**, which is the whole piece buried.

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
