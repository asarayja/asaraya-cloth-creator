# Hair

Hair goes in the `hair` slot (component 2) and uses the `ped_hair_cutout_alpha.sps`
shader. The part that is not obvious is the movement.

## Steps

1. **Build Full Body** if you have not already.
2. Select the hair mesh.
3. Set **Hair Spring** in the **Hair** box.
4. Press **Add Hair Jiggle**.
5. **Set Shader** → `ped_hair_cutout_alpha.sps`.
6. **Set Clothing Slot / Name** → `hair`, and a number.
7. **Pre-Flight Check**, then export.

## What "hair physics" actually is

There is no hair simulation in GTA. The engine drives exactly one kind of bone with
spring dynamics on the freemode skeleton — the breast springs — and there is no hair
chain to drive.

What working hair mods do instead is spread the hair's weight down a vertical chain, so
the length lags behind the skull rather than being welded to it:

| Part of the hair | Bone | Effect |
| --- | --- | --- |
| Skull cap | `SKEL_Head` | Follows the head exactly |
| Middle length | `SKEL_Spine3` | Follows the torso, so it lags when the head turns |
| Tips | `SPR_R_Breast` | Borrows the one bone the game actually springs |

**Add Hair Jiggle** writes that whole chain for you, with smooth crossfades between the
three.

## Hair Spring

The one setting worth changing. It controls how much of the tips borrow the spring bone.

| Value | Result |
| --- | --- |
| `0.20` | Barely perceptible |
| `0.35` | The default |
| `0.60` | Clear movement |
| `0.97` | The tips move almost entirely with the spring |

Every value in that range comes from a real hair file that works in game, so anything
between them is safe.

Where along the length the movement *starts* is fixed, and deliberately not a setting —
see below.

**Spring side** picks which breast spring the hair borrows. Right is what most working
files use. *Split by side* sends left strands to the left spring and right strands to the
right — more natural in principle, but no reference file does it, so it is offered rather
than assumed.

## Where the numbers come from

Eight working FiveM hair files were measured. All of them use the same three bones and
nothing else, and 59–70% of their vertices carry more than one, so the transitions are
gradual rather than banded. The crossfade points were then fitted to all three distinct
profiles at once.

**Why the starting point is not a setting.** It looked at first as though a stronger
spring also started higher up the hair, and an early version tied the two together. A
third reference file disproved it: its spring is the strongest of the eight and starts
*lower* than a middling one. The measured starting points are 0.25, 0.40 and 0.60 against
strengths of 0.20, 0.97 and 0.60 — no relationship at all. With nothing to predict it
from, the starting point is fixed at the middle of the measured range.

The fit is closest on the strongest and subtlest files and loosest on the middling one,
which starts its spring higher than the other two. Where the references disagree with
each other, the curve sits between them.

## It replaces the existing weights

Working hair carries two or three bones and nothing else, so this writes the whole
skinning rather than blending into what is there. If the hair already had real weights
you wanted, the add-on says how many groups it replaced — **Ctrl+Z** puts them back.

## Short hair

A bob, a bun or a fringe has no length to swing. If the mesh is under about 60 mm tall,
the tool weights it to the head alone and tells you why. Spreading a cap down the spine
would make it slide off the skull.

## Common problems

**The hair slides off the head when the character moves** — too much spring for that
length. Lower **Hair Spring**, or check the mesh is not far shorter than it looks.

**Nothing moves at all** — the hair may be bound to the wrong armature. Select it with
the Base Body in the scene and run the tool again.

**It renders white or solid** — that is the shader, not the weighting. Hair needs
`ped_hair_cutout_alpha.sps`. See [Shader and surface](../tools/shader-and-surface.md).

**The file never appears in game** — hair is component 2, and the file name has to say
so. See [Clothing slot](clothing-slot.md).
