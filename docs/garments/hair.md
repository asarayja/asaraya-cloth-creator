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

The one setting worth changing. It controls how much of the length borrows the spring
bone — and, because the two go together, how far up the movement starts.

| Value | Result |
| --- | --- |
| `0.20` | Movement in the tips only. Subtle |
| `0.35` | The default. Between the two reference styles |
| `0.60` | Swing from mid-back down. Obvious motion |

Both ends of that range come from real hair files that work in game, so anything between
them is safe.

**Spring side** picks which breast spring the hair borrows. Right is what most working
files use. *Split by side* sends left strands to the left spring and right strands to the
right — more natural in principle, but no reference file does it, so it is offered rather
than assumed.

## Where the numbers come from

Seven working FiveM hair files were measured. All of them use the same three bones and
nothing else, and 64–70% of their vertices carry more than one, so the transitions are
gradual rather than banded. The crossfade points were then fitted to both reference
profiles at once.

The fit is close on the spring — the part that produces the movement — and looser in the
middle of the head, because the reference files disagree with each other there. At
three-quarters height one holds the head at 99% and the other has already dropped to 70%.
No single curve reaches both, so the default sits between them, and **Hair Spring** moves
you toward whichever you prefer.

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
