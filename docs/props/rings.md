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

**Use `decl` (component 10).** It is a skinned clothing component, so it follows the
fingers, and — the part that decides it — players can actually select it.

GTA does have `p_lhand` and `p_rhand` prop slots, and an earlier version of this page
suggested rings could go there. That was wrong in practice. The common FiveM clothing
menus do not offer them: checking illenium-appearance's own source, it writes prop ids
**0, 1, 2, 6 and 7** only — labelled Hat, Glasses, Ear, Watches and Bracelets. Ids 3
(mouth), 4 (left hand) and 5 (right hand) are never written.

A ring built as a hand prop is a perfectly valid file that most players have no way to
put on. **Convert to Ear Prop** now warns when you pick one of those three slots.

If you want rings handled like jewellery rather than clothing, the wrist slots
(`p_lwrist` / `p_rwrist`) do reach everyone — you would be attaching them at the wrist
rather than the finger.

The component route is also what published ring mods actually use: they install to `accs`,
`teef` or `decl`. A component is skinned to the skeleton, so a ring weighted to the finger
bones follows the hand for free — no anchor, no menu fork, and no question about whether
other players see it.

## Rings as part of a hand set

If you are making a whole set — rings plus a bracelet — you can join them into one object
and convert it as a single **wrist** prop. That is fewer files to manage, fewer draw calls
in game, and it lands in a slot the menus actually offer. Just remember the
one-material-slot rule from [Earrings and piercings](earrings-and-piercings.md).

## Common problems

**The mirrored ring looks inside-out** — this is exactly what the button prevents. If you
mirrored by hand instead, fix it with **Fix Normals (recalc outside)**, or redo it with
the button.

**Both rings ended up on the same hand** — the add-on detects the side from where the
mesh actually sits. If the ring is centred on the body, it cannot tell. Move it onto the
hand it belongs to first, then mirror.
