# Shader and surface

The shader decides how the game draws a material, and the wrong one fails in ways that
look like a modelling mistake. The most common is transparency: lace and mesh need
`ped_alpha`, and on plain `ped` the alpha channel is ignored and the fabric comes out
solid.

## Steps

1. Select the garment.
2. In the **Shader** box, pick a shader and a surface.
3. Press **Set Shader**.

Your textures are kept. The shader change rebuilds the material's node tree, so the
add-on captures the textures first and puts them back afterwards, matched by name. If the
new shader has no slot for one of them, you are told rather than left to discover it
later.

## The shaders

| Shader | Use it for |
| --- | --- |
| `ped.sps` | **Opaque fabric. The default, and right for most garments.** |
| `ped_alpha.sps` | Lace, mesh, tulle, nylon, sheer panels — anything whose texture has real transparency |
| `ped_default.sps` | What Rockstar's own body parts use. Pick it when matching a vanilla part |
| `ped_default_cutout.sps` | Transparency that is fully on or off, no blending — cut-out patterns, eyelets. Cheaper than `ped_alpha` and free of sorting problems |
| `ped_cloth.sps` | A garment driven by GTA's cloth simulation. Needs a `.yld` to go with it |
| `ped_enveff.sps` | Patent leather, latex, wet vinyl — environment reflection. One of the reference shoes uses it |
| `ped_decal.sps` | Sits on top of another surface: logos, prints, rings, anything in the `decl` slot |
| `ped_hair_cutout_alpha.sps` | Hair cards |

It goes both ways: `ped_alpha` on an ordinary opaque garment costs a sorting pass and can
make it flicker against other transparent things. Do not use it as a safe default.

## The surfaces

The surface preset writes the parameters that decide whether something reads as metal or
as cloth.

| Surface | Use it for |
| --- | --- |
| **Metal (polished)** | Jewellery, piercings, buckles. Tight, bright highlight |
| **Skin** | What the vanilla body uses |
| **Fabric** | Cotton, denim, wool — matte. The right default for clothing |
| **Leave as-is** | Change the shader without touching how shiny the surface is |

Every number behind these presets was read off a real working file, not guessed. Metal
carries roughly a hundred times the specular intensity of fabric, with a highlight about
four times tighter.

## Blender's Metallic slider does nothing

This trips up nearly everyone. The **Metallic** and **Roughness** sliders on the
Principled BSDF are viewport-only. They make the object look metallic in Blender and
change absolutely nothing in game.

GTA reads its own parameters, and the **Metal (polished)** surface is what writes them.
If something looks right in Blender but flat in game, this is why.

## Common problems

**Lace renders solid** — you are on `ped.sps`. Switch to `ped_alpha.sps`.

**A texture went missing after switching shader** — the add-on reports which one and on
which material. The new shader has no slot for that parameter; re-assign it or pick a
shader that has it.

**Everything renders white** — see [White in game](../troubleshooting/white-in-game.md).
