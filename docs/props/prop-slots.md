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
| `p_lhand` | `PH_L_Hand` | Held items, left hand |
| `p_rhand` | `PH_R_Hand` | Held items, right hand |

## Three of these are not in the clothing menu

GTA has eight prop slots. A clothing menu does not have to offer all eight, and the common
ones do not.

Checked against illenium-appearance's own source, it writes prop ids **0, 1, 2, 6 and 7**
— Hat, Glasses, Ear, Watches, Bracelets. Ids **3 (`p_mouth`), 4 (`p_lhand`) and
5 (`p_rhand`)** are never written, so a player has no way to select them.

Those three still produce valid files, and a script can apply them directly. But if you
are building for players to pick from a menu, stay on the five that work. **Convert to Ear
Prop** warns you when you choose one of the other three.

The wrist bones are worth pointing out. The obvious guess is `SKEL_L_Forearm`, and that
is wrong — the game's own wrist props anchor to `RB_L_ForeArmRoll`, which is the roll bone
that turns with the wrist. Anchor to the forearm instead and the watch stays put while the
hand rotates under it.

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
