# Asarayja Cloth

A Blender add-on that prepares clothing, jewellery and props for **GTA V / FiveM**.
It sits on top of [Sollumz](https://sollumz.org) and handles the part Sollumz leaves to
you: weights, jiggle, fit, slot naming, shaders and the checks that catch a broken asset
before it reaches the game.

**Current version: 1.0.34** · Blender 4.2+

## Install

1. Install **[Sollumz](https://sollumz.org)** first and **restart Blender**
2. Download `asaraya_cloth_creator.zip` from [Releases](../../releases/latest)
3. Blender → Edit → Preferences → Add-ons → Install from Disk

Press **N** in the 3D viewport and pick the **Asarayja Cloth** tab.

Full instructions: [Installation](docs/getting-started/installation.md)

## What it does

| | |
|---|---|
| **Fit External to Body** | matches the source game's bone groups to the body instead of guessing from a bounding box |
| **Build Full Body** | assembles a weight-source ped with breast jiggle generated on the vanilla body shape |
| **Auto-Weight / Add Jiggle** | skin weights from the body, GTA-compliant, jiggle included |
| **Drape onto Body** | settles a garment with the cloth solver instead of projecting it geometrically |
| **Pre-Flight Check** | one pass over geometry, limits, weights, LODs, materials, UVs, naming and heel height |
| **Pose Test** | poses the ped through six extremes and reports clipping in millimetres, measured against the layers actually worn |
| **Set Clothing Slot / Name** | names the file for its component or prop slot, inside and out |
| **Convert to Ear Prop** | turns a skinned accessory into a rigid ped prop, verified against vanilla files |
| **Add Hair Jiggle** | weights hair down the head/spine/spring chain so the length lags instead of being welded to the skull |
| **Mirror to Other Hand** | builds the opposite hand's ring from one side |
| **Set Shader + Surface** | ped shaders with measured metal / skin / fabric presets |

## Documentation

**[asarayja.github.io/asaraya-cloth-creator](https://asarayja.github.io/asaraya-cloth-creator/)**

The source lives in [`docs/`](docs/) as plain Markdown. `build-site.py` renders it into
the static site published on GitHub Pages — no dependencies, just `python3 build-site.py`.

| | |
|---|---|
| New here | [How it works](docs/getting-started/how-it-works.md) |
| You have a FiveM `.ydd` | [Existing garment](docs/garments/existing-garment.md) |
| You have a model from elsewhere | [External garment](docs/garments/external-garment.md) |
| You are starting from nothing | [Your own clothing](docs/garments/your-own-clothing.md) |
| Hair | [Hair](docs/garments/hair.md) |
| Shoes and heels | [Shoes](docs/garments/shoes.md) |
| Earrings, rings, watches | [Prop slots](docs/props/prop-slots.md) |
| Something is broken | [Troubleshooting](docs/troubleshooting/fits-wrong.md) |

## About the defaults

Nearly every default in this add-on was measured against real GTA files rather than
guessed — anchor bones taken from vanilla props, shader values read off working
materials, clearance figures from actual garments. Several of them exist because an
earlier, reasonable-sounding assumption turned out to be wrong when measured.

## Requirements

- Blender 4.2 or newer
- [Sollumz](https://sollumz.org) enabled in the same Blender

## Licence

GPL-3.0-or-later — see [LICENSE](LICENSE). Blender add-ons that use `bpy` have to be
GPL-compatible, so this is the required choice rather than a preference.
