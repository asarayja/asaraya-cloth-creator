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

You have two choices, and both are legitimate:

* **`decl` (component 10)** — the classic route for rings. It is a skinned clothing
  component, so it follows the fingers.
* **`p_lhand` / `p_rhand` (props)** — rigid, attached to the hand bone. Use this if you
  want rings handled the same way as bracelets and watches.

There is no rule forcing one over the other. If you are already building bracelets as
props, keeping rings in the same system is simpler to manage.

## Rings as part of a hand set

If you are making a whole set — rings plus a bracelet — you can join them into one object
and convert it as a single wrist prop. That is fewer files to manage and fewer draw calls
in game. Just remember the one-material-slot rule from
[Earrings and piercings](earrings-and-piercings.md).

## Common problems

**The mirrored ring looks inside-out** — this is exactly what the button prevents. If you
mirrored by hand instead, fix it with **Fix Normals (recalc outside)**, or redo it with
the button.

**Both rings ended up on the same hand** — the add-on detects the side from where the
mesh actually sits. If the ring is centred on the body, it cannot tell. Move it onto the
hand it belongs to first, then mirror.
