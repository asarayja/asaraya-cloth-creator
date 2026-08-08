# External garment

You have a model from another game, from Marvelous Designer, or from a 3D store, and you
want it in FiveM.

The difference from a FiveM garment is that this one has **the wrong proportions** and
**no weights that mean anything** to the GTA skeleton. Both have to be dealt with.

## Steps

1. **Build Full Body**.
2. Import the garment into Blender the normal way (`.fbx`, `.obj`, `.blend` — whatever
   fits).

   Opening the source file and building the body **into** it works just as well, if the
   garment is already set up there. **Fit External to Body** removes the source rig for
   you either way — one imported dress arrives bound to a 165-bone rig of its own, and leaving
   it would mean the garment is deformed by two skeletons at once after weighting.
3. Select the **Base Body first**, Shift-select the **garment**.
4. **Fit External to Body** — scales and places the garment onto the body, removes the
   source game's rig, and clears the body out of the fabric.
5. **Convert to FiveM Drawable** — turns the mesh into something the GTA format
   understands.
6. **Auto-Weight (new garment)** — the garment has no usable weights, so you build them
   from scratch here.
7. **Set Shader** → pick shader and surface. See [Shader and surface](../tools/shader-and-surface.md).
8. **Set Clothing Slot / Name** → pick the clothing slot. See [Clothing slot](clothing-slot.md).
9. **Pre-Flight Check**, fix anything marked ERROR, and export.



## A model with no rig at all — .glb, .fbx, marketplace downloads

Clothing bought or downloaded as a plain 3D model has no skeleton and no vertex groups, so
there are no landmarks to fit by. It also arrives at whatever size the artist worked in.
Measured across 16 `.glb` garments, the heights ran from **0.01 m to 1300 m** — four
orders of magnitude, in the same folder.

**They now land on the body at body scale regardless.** All 16 came out between 0.32 m and
1.83 m, centred on the figure, with no hand adjustment: import, select every piece, press
**Fit External to Body**.

Two things had to be fixed for that, and both were about the model being a *model* rather
than a game asset:

* **It is usually several meshes.** The fit sized and moved only the active object, so a
  two-piece outfit had one piece scaled and the other left where it was — one test garment
  came out **146 m tall**. Every selected piece is now measured together and moved by the
  same transform.
* **Its origin is nowhere near its geometry.** Moving it by setting the object's location
  assumed otherwise and displaced it by the offset. Everything now goes through the world
  matrix, so where the origin sits stops mattering.


### Turn off Push out for a delicate garment

**Fit External to Body** clears the body out of the garment when it finishes, and for
almost everything that is essential — an imported garment can arrive with half its vertices inside
the body and is unusable without it.

On a rig-less model it can be too much. A bounding-box fit gets the position and rough size
right but cannot match the *shape* of a body fuller than the mannequin the piece was
modelled on, so a lot ends up buried: on a chained halter top, **4321 of 13031 vertices
started inside the body and 5408 faces cut through**, and clearing them moved 4633
vertices by a median 36 mm. The neckband crumpled and the hem tore into spikes — while
every number stayed healthy, because nothing had opened a seam and nothing was left inside.

Untick **Push out of the body** in the redo panel and the garment comes through pristine.
Then fix the clipping by hand, or by [poke-through](../tools/poke-through.md) on the parts
that need it.


### Files that need a hand first

**The model's own mannequin often comes with it.** A `.blend` from a marketplace can hold
the body it was fitted to, a backdrop plane and the rig's widget shapes; one `.fbx` brings
the model's head along. None of that is clothing, and picking it by mistake fits the wrong
object. Look at the outliner and select the garment.

**Some `.fbx` files import as nothing.** One hair model here returns zero objects from
Blender's importer at every setting, although the file plainly contains geometry — a
`Vertices` array, four `Geometry` nodes and thirteen deformers are in there. That is a
limitation of the importer, not of this add-on. Convert the file elsewhere first.

### Textures come in on their own

A `.glb` carries its textures inside the file, and Blender's importer unpacks them and
wires them to the material for you — measured across eight files, every image that was in
there arrived **packed into the .blend and connected**, at its original resolution up to
2048×2048. Nothing has to be extracted by hand.

Some models ship with no texture at all; two of the eight had none. Those need one
assigning, see [Assigning textures](../tools/textures.md).

### Height is measured below the neck

Clothing does not cover the head, so the height it is matched against is the body from the
**neck joint down**, not the whole figure. Matching the full height stretches a garment by
exactly one head: a crop top and trousers came out 1.83 m on a 1.83 m body, with the
neckline over the chin.

### What it cannot know, and what to do about it

**What the garment IS** — the file name answers it, so the fit now asks.

