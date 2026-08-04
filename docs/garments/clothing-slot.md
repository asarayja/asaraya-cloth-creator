# Clothing slot and file name

GTA finds clothing by **file name**. Get the name wrong and the garment never appears in
game — and you get no error explaining why. This is the most common reason a garment
"does not work".

## Steps

1. Select the garment.
2. In the **Clothing slot (file name)** box: pick the slot, set the number, pick the
   variant.
3. Press **Set Clothing Slot / Name**.

The result is a name like `mp_f_freemode_01^jbib_000_u`, and that is the name Sollumz
exports the file under.

## The clothing slots

| Slot | No. | What it is |
| --- | --- | --- |
| `head` | 0 | Head |
| `berd` | 1 | Beards, masks and face overlays |
| `hair` | 2 | Hair |
| `uppr` | 3 | Torso and arms (the body itself, under clothing) |
| `lowr` | 4 | Legs, trousers |
| `hand` | 5 | Hands |
| `feet` | 6 | Feet, shoes |
| `teef` | 7 | Teeth — and in practice a lot of jewellery |
| `accs` | 8 | Accessories: scarves, chains, bags |
| `task` | 9 | Vests and body armour |
| `decl` | 10 | Decals and overlays: logos, rings |
| `jbib` | 11 | Top layer: jackets, dresses, shirts |

**Dresses and tops belong in `jbib`.** That is the one you will use most.

## Variants

* **`u` — Universal.** One texture set. This is the normal choice for add-on clothing.
* **`r` — Race-dependent.** Separate variants per skin tone. Used by the base game.

Prop slots (`p_ears`, `p_head` and the rest) take **no** variant — they are named
`p_ears_002`, not `p_ears_002_u`. Pick a prop slot and the panel hides the variant field
by itself.

## About the name inside the file

A `.ydd` also carries a name **inside** it, and it does not have to match the file name.
The game matches on the **file** name.

This is worth stating plainly because it is easy to assume otherwise. Of 28 downloaded
hair files measured for this add-on, most carry an internal name inherited from whatever
they were built from — `hair_000_u.ydd` calling itself `hair_019_u`, another calling
itself `base mio` — and they all work in game.

So renaming a downloaded file on disk is enough. **Set Clothing Slot / Name** sets both
at once, which is worth doing for clothing you build yourself: it keeps the outliner
readable and means the export lands with the right filename instead of needing a rename
afterwards.

## The slot-change warning

If the add-on sees the garment was previously named something like `jbib_...` and you
name it `uppr`, it tells you. Moving a garment between slots is legitimate — but it looks
exactly like a misclick from the outside, so you get asked.
