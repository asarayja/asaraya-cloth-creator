# Rings

Rings are a special case for one reason: you almost always want the same ring on both
hands, and mirroring a mesh by hand gets the winding order wrong so it renders
inside-out.

## Steps

1. Select the ring.
2. Open the **Rings / hand accessories** box.
3. Tick **Both hands** if you want it on both.
4. Press **Mirror to Other Hand**.

The add-on works out which hand the ring is currently on, mirrors it across to the other,
and flips the faces back the right way so it does not render inverted.

## Which slot to use

**A component, not a prop.** `decl` (10) is the usual choice and what most published ring
mods use — but nothing forces it. `accs` and `teef` are both used in the wild, and any
component slot works if you would rather keep rings somewhere else in your own setup. Pick
the one that fits how you organise clothing.

A component is skinned to the skeleton, so a ring weighted to the finger bones follows the
hand for free. No anchor, no menu patch, and no question about whether other players see
it.

## Why not a hand prop

GTA has `p_lhand` and `p_rhand` anchors, and an earlier version of this page suggested
rings could go there. They cannot, and this add-on no longer offers those slots at all.

They were tested the whole way: a prop built for `p_rhand`, Durty Cloth Tool labelling the
slot **"unused"** and refusing it, the `.ymt` and `shop.meta` corrected by hand anyway, and
the result installed on a live server. The slot registered nothing, while the five working
slots reported their usual counts on the same ped.

That matches everything else about them — vanilla ships zero drawables on those anchors,
no clothing menu writes them, and nobody publishes one. See
[Prop slots](prop-slots.md) for the full account.

## Rings plus a bracelet

If you are making a whole set, you have two ways to go. Keep the rings as a component and
the bracelet as a `p_rwrist` prop — they are independent, so both show at once. Or join
everything into one object and convert it as a single wrist prop: fewer files, fewer draw
calls, but the rings then hang off the wrist bone rather than the fingers, which shows when
the hand moves.

If you join them, remember the one-material-slot rule from
[Earrings and piercings](earrings-and-piercings.md).

## Common problems

**The mirrored ring looks inside-out** — this is exactly what the button prevents. If you
mirrored by hand instead, fix it with **Fix Normals (recalc outside)**, or redo it with
the button.

**Both rings ended up on the same hand** — the add-on detects the side from where the
mesh actually sits. If the ring is centred on the body, it cannot tell. Move it onto the
hand it belongs to first, then mirror.
