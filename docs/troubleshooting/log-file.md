# The log file

When something goes wrong and the message in the viewport is not enough, the log has the
details.

## Turning it on

`Edit ▸ Preferences ▸ Add-ons ▸ Asarayja Cloth Creator`, and tick the log option.

The default location is `asarayja_cloth.log` in your home folder. You can point it
somewhere else in the same preferences.

## What is in it

Every operation records what it did and what it found: how many vertices were moved, which
vertex groups were rejected, which textures were restored after a shader change. The
numbers behind a report are all there.

## Where to look first

The messages nearest the bottom are the most recent. Errors are marked, so searching for
`ERROR` usually finds the relevant line quickly.

## Reporting a problem

If you are reporting a bug, the log is the most useful thing to include. Attach it along
with:

* your Blender version
* your Sollumz version
* the add-on version, shown at the top of the panel
* what you pressed, and what happened
