# Building .ytd texture files

A garment's colour variants are one `.ytd` each. Twelve colourways means twelve texture
dictionaries, and building them meant opening CodeWalker or OpenIV and doing it by hand,
twelve times.

**Build .ytd Textures** does the whole set in about a second.

## Steps

1. Export your colour variants as `.dds` into one folder — `a.dds`, `b.dds`, `c.dds` …
   NVIDIA Texture Tools, GIMP and `texconv` all write these.
2. Set the slot and number in the **Clothing slot** box — that is where the file names
   come from.
3. Press **Build .ytd Textures** and pick any `.dds` in the folder.

You get one `.ytd` per variant, written beside the source files and named the way Durty
Cloth Tool looks for them:

| Kind | Name |
| --- | --- |
| Component | `jbib_diff_000_a_uni.ytd`, `_b_uni`, `_c_uni` … |
| Component, race-dependent | `_a_whi.ytd` when the variant is set to `r` |
| Prop | `p_ears_diff_002_a.ytd` — no race suffix |

## The letters matter

Durty Cloth Tool counts variants by walking letters from `a` upward and **stopping at the
first one missing**. A gap does not produce an error; everything after it is silently
dropped, so `a, b, d` gives you two colourways in game instead of three.

The add-on keeps the letter your file already has — `d.dds` becomes `_d_`, not renumbered
to `_c_` — because the letter decides which colourway a texture becomes and you chose it.
Then it checks the sequence and tells you which letters are missing.

## What it needs from you

**Block-compressed `.dds`.** DXT5 for anything with transparency, DXT1 for anything
without. An uncompressed `.dds` is refused with a message rather than written into a file
the game cannot read.

That requirement is not a design choice — **Blender cannot write `.dds` at all.** It has
no DDS export, no Pillow, and its bundled OpenImageIO lists the format but refuses to
create one. So the compression has to happen in your texture tool, and the add-on takes it
from there.

Sizes up to 4096 × 4096 work, and non-square is fine — a Sims texture is usually
2048 × 4096.

## About texture size

A 2048 × 4096 DXT5 with mips is 11 MB of pixels. It compresses to about 540 KB on disk,
so twelve variants cost roughly 7 MB of files — but the graphics page the game allocates
is the uncompressed size, and only one variant is loaded at a time.

For comparison, the vanilla-style clothing in the reference set is 1024 × 1024, about
1.4 MB when loaded. If a garment feels heavy in game, the resolution is the first thing to
look at.

## How it works, and what is still unproven

A `.ytd` is a 16-byte `RSC7` header, then a raw deflate stream holding a small description
of the texture and the pixels themselves. **The pixels are a straight copy of the `.dds`
payload** — no image encoding happens, which is the only reason this is possible in pure
Python with no dependencies.

Every field was measured against the 30 real `.ytd` files in this project rather than
taken from documentation. Writing them back out:

* **11 of 30 come back byte-for-byte identical** — every one CodeWalker built
* **17 of 30 differ by 13–14 bytes** out of 1–2 MB, in fields that already hold three
  different values across three builders, with identical headers
* 2 differ more, because that builder pads with `0xCD` instead of zero and picks a
  different but arithmetically equal page encoding

**No file written by this tool has been loaded by the game.** The bytes match every
reference available; whether GTA accepts them is a different question, and only a test in
game answers it. Build one, put it in a resource, and look at the garment before you build
a wardrobe this way.

## Common problems

**"is uncompressed"** — re-export the `.dds` with DXT5 or DXT1 compression.

**Durty only shows some of the variants** — a gap in the letters. The add-on warns about
this; check the message.

**The garment is untextured in game** — the `.ytd` is only half of it. The drawable also
needs its shader slot pointing at the dictionary; see
[Assigning textures](textures.md) and [Clothing slot](../garments/clothing-slot.md).
