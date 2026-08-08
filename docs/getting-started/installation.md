# Installation

## What you need

* **Blender 4.2 or newer**
* **Sollumz 2.8.3 or newer** — the add-on builds on Sollumz and does nothing without it
* **Asarayja Cloth Creator** — `asaraya_cloth_creator.zip` from [Releases](https://github.com/asarayja/asaraya-cloth-creator/releases)


## Sollumz 2.9.0

Works. Everything the add-on does was re-run against it: 19 garments through the whole
flow — fit, weights, drawable, slot, shader, export skinning, LODs — with **0 Pre-Flight
errors**, and the `.ytd` writer still reproduces the same 11 of 30 reference files
byte-for-byte.

Two things about 2.9.0 are worth knowing before you upgrade.

**It needs a dependency installed.** The core of import and export moved out into a Python
package called `szio`, and until it is there Sollumz registers *nothing* — not even
`sollum_type` — so every button here fails. Blender shows a **Install dependencies**
button in Sollumz's add-on preferences. Press it once. A `szio` from an older Sollumz does
not count: 2.9.0 wants 1.3.0.dev9 and refused to start on the 1.3.0.dev7 that was already
installed.

**The import call changed shape.** `import_ydd(filepath)` became
`import_ydd(asset, name)`, taking something already parsed rather than a path. The add-on
now imports through Sollumz's **operator** instead of that function — the same entry point
the File menu uses, which kept its name and arguments across both versions and is the more
stable thing to depend on.

**HD texture dictionaries** are new in 2.9.0: textures marked HD export to a `+hi.ytd` at
full resolution while the base `.ytd` holds half-resolution copies. [Build .ytd
Textures](../tools/ytd.md) writes the base file only, at full resolution, which is what
Durty Cloth Tool looks for.


## Steps

1. Install **Sollumz** first: `Edit ▸ Preferences ▸ Add-ons ▸ Install from Disk` →
   pick the Sollumz zip → tick the checkbox to enable it.
2. **Restart Blender.** Sollumz registers things that are only fully in place after a
   restart, and this add-on reads from them.
3. Install **`asaraya_cloth_creator.zip`** exactly the same way.
4. In the 3D viewport press **N** to open the sidebar, then choose the
   **Asarayja Cloth** tab.

## Check that it worked

The top of the panel shows the version, for example `Asarayja Cloth  v1.0.20`.

If it says **"Sollumz not enabled"** instead, then Sollumz is either not installed, not
ticked, or Blender was not restarted after installing it. Repeat steps 1 and 2.

## If the buttons are greyed out

Most buttons need something selected in the scene — usually a body and a garment. See
[Base Body](base-body.md).
