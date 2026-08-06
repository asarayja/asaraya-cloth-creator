# Pre-Flight Check

Run this before every export. It is one button that reports everything wrong with a
garment, so you find problems in Blender instead of in game.

## Steps

Select the garment and press **Pre-Flight Check (before export)**.

## Reading the result

| Level | Meaning |
| --- | --- |
| **ERROR** | It will not work. Fix this. |
| **WARN** | It probably is not what you meant. Worth a look. |
| **INFO** | Worth knowing, no action needed. |

The list is sorted worst first, because the top line is the one people read.

Nothing here changes the garment — it only reports.

## What it checks

**Geometry**

* Triangle soup — every triangle separate, which comes apart the moment you weight it
* Over the triangle or vertex limit
* Vertices belonging to no face
* Zero-area faces, which are what make welding delete geometry
* A high share of open edges, which usually means single-layer fabric that GTA renders
  see-through

**Weights**

* Vertices with no weight at all — they collapse to the origin in game
* Vertex groups matching no bone — Sollumz refuses the export on these
* Helper groups left behind (`ACC_*`) — these export as bone 0 and drag those vertices to
  the pelvis
* More than 4 bone influences per vertex — GTA's hard limit, and the extras are dropped
  silently

**Materials**

* No material at all
* Several material slots on the same shader — each one becomes its own shader *and* its
  own geometry
* A material that is not a GTA shader
* No texture assigned
* A shader that is not a ped shader. Imported garments land on `default.sps`, which
  exports without complaint and looks wrong in game
* Several slots on the same shader **and** the same texture — those are redundant. Slots
  with different textures are left alone, because that is how a garment made of several
  pieces works
* No `DiffuseSampler` specifically — a material can carry a normal map and a spec map and
  still render pure white, because the diffuse is what supplies the colour

**UV maps**

* No UV map at all — no texture can be applied
* Only one UV map, when every ped shader reads two

**Naming and export**

* Nothing in the hierarchy named for a clothing slot, so the game will never find it
* No skeleton in the drawable's hierarchy, which means Sollumz exports it unskinned

## Why these checks and not others

Every test in the list is one that has actually caught a real problem. Two of six real
test dresses were triangle soups. A hand-built piercing set had only one UV map. A set of
piercings rendered white with two textures attached, because neither was the diffuse.
The list is evidence, not a wishlist.
