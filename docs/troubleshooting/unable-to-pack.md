# "Unable to pack file" when saving

Saving your .blend prints one of these per line, naming `.dds` files in a folder that
never had them:

```
Unable to pack file, source path '.../uppr_diff_015_a_whi.dds' not found
Unable to pack file, source path '.../head_diff_045_a_whi.dds' not found
Unable to pack file, source path '.../givemechecker.dds' not found
```

**It is harmless, and it is not your garment.** Nothing is broken and nothing is lost.

## Where it comes from

Those names — `uppr_`, `lowr_`, `head_`, `feet_`, `givemechecker` — are GTA body textures.
They belong to the **Base Body** the add-on builds, not to anything you imported.

The add-on ships the body geometry but not GTA's textures, and the importer still points
every material slot at a `.dds` next to the file it read. Those paths are stored
**relative**, so they re-resolve against wherever *you* save your .blend, and Blender
reports one missing file per slot from then on.

It is easy to blame the garment — a Sims import does bring its own textures with it — but
those arrive **packed inside the .blend**, which is why they never show up in this list.

## The fix

**Press Build Full Body once and save again.** Rebuilding clears the dead texture links,
including in a file that already has them, and the messages stop.

Current versions do this automatically at the end of every build, so a body built from now
on never carries them.

## What is not touched

Only images that are **broken** (the file is genuinely missing), **not packed**, and used
by **no material on any object** are removed. Your garment's own textures fail every one of
those tests:

* a Sims import's textures are packed, so they are kept whatever their path says
* a texture you assigned yourself sits on a live material, so it is kept even if the path
  is wrong — fix the path rather than losing the reference

Verified on a real file: 7 broken links removed, `BaseTexture` and `DiffuseMap` on the
garment untouched, and packing then completed with no errors at all.
