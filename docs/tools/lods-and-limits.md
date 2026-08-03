# LODs and limits

## Reduce Polys

GTA has limits on how heavy a garment can be. Models made for film, or ripped from other
games, are routinely far over them.

Select the garment and press **Reduce Polys (FiveM limits)**. It brings the mesh under the
triangle and vertex limits while preserving the shape as far as it can.

**Pre-Flight Check** tells you whether you are over, and by how much, so you know whether
you need this at all.

Reducing polygons loses detail. If the garment has fine work you want to keep, it is
often better to reduce by hand with a Decimate modifier where you can control which parts
lose detail and which do not.

## Fill Empty LODs

A drawable has several levels of detail — high, medium, low, very low — and the game picks
one based on how far away the character is. If an LOD is empty, the garment simply
disappears at that distance.

Select the garment and press **Fill Empty LODs**. It generates the missing levels from the
high-detail mesh.

If a garment has only one LOD it still works, but the game renders full detail at every
distance, which costs performance for no benefit. Pre-Flight Check reports this as INFO.

## Common problems

**The garment vanishes when you walk away from it in game** — an empty LOD. Run
**Fill Empty LODs**.

**The garment looks blocky at a distance** — that is the LOD working as intended. If it is
too aggressive, delete the generated LODs and make them by hand with lighter decimation.

**Reduce Polys ruined the shape** — undo, and decimate by hand instead. Automatic
reduction cannot know which details matter.
