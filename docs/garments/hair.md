# Hair

Hair goes in the `hair` slot (component 2) and uses the `ped_hair_cutout_alpha.sps`
shader. The part that is not obvious is the movement.


## The source figure does not have to be in the file

Delete the rig first or leave it — the result is **identical**. Measured across nine
hairstyles, both ways: the same scale to four decimals and the same placement to the
pixel.

That is deliberate. The figure was always going to be deleted, so needing it would have been
a trap: an earlier version aimed by the head in the file, and tidying up first made the
scale scatter to **1.172** and put one style over 99 % of the face.

## Fitting external hair to the head

Hair carries almost no bones, so the landmark fit that places clothing has little to work
with: of nine test hairstyles, five had only `Head` and `Spine2` and were refused
outright, and the four that passed had 4–5 pairs and produced scales from 0.88 to 1.15 —
from a rig where clothing, with 26 pairs, reports 0.95–1.00 every time. That spread is
noise, not size.

So hair is fitted its own way, and two measurements drive it.

**It is scaled to the skull.** The source figure's skull is wider than GTA's exactly where
hair sits. Measured at four heights below the crown, on the head mesh that ships with
every one of the nine files:

| Below the crown | GTA | Source | Ratio |
| --- | --- | --- | --- |
| 20 mm | 113 mm | 119 mm | 0.947 |
| 40 mm | 135 mm | 151 mm | 0.896 |
| 60 mm | 147 mm | 160 mm | 0.916 |
| 80 mm | 155 mm | 162 mm | 0.956 |

Mean **0.929**, and all nine files agree exactly because it is the same head. Comparing
the widest point of the whole head instead gives 181 mm against 180 and says they are the
same size — those maxima land at the jaw, not on the cranium, which is why this was missed
at first.

**It is aimed by where the source head is known to sit.** The exporter writes everything in
the figure's rest frame, so the head is in the same place in every export — measured across
all nine files, the largest disagreement is **0.00 mm on all three axes**. That makes the
whole transform a constant, and the head itself unnecessary.

The head in the file is still used when it happens to be there, purely as a cross-check;
it gives the same answer. And if the hair lands more than 350 mm from where a head should
be, the file was not written in that frame, so it falls back to the hair's own crown and
tells you.

Aiming by the hair's own centre is what it must *not* do: hair hanging down the back drags
the median with it and pushes a long style forwards onto the face.


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

## Movement

Not every hair is meant to move, so the first choice is how much it should.

| Mode | What it does | Use it for |
| --- | --- | --- |
| **Spring** | Head → torso → breast spring in the tips | Long hair advertised as having physics |
| **Follow torso only** | Head blended into the spine, nothing bounces | The commonest setup in ordinary hair. The length still lags when the head turns |
| **Rigid to the head** | Everything on `SKEL_Head` | Short, close-fitting hair. No movement at all |

All three come from real files. Of twenty ordinary hair files measured, most are
*Follow torso only*, two carry a spring anyway, and one is fully rigid.

**Hair Spring** below only applies in **Spring** mode.

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

28 working FiveM hair files were measured — eight sold as having physics, twenty
ordinary. The eight all use the same three bones and nothing else, and 59–70% of their vertices carry more than one, so the transitions are
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

**It renders white or solid** — that is the shader, not the weighting. Hair uses either
`ped_hair_cutout_alpha.sps` or `ped_hair_spiked.sps`; both are in the shader list. See
[Shader and surface](../tools/shader-and-surface.md).

## What is deliberately not reproduced

Two bones carry real weight in some ordinary hair files and are left alone here:
`MH_Hair_Crown` and `MH_Hair_Scale`, at up to 17%. They are not spring bones, and what
drives them has not been verified — so the add-on writes nothing to them rather than
guessing. If your hair came with weights on them and you run this tool, they are replaced
along with the rest.

**The file never appears in game** — hair is component 2, and the file name has to say
so. See [Clothing slot](clothing-slot.md).
