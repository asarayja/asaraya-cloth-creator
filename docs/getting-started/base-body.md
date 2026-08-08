# Base Body — build the body first

Almost everything in the add-on measures against a body. Weights are copied from it,
jiggle comes from its skeleton, and poke-through is measured against its skin. **Build it
before you do anything else.**

You do this **once per scene**, not once per garment.


## What it looks like

The body comes out **plain grey**, with one simple material on it.

That is deliberate. The imported body arrives with GTA's `ped.sps` materials, and with
their textures missing it renders **solid black** in Material Preview and Rendered — a
silhouette you cannot read at all. Solid shading looks fine, which is why it is easy to
miss until you switch shading mode and the ped disappears.

Filling the empty texture slots with a grey image was tried and does not fix it: the torso
and head stayed black while the legs went grey. One plain Principled material renders the
whole body evenly, and it behaves the same on Linux and Windows because nothing has to be
found on disk.

Nothing is lost by this. The base body is a weight source and a surface to measure
against — it is never exported and never seen in game, and everything the add-on measures
reads geometry, not materials.


## Steps

1. Choose **Female** or **Male** at the top of the panel.
2. Press **Build Full Body**.

That is all. You get a complete body with a skeleton — torso, head, legs, feet and hands,
assembled from the original GTA parts that ship with the add-on.

## What you get

* An object called **Base Body**
* A skeleton called **ACC_Skeleton_F** or **ACC_Skeleton_M**
* On the female body: **breast jiggle is already set up**

Set **Jiggle Strength** in the panel **before** you press the button. The default suits
most cases; raise it for more movement.

## About the body shape

The torso is the original `uppr_015_r` from the game — stock breast size, exactly what a
player has by default. That is deliberate: clothing you make should fit what people
actually have.

If you want a different shape, import your own `uppr` file and use that as the body
instead. Everything else in the add-on works the same way.

## Importing a garment straight after

The **Import GTA Garment (auto-skeleton)** button sits right below, because that is the
most common next step. It imports a `.ydd.xml` together with the bundled skeleton, so the
garment keeps its original weights.

> **Use this button, not Sollumz's own import.** Import without a skeleton and the
> garment loses its weights — and then it no longer fits the body.

## Common problems

**"No armature found"** — you have not built a Base Body yet, or it has been deleted.

**The garment sits beside the body** — see [Fit and placement](../tools/fit-and-placement.md).
