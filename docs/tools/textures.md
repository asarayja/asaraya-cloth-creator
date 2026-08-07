# Assigning textures

A GTA material has three texture slots that matter, and setting them by hand means finding
the right node three times, for every material on the garment. It is the last step that
sends you into the Sollumz material panel.

| Slot | What goes there |
| --- | --- |
| `DiffuseSampler` | The colour. Without it the garment renders white in game |
| `BumpSampler` | The normal map |
| `SpecSampler` | The specular map |

Those three names appear 186 times each across the reference clothing measured for this
add-on, so there is nothing to guess about where a map belongs.

## Steps

1. Select the garment.
2. Press **Assign Textures**.
3. Pick **any one** of its textures — diffuse, normal or spec. `.dds` is the default
   filter, since that is what almost all of them are.

The file you picked is recognised by its name, the others are found beside it in the same
folder, and each goes on the right node.

## Pick any one, not the diffuse

This is deliberate, and it is what makes the button usable rather than merely convenient.

A real garment folder often holds **no diffuse at all** — the reference `.ydd` folders in
this project ship `feet_normal_002.dds` and `feet_spec_002.dds` and nothing else, because
the colour lives in the `.ytd`. A garment from The Sims is the mirror image: its diffuse
arrives already on the material from the `.blend`, and the normal and spec are the loose
files you have to add.

Demanding the diffuse first would have failed on both.

## How the maps are found

Names are regular enough to sort out automatically. Across 211 texture files in the
reference clothing, 92 contain `normal`, 92 contain `spec`, and the rest are `bump`,
`diff` or `noise`.

| Name contains | Goes on |
| --- | --- |
| `normal`, `bump`, `_n` | `BumpSampler` |
| `spec`, `_s` | `SpecSampler` |
| `noise` | `AnisoNoiseSpecSampler` — the hair shaders' slot |
| anything else | `DiffuseSampler` |

When a folder holds several garments' textures, the file sharing the longest name prefix
with the one you picked wins — so `hair_diff_123` takes `hair_normal_123` rather than
`feet_normal_000`.

If the only candidate for a slot has a name that does not match at all, it is still used —
it may genuinely be the right file — but you are told, because a folder holding a whole
wardrobe would otherwise pair `jbib_normal_000` with `feet_spec_000` without a word.

## A garment made of several pieces

Materials that already carry a diffuse of their own are left alone rather than overwritten,
so joining trousers and a belt and then assigning textures does not flatten one onto the
other. The report says which materials were skipped and why.

## Common problems

**The garment still renders white** — the diffuse slot is empty. Pre-Flight names this
specifically; see [White in game](../troubleshooting/white-in-game.md).

**"No file found for SpecSampler"** — there was no matching file beside the one you picked.
Put the maps in the same folder, or assign that one by hand.

**It picked the wrong file** — you will have been warned if the name did not match. Run it
again pointing at the correct file; the picked file always wins for its own slot.

**You only want to look at a texture, not assign it** — use
[Preview Texture](texture-preview.md), which is never exported.