A bounding box cannot tell a bikini from a dress, and measuring either against a whole
1.83 m body made everything partial come out too big: a bikini landed 1.2 m tall with the
straps hooping past the shoulders, and a pair of trousers put its waistband at the
shoulders. The names are unambiguous, though. Across 42 downloaded garments the word
*top* appears 20 times, *skirt* 8, *crop* 6, *pants* 5, *dress* 3.

So **What is it** sits above the Fit button. Leave it on *Auto* and the name decides;
override it when the name is unhelpful. Each kind is measured against the part of the body
it covers, taken from the skeleton rather than from fixed heights so the male body needs no
second table:

| Kind | Covers |
| --- | --- |
| Crop top / bralette | Shoulders to the waist |
| Top | Shoulders to the hip |
| Bikini / lingerie | Bust and hips |
| Necklace / chain | The neck — the `teef` component |
| Skirt, Shorts | Waist to the knee |
| Trousers | Waist to the ankle |
| Dress | Shoulders to the knee |
| Full outfit | Shoulders to the ankle |

Measured on the same files, before and after: a pleated skirt went from **6.90 m to
0.49 m**, trousers from 1.54 m to 0.90 m, a crop top to 0.48 m at the chest.

Auto reads 39 of the 42 correctly. The three it declines are a hair model and two
necklaces — and necklaces now read as `NECK`. Order decides ties, so *bikini set* is a
bikini rather than an outfit, *corset waist dress* is a dress, and *crop top* is a crop.

**A bikini is still the hard one.** Its box is far wider than it is tall — the straps reach
out — so matching height undersizes it. Set the size by hand there.

Two ways round it were tried and are worse, both recorded here so they are not tried
again: matching **width** alone lets a tall model overshoot vertically, and **searching**
for whichever scale ends up nearest the body picks grotesque sizes, because nearness is not
enclosure — an oversized garment sweeps past a great many body points on its way by, and
that put one pair of trousers at two and a half metres.

So when a garment lands at the wrong size, use **Size** and **Nudge up** in the redo panel
at the bottom left. They are there for exactly this, and they re-run instantly.

Beyond that, the fit does not know a puffed sleeve from a fitted one, so expect to use
[poke-through](../tools/poke-through.md) and the sleeve tools afterwards, as with any
other garment.


## The source game's own character

A .blend exported from a character creator contains the whole figure — body, head, teeth, feet —
sitting beside the garment. It is not clothing; it is the mannequin the clothing was
modelled on, and leaving it there means picking the wrong mesh and fitting the wrong
object.

**Fit to Body deletes it for you**, along with the source rig it was bound to.

What identifies it is parenting, and the rule turned out to be exact. Checked over 125
meshes in 20 real files, with no exceptions either way:

* the figure's parts are **parented** to the source rig — 72 of 72
* the garment or hair never is, only modifier-bound — 53 of 53

So deleting the rig's children removes the figure and can never remove the clothing. It is
the same thing as *Delete Hierarchy* on the rig, which is what people do by hand.

**When the body is merged into the garment mesh itself**, nothing can separate them —
there is no name or material to go by. Two of the test files were like that, and they have
to be cleaned up in Blender first. [Pre-Flight](../tools/pre-flight-check.md) warns when
the mesh you selected looks like the figure rather than the clothing.


## It uses the source game's rig, if the garment still has it

A garment ripped from another game almost always arrives with that game's vertex groups
still on it — names like `b__L_Calf__`, `b__Spine1__`, `b__CAS_L_Breast__`. Those
groups are the best fitting information available, because they say which body part every
vertex belongs to. A bounding box cannot know that.

**Fit External to Body** translates those names to GTA's, matches each shared bone between
the garment and the body, and solves for the scale, rotation and position that line them
up. It falls back to the old bounding-box method when a garment has no usable groups, and
the report tells you which it used.

The difference on three real imported garments, measured as the median distance from the
garment to the body surface:

| Garment | Bounding box | Bone groups |
| --- | --- | --- |
| Bikini set | 63 mm | **24 mm** |
| Dress | 67 mm | **13 mm** |
| Dress, full length | 85 mm | **21 mm** |

### Placing it is only half the job

A garment can be scaled and positioned perfectly and still have the body straight through
it, because the figure it was made for is a different shape. Measured on the same three
garments right after a good-looking fit, the share of garment vertices sitting **inside**
the body was 38%, 55% and 55% — the skirt collapsed onto the legs, the body showing
through the front.

So the button finishes the job: after placing the garment it pushes the body out of the
fabric. That takes those figures to 1%, 3% and 3%, with nothing deeper than a millimetre.

