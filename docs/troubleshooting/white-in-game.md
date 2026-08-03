# It renders white in game

The garment or prop looks correct in Blender and comes out plain white in game. Work down
this list — the first item is the cause most of the time.

## 1. No diffuse texture

A material can carry a normal map and a specular map and still render pure white, because
the **diffuse** is what supplies the colour.

The texture node must be the one named **`DiffuseSampler`**. Any other name is a
different parameter, and the game will not use it as colour.

**Pre-Flight Check** reports this specifically, and lists which texture nodes you do have.

## 2. It is only a preview

[Preview Texture](../tools/texture-preview.md) shows a texture in the viewport and is
deliberately never exported. If that is the only texture on the material, the export has
none.

Pre-Flight Check says so as INFO when a preview is active.

## 3. The material is not a GTA shader

An ordinary Blender material is not a GTA material. Run **Convert to FiveM Drawable**, or
set the shader with [Set Shader](../tools/shader-and-surface.md).

## 4. The texture did not get exported

Check that the texture file actually ended up next to the `.ydd`. On Linux there was a
path bug that lost textures on every export — see
[Textures on Linux](textures-on-linux.md).

## 5. You set Blender's Metallic slider

For metal specifically: the **Metallic** and **Roughness** sliders on the Principled BSDF
are viewport-only. They make it look metallic in Blender and change nothing in game.

Use **Set Shader** with the **Metal (polished)** surface instead. That writes the
parameters GTA actually reads.

## The short version

Run **Pre-Flight Check**. It checks 1, 2, 3 and 5 and tells you which one it is.
