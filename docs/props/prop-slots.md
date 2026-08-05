# Prop slots

Props are rigid accessories attached to a bone: hats, glasses, watches, bracelets,
earrings. They are not skinned, so they do not deform — they follow the bone exactly.

## The slots

| Slot | Bone | What it is for |
| --- | --- | --- |
| `p_head` | `SKEL_Head` | Hats, caps, helmets, headwear |
| `p_eyes` | `SKEL_Head` | Glasses, sunglasses, goggles |
| `p_ears` | `SKEL_Head` | Earrings, ear piercings |
| `p_mouth` | `SKEL_Head` | Masks, cigarettes, mouthpieces |
| `p_lwrist` | `RB_L_ForeArmRoll` | Watches (left wrist) |
| `p_rwrist` | `RB_R_ForeArmRoll` | Bracelets (right wrist) |

The wrist bones are worth pointing out. The obvious guess is `SKEL_L_Forearm`, and that
is wrong — the game's own wrist props anchor to `RB_L_ForeArmRoll`, the roll bone that
turns with the wrist. Anchor to the forearm instead and the watch stays put while the hand
rotates under it.

## Where are the hand slots?

GTA's anchor enum has eight entries. Two of them — `ANCHOR_LEFT_HAND` (4) and
`ANCHOR_RIGHT_HAND` (5) — are deliberately **not offered by this add-on**, because they
were tested end to end and do not work.

What the test consisted of:

1. A prop built for `p_rhand`, anchored to `SKEL_R_Hand`
2. Named `p_rhand_001.ydd` and fed to Durty Cloth Tool
3. Durty labels those slots **"unused"** and refuses them, falling back to head
4. Corrected by hand anyway — the `.ymt` anchor edited in CodeWalker, the `shop.meta`
   rewritten to `ANCHOR_RIGHT_HAND` with matching drawable indices
5. Installed on a live server and queried with `GetNumberOfPedPropDrawableVariations`

**The slot still registered nothing**, while 0, 1, 2, 6 and 7 reported their usual counts
on the same ped. It failed at the metadata stage, before the question of whether the game
would render it was ever reached.

That is one attempt on one server rather than a proof, but it lines up with everything
else: vanilla ships **zero** drawables on those anchors out of 5213 prop entries, nobody
publishes one, no clothing menu writes them, and the author of the standard build tool
marks them unused.

Offering a slot that produces a file nobody can wear is worse than not offering it, so
they are gone.

`p_mouth` is kept despite having the same menu problem — masks and cigarettes are a real
use for it and a script can apply it directly. **Convert to Prop** warns when you pick it.

## Rings

Rings are the reason the hand slots keep coming up, and the answer is not a prop at all.

Put them in a **component**. `decl` (10) is the usual choice and what most published ring
mods use, but nothing forces it — `accs` and `teef` are both used in the wild, and any
component slot works if you would rather keep rings somewhere else in your own setup.

A component is skinned to the skeleton, so a ring weighted to the finger bones follows the
hand for free: no anchor, no menu patch, and no question about whether other players see
it. See [Rings](rings.md).

## Making a prop

The flow is the same for every slot:

1. Get the mesh right — one object, one material slot, a shader, a diffuse texture.
2. Pick the slot and number in the **Rigid prop (no movement)** box.
3. Press **Convert to Ear Prop (p_ears)**. The button keeps its name, but it converts for
   whichever slot you picked.

The full walkthrough, including the material rules, is on
[Earrings and piercings](earrings-and-piercings.md) — it applies to every prop, not just
earrings.

## Naming

Props are named `p_ears_002`, `p_head_014` and so on — **no `_u` variant suffix**, unlike
clothing components. The conversion sets the name for you.

To change the number afterwards, use **Set Clothing Slot / Name**. Do not run the
conversion a second time; it would transform the coordinates twice and move the prop off
its anchor.

## What a prop file looks like

Worth knowing if you are comparing against a file from the game:

* No `<Skeleton>` block at all
* `HasSkin = 0` and `BoneIndex = 0`
* Geometry stored relative to the anchor bone, not to world space
* High LOD only

The add-on produces all of this. You do not have to edit any of it by hand.