This is worth knowing about because the obvious way to measure a fit — distance from the
garment to the nearest point on the body — cannot see the problem at all. A garment buried
13 mm inside the body scores exactly the same as one sitting 13 mm outside it. The
measurement has to be signed.

### Meshes from a game are split along their seams

This is the single thing that most often destroys a garment, and it is invisible until it
happens.

A game stores UVs per vertex, so wherever the texture has a seam the mesh carries **two
vertices on the same point with no edge between them**. Across the imported garments measured
for this add-on that runs from 21% of the mesh to **100%** of it. Nothing about the vertex
or face count reveals it.

Any tool that moves vertices then moves each side of a seam separately, and the seam opens
into a crack. Before this was handled, clearing the body out of a dress split 330 of its
718 seams, the worst by 118 mm — the straps came apart into ribbons.

**Fit External to Body**, the poke-through tools and **Drape** now all keep coincident
vertices together. Measured across 47 meshes, female and male: **zero** seams opened, and
no topology changed.

Coincident vertices are found by proximity rather than by a rounded coordinate. Rounding
looks equivalent and is not: a transform leaves about a ten-thousandth of a millimetre of
float drift, and two points either side of a rounding boundary land in different buckets.
On a male t-shirt that let 2 of 128 seams through, which opened by 8.5 mm.

### One outfit in several pieces

An export often splits an outfit — trousers and a belt, a top and its sleeves. Fit them
separately and they drift apart: a belt fitted on its own landed **161 mm** above the
trousers it belongs to, and 33 mm too tight, because a thin band carries too few bone
groups to fit reliably.

Join the pieces with **Ctrl+J first**, then fit once. The same belt then sat 4.5 mm out.

This applies to any file that opens with several objects — one male outfit arrived as
seven, including two four-vertex scraps that landed 160 mm off the body on their own.
Joined first, they inherit the main garment's placement and the problem disappears.

The join keeps one material per piece, so each keeps its own texture — that is normal for
GTA clothing, and Pre-Flight will confirm it rather than telling you to merge them.

### The last few millimetres are yours

The landmark fit lands within a few millimetres at every joint it can measure, and that is
not always the same as looking right — a least-squares fit leaves a small residual by
construction. On one sweater it read as the neck and cuffs sitting a touch low and the hem
a touch short, while the bust was exactly where it belonged.

**Nudge up** and **Size** in the redo panel (press **F9** straight after fitting) are the
last word. They re-apply without re-running the fit, so you can dial a number in and watch
it move.

**Size scales about the chest, not the hem.** That is deliberate: the bust is the landmark
the fit gets right and the one you notice when it is wrong, so growing the garment raises
the neck, lengthens the sleeves and drops the hem while leaving the chest alone. On that
sweater, 107% raised the neck 19 mm and dropped the hem 28 mm while the bust moved 3 mm.

Scaling about the hem was tried first and is wrong for the same reason — it lifts the bust
off the body.

What the fit still cannot do is change the garment's shape. A bandeau top cut for a
slimmer figure will sit below a larger bust however well it is placed; that is sculpting
or [Drape](../tools/drape.md), not fitting.

### About the scale

The scale estimates tell the same story. The bounding box guessed 1.64, 1.69 and 1.03 for
the three — wildly inconsistent, because a bikini's box says nothing about how tall its
wearer is. Matching bones gave 1.19, 1.02 and 0.91, which is what you would expect between
two human figures.

Why a bikini defeats a bounding box is worth spelling out: the box of a bra and briefs
tells you nothing about the body, and the garment arrives a metre away from where the body
is, so there is no overlap to measure against either. Bone names have neither problem — a
vertex in `Spine1` belongs at the body's `Spine1` whatever the scale or the origin.

## When it still does not fit

Steps 4 and 5 do the rough work. If it is nearly right but not quite:

* **Fit to Reference Garment** — if you have a FiveM garment that already fits perfectly,
  use that as the template instead of the body. This often lands closest.
* **Drape onto Body** — let the fabric fall into place with physics. See [Drape](../tools/drape.md).
* **Smooth-Fit Skirt/Dress (Lattice)** — for skirts and dresses that should follow the
  hips without being squashed flat.

## If the mesh is a "triangle soup"

Models ripped from other games often arrive as loose triangles with no connected surface.
It looks perfectly fine in Blender, but comes apart the moment you weight it.

**Pre-Flight Check** detects this and tells you. The fix is
[Repair Mesh](../tools/repair-mesh.md).

## Too many polygons

Models built for film, or for other games, are often far too heavy for GTA.
**Reduce Polys (FiveM limits)** brings them under the limits. See
[LODs and limits](../tools/lods-and-limits.md).
