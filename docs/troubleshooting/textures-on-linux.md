# Textures on Linux

**Fixed in v1.0.5.** If you are on a current version there is nothing to do.

## What the problem was

Sollumz built the path to the texture folder using a hard-coded backslash. On Windows that
is the path separator and everything worked. On Linux it is an ordinary character in a
file name, so the path never resolved — and **every export lost its textures**.

This affected plain Sollumz too, not only this add-on. It was confirmed by importing the
same file through Sollumz on its own and getting the same result.

## What the add-on does now

**Import GTA Garment (auto-skeleton)** resolves texture paths itself instead of relying on
that code path. Textures load correctly on Linux, macOS and Windows alike.

## If you are on an older version

Update to the current release. If you cannot, assign the textures by hand after importing
— the image files are there, only the automatic lookup fails.

## Checking it worked

Switch the viewport to Material Preview after importing. If the garment shows its texture,
the paths resolved.
