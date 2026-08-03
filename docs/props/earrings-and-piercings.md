# Earrings and piercings

There are two ways to put jewellery on a head, and picking the right one saves a lot of
frustration.

| | Clothing component (`teef`) | Prop (`p_ears`) |
| --- | --- | --- |
| How it works | Skinned to the skeleton, like a garment | Rigidly attached to a bone |
| Moves with the head | Yes | Yes |
| Swings on its own | No | No |
| What the base game uses | — | **This** |

GTA's own hoop earrings are props. If you want jewellery that behaves like the real
thing, make a prop.

> **A note on swinging.** Real earrings swing when you walk, and it is tempting to try to
> reproduce that with bones. It does not work: the game gives you no way to drive that
> motion, and every attempt ends up with the earring leaving the ear and passing through
> the head. A prop sits exactly where a real earring sits, and that is the correct answer.

## Before you convert

The conversion is a one-way transformation, so get the mesh right first.

1. **Join everything into one mesh.** Select all the pieces and press **Ctrl+J**. A set
   of piercings should be a single object.
2. **Put everything on one material slot.** Joining with Ctrl+J leaves one slot per piece
   you joined. Every extra slot exports as its own shader *and* its own geometry — all
   four of the game's own ear props ship exactly one of each.
   In Edit Mode: press **A** to select all, pick slot 0, press **Assign**, then remove the
   unused slots.
3. **Set the shader.** Press **Set Shader** with surface **Metal (polished)** for steel,
   silver or chrome. See [Shader and surface](../tools/shader-and-surface.md).
4. **Assign a diffuse texture.** Without one the jewellery renders pure white in game.
   The texture node must be the one named `DiffuseSampler` — a normal map and a spec map
   are not enough on their own.

**Pre-Flight Check** catches all four of these if you would rather just run it and read
the list.

## Converting

1. Select the jewellery.
2. In the **Rigid prop (no movement)** box, pick the slot — `p_ears` for earrings — and
   set the number.
3. Press **Convert to Ear Prop (p_ears)**.

You get a finished prop: no skeleton, geometry rewritten relative to the anchor bone, and
named `mp_f_freemode_01^p_ears_002`.

> **Only run this once.** Converting rewrites the coordinates relative to the bone. Run
> it a second time and it does that again, which ruins the placement. To change the
> number afterwards, use **Set Clothing Slot / Name** instead — that only renames.

## Where each slot attaches

| Slot | Bone | What it is for |
| --- | --- | --- |
| `p_ears` | `SKEL_Head` | Earrings |
| `p_head` | `SKEL_Head` | Hats and headwear |
| `p_eyes` | `SKEL_Head` | Glasses |
| `p_mouth` | `SKEL_Head` | Masks and cigarettes |

See [Prop slots](prop-slots.md) for the full table including wrists and hands.

## Common problems

**It renders white in game** — no `DiffuseSampler` texture, or the wrong shader. See
[White in game](../troubleshooting/white-in-game.md).

**It looks metallic in Blender but not in game** — you set the Principled BSDF's
*Metallic* slider. That is a viewport-only control and is not exported. Use
**Set Shader** with the **Metal (polished)** surface instead.

**The piercing looks faceted, not round** — that is the mesh, not the export. Add a
Subdivision Surface modifier, or right-click the object and choose **Shade Smooth**.
