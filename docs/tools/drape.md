# Drape onto Body

Lets the fabric fall onto the body with a physics simulation, instead of you pushing
vertices around by hand. Good for skirts, dresses and anything loose.

## Steps

1. Select the **Base Body first**, Shift-select the **garment**.
2. Press **Drape onto Body (simulate)**.

The top of the garment is pinned so it does not slide off, the body is set up as a
collider, and the simulation runs for a set number of frames. The result is applied as
real geometry.

## Adjusting it

Open the panel at the **bottom left** of the viewport right after running:

| Setting | What it does |
| --- | --- |
| **Frames** | How long the fabric falls. More frames settle further |
| **Pin fraction** | How much of the top is held in place. Raise it if the garment slides down, lower it if the shoulders stay too stiff |
| **Stiffness** | How much the fabric resists stretching. High for structured cloth, low for silky drape |

## When to use it

Drape is at its best on a garment that is roughly in the right place but hangs wrong — a
skirt that floats away from the hips, a dress that ignores the waist. It is not a
substitute for fitting: if the garment is the wrong size, use
[Fit and placement](fit-and-placement.md) first.

## Garments from other games

A mesh ripped from a game is split along its UV seams — two vertices on the same point
with no edge between them. The cloth solver pulls along edges, so each side of a seam fell
on its own and the garment came apart: measured on a Sims dress, **395 of 718 seams
opened, the worst by seven metres**.

Drape now runs the simulation on a welded stand-in and writes the result back onto the
original vertices, so the garment's own topology is never touched. Seams stay shut.

Binding the duplicates with zero-length springs was tried first and was worse. The seams
held perfectly — zero of 718 opened — while the skirt exploded into a heap of intersecting
shards, because a spring of no length at high stiffness produces absurd forces. One number
passing is not the same as the thing working.

## A note on self-collision

Blender's cloth solver has a self-collision option, and turning it on is the single
fastest way to destroy a drape. With it enabled, garments in testing ended up roughly
twenty times further out of place than with it off — everything else being identical.

The add-on keeps it off deliberately. If you build your own cloth setup outside the
add-on and the result explodes, this is the first thing to check.

## Common problems

**The garment slid off the body** — raise **Pin fraction**.

**The fabric looks shrink-wrapped and flat** — lower **Stiffness**, or use
**Smooth-Fit Skirt/Dress (Lattice)** instead, which keeps volume.

**It went straight through the body** — the body was not selected first, so there was no
collider. Select body, then garment.
