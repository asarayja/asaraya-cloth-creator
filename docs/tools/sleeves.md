# Sleeves

Two buttons, for two different problems. Both sit under **Fit & Placement**, and both are
meant to run **after** the garment has been fitted to the body.

| Button | Use it when |
| --- | --- |
| **Align Sleeves to Arms** | Almost always. Puts the sleeve on the arm and opens the cuff for the hand |
| **Tighten Sleeves to Arms** | Optional. The sleeve is baggier than you meant it to be |

**Align is the one that does the work.** It covers the arm, opens the cuff and cleans up
after itself, and on the test sweater it alone left 10 faces cutting through the body, 2 of
them at the hands.

**Tighten is a design decision, not a repair.** It narrows the sleeve, and on a garment
whose sleeves are *meant* to be wide that is damage, however good the numbers look. On the
bell-sleeved sweater it bought 2 fewer faces and cost 9 mm of sleeve width at the forearm —
a bad trade there, a good one on a sleeve that genuinely hangs too loose. Look at the
garment and decide; nothing downstream needs it.


## Do not run it on a sleeveless garment

Measured on a sleeveless dress imported as a `.glb`, Align moved **1773 of 3735 vertices
by a median 59 mm**, up to 118 mm. It wrecked it.

The reason is the pose. The arms hang down beside the hips, so the flared side of a dress
is nearer the arm than it is to the spine — and the arm passes *inside* the dress, so the
cloth genuinely wraps it. Three separate tests were tried to tell the two apart and none
of them separates on real data:

* cloth in every band from armpit to wrist — the dress fills them all
* cloth going right around the arm — the dress does, because the arm is inside it
* distance to the arm — sleeves measure 65–79 mm and the non-sleeves 78–87 mm, overlapping

So it is your judgement, not the tool's. **If the garment has no sleeves, do not press
it.** There is no undo cost to checking: Align reports both sides and what happened to
each.


## Align Sleeves to Arms

Rotates each sleeve as one rigid piece about its shoulder so the tube lies along the arm.
Optionally bends the forearm about the elbow, and stretches the cuff out to the wrist.

**It measures itself, and undoes the rotation if it made things worse.** With a Base Body
in the scene, the sleeves are measured before and after, and the rotation is kept only if
their centre lines ended closer to the arms'. Otherwise you get *"Sleeves left as they
are"* rather than a silently mangled garment.

### It is judged on where the sleeve sits, not how far it is from the body

That distinction is the whole ballgame. A sleeve can hang **beside** the arm with the
entire limb sticking out through the back of it and still score a perfectly ordinary
distance-to-the-body, because the cloth is a normal distance from *some* part of the
body — just not from the arm it belongs on. Look only at the front and it appears fine.

So what is measured is the offset between the sleeve's own centre line and the arm's. On
two imported sweaters, with the amount of arm left outside the sleeve alongside:

| Garment | Arm outside the sleeve |
| --- | --- |
| horror, left | 43.0 → **0.4 %** |
| horror, right | 46.1 → **0.4 %** |
| genser, left | 43.4 → **0.4 %** |
| genser, right | 46.9 → **0.4 %** |

Judged on distance-to-the-body, every one of those rotations looked like a regression and
was thrown away.

### What counts as a sleeve

A vertex is sleeve when it is **nearer the arm than the spine** — not simply when it sits
past the shoulder.

That distinction broke wide garments badly. The hem of a loose sweater reaches out as far
as the shoulder does, so 143 vertices sitting more than 300 mm *below* the shoulder were
picked up as sleeve and dragged towards the arm line, flinging the hem out into wings
either side of the hips. Nearest-limb keeps a wide bell sleeve, which is far from the arm
but further still from the torso, and drops the hem, which is the other way round.

It also fixed the alignment itself. Hem vertices dragged the sleeve's measured axis away
from the arm, so the rotation aimed at the wrong line. With them excluded, the arm left
outside the sleeve after Align falls from 28.7 % to **0.4 %**.

### It only touches actual sleeves

Centring cloth on the arm line is right for a sleeve and badly wrong for anything else, so
the upper arm **and** the forearm both have to carry cloth before it is touched. Measured
across six garments, cloth outboard of the shoulder comes in three shapes: a real sleeve
fills every band from armpit to wrist; a cap sleeve or strap fills only the first; a
cuff-height piece fills only the last. Pulling that last kind onto the arm line moved it
**320 mm** — it was never a sleeve.

**Both arms are judged together and taken or left as one.** Judging each side on its own
looked safer and was worse to use: on a symmetric garment the two sleeves score within a
millimetre of each other, so the check landed on opposite sides of "better" by chance and
rotated one arm only — the left on one sweater, the right on the next. A garment with one
sleeve turned and the other not is more broken than one left alone. The report names both
sides and what happened to each.

Note that the check needs **Base Body set in the panel** — that is what it measures
against. Without it there is nothing to measure and the rotation is applied unchecked.

That check earns its place. Before it existed, the button made the sleeves **worse** on
three of four imported garments — a median gap of 31.7 mm became 42.6 mm on one and
43.3 mm became 141.4 mm on another. A garment that has already been fitted by landmarks
is pointing the right way; rotating it again only swings it off the arm.

## Tighten Sleeves to Arms

Draws each sleeve in towards the arm, the way an Elastic Deform brush would, for the case
Align cannot help with: the sleeve is aimed correctly but sits too far out.

Vertices move **radially in towards the arm's own centre line**, not along the nearest
body normal. That is what keeps it looking like a sleeve — a tube pulled towards its
centre line stays a tube, whereas pushing every vertex down its nearest surface normal
flattens the cuff against the wrist.

Distances are measured **to the arm axis** too, not to whatever piece of body happens to
be nearest, and the tightening stops at the arm's own thickness in that band plus the
clearance. Measuring to the nearest surface instead made the exposed arm *worse* — 17.1 %
to 22.1 % on a measured sweater — because a sleeve hanging beside the arm reads an
ordinary distance to the torso, and closing that "gap" shrinks the tube around a centre
the arm is not at. Pulling towards a common radius about the arm both narrows the sleeve
and wraps it around the limb.

**If you use it, run Align first.** In that order on the horror sweater the arm left
outside the sleeve goes 43.0 % → 0.4 % → 1.6 % on the left and 46.1 % → 0.4 % → 1.2 % on
the right. Both buttons open the cuff and run poke-through when they finish, so there is no
required order beyond that and no third step to remember.

### Strength closes a fraction, not a fixed distance

`Strength` is the share of each vertex's gap to close. `0.5` halves the distance to the
arm everywhere; `1.0` takes it all the way down to the clearance.

A fraction rather than a fixed target is the whole point. A bell sleeve sits 45 mm off the
arm at the cuff and 12 mm at the elbow **because that is the design**. Pulling every vertex
to one clearance turned a measured test sweater into a tight tube with a hard flange where
the untouched part began — the median gap improved from 32 mm to 12 mm while the garment
lost its shape. Taking a share of each gap keeps the flare and narrows it.

| Setting | What it does |
| --- | --- |
| `Strength` | Fraction of the gap to close. Start at `0.5` |
| `Keep cuff` | How much of the sleeve, back from the hand, keeps its width. `0.30` by default |
| `Lengthen` | Millimetres to push the cuff further down the arm. Negative shortens |
| `Clearance` | Millimetres of air to leave. Set from the mesh when you press the button |
| `Also push out` | Move sleeves *tighter* than the clearance outwards too. Off by default — a snug sleeve is normal, and inflating one to a fixed distance makes it look padded |

### Clearance is set from the mesh, not fixed

A flat triangle laid over a round arm cuts into it, and the coarser the mesh the deeper it
cuts — so one clearance cannot suit every garment.

Measured on a sweater with 37.8 mm edges: tightening to a fixed 8 mm **cost coverage**,
taking faces cutting through the body from 50 to 54 even after poke-through. At 15 mm the
sleeve still came in from 75 mm to 65 mm and the count stayed at 50 — the same as leaving
it alone. Past 25 mm nothing moves at all.

So the button opens on two-fifths of the garment's median edge length, held between 5 and
25 mm. Across four garments that removed the penalty on both coarse ones and changed
nothing on the fine ones: **Tighten now costs no coverage on any of them.** Change the
number in the redo panel if you want it tighter.

### Keep cuff — the flare belongs at the far end

The correction eases in from the armhole **and back out again towards the hand**, so the
cuff keeps its width while the upper arm is drawn in.

A bell sleeve flares at the far end on purpose. On a measured test sweater the sleeve is
246 mm across at mid-forearm and 83 mm at the shoulder; narrowing both by the same
fraction gave a cuff clamped around the wrist on a garment meant to hang wide over the
hand. With `Keep cuff` at `0.30` the same run tightens the upper arm from 81 to 59 mm
while the cuff stays at 102 mm against its original 103.

Set it to `0` on a plain sleeve you want tightened all the way to the wrist.

### Lengthen — reaching further down the arm

Tightening a sleeve does not shorten it — vertices move sideways towards the arm's centre
line, never along it. But a bell that used to hang wide covers less of the hand once it is
narrowed, so it reads as shorter, and sometimes it genuinely needs to reach further.

`Lengthen` slides the sleeve down the arm, holding the armhole still and easing the stretch
in over the first 30 % so the shoulder seam does not move. Asking for 40 mm moved a
measured cuff exactly 40 mm, with 0 of 213 seams opened.

Lengthening is deliberately **not** subject to the undo-if-worse check below. Pushing a
cuff out over the hand always increases its distance to the body, because past the wrist
there is barely any body under it — which is the point of asking for it.

Drag `Strength` in the **panel at the bottom left of the viewport** after pressing the
button, and watch the sleeve move. That is the sculpt-brush feel, without a brush.

### What keeps it from breaking the garment

* **The armhole is held still** and the correction eases in over the first 30 % of the
  arm, so the seam to the torso does not tear.
* **Split vertices move together.** Game meshes are split at UV seams, where 21–100 % of a
  real garment's vertices are duplicates sitting on top of each other. Measured across six
  garments after tightening: **0 seams opened**, worst separation 0.00 mm.
* **It only pulls in**, never out, unless you turn `Also push out` on.
* **It undoes itself if it made things worse.** Pulling towards the *arm* axis moves a
  vertex away from the *torso*, so on a sleeveless top the shoulder straps get dragged off
  the body. Nothing here can tell a strap from a short sleeve by shape, so the measurement
  decides, and you are told.

### Measured results

Six garments, fitted to the body first, then tightened at `Strength 0.5`. Median gap from
the sleeve to the body, and the 95th percentile:

| Garment | Median | 95 % | Seams opened |
| --- | --- | --- | --- |
| genser | 35.4 → **18.2 mm** | 93.5 → 83.6 mm | 0 / 218 |
| horror | 31.7 → **17.0 mm** | 94.1 → 85.9 mm | 0 / 213 |
| top2 | 18.3 → **15.5 mm** | 50.0 → 44.8 mm | 0 / 651 |
| 3 | 43.3 → **40.9 mm** | 94.1 → 94.1 mm | 0 / 2776 |
| 4 | 7.2 → 7.2 mm | already inside the clearance, untouched | 0 / 1855 |

`3` moves least because most of its sleeve is already down at the arm's own thickness plus
the clearance. Lower `Clearance` if you want it closer still.

Cloth poking *into* the body never rose on any of them.

## The cuff is opened to fit the hand

Past the wrist the hand gets **wider** — the thumb and the side of the palm — while a
tapered sleeve keeps narrowing. Measured along the arm axis on the bell-sleeved test
sweater, with 1.0 at the wrist:

| Along the arm | Hand across | Sleeve at its narrowest |
| --- | --- | --- |
| 1.00 | 38 mm | 40 mm |
| 1.05 | 54 mm | **29 mm** |
| 1.10 | 64 mm | **16 mm** |
| 1.15 | 76 mm | **36 mm** |

A 16 mm opening around a 64 mm hand is the cuff sitting *between the thumb and the side of
the palm*, which is exactly what it looked like in the viewport — and no amount of
[poke-through](poke-through.md) fixes it. Pushing cloth off a thumb only drags the cuff out
of shape, because the hand is inside the sleeve and the cloth has nowhere to go. **The
opening has to get bigger.**

Both sleeve buttons now do that before anything else: every vertex out past the wrist is
moved straight out from the arm axis until it clears the widest part of the hand at its own
height, plus 6 mm. Radially, so the cuff opens like a cuff instead of being dented; only
outwards, so a sleeve already wide enough is untouched; and eased in so there is no step
where the flare begins.

| | Faces cutting through | of those, at the hands |
| --- | --- | --- |
| after Fit to Body | 76 | 28 |
| after Align, before this | 35 | 27 |
| after Align, with it | **10** | **2** |

Skin visible inside the garment ended at **0.44 % from the front and 0.30 % from the
back**, against 2.27 % and 1.91 % before any of this work.

A short sleeve never reaches past the wrist, so nothing happens to it.

## Both buttons tidy up after themselves

Moving a sleeve puts cloth somewhere new, and somewhere new can be inside the arm or the
hand. [Poke-through](poke-through.md) runs inside **Fit to Body**, which is *before* any of
this, so nothing used to clean up afterwards.

Measured on the horror sweater: Fit to Body left 26 faces cutting through around the hands,
and Align pushed that to **35** — the cuff swinging onto the thumb. Run Align and stop
there, which is the natural thing to do, and that is exactly what you see.

Both buttons now run poke-through when they finish, at eight rounds rather than the usual
three, because a sleeve that has just been rotated has moved a lot of cloth at once and
the early rounds are still finding new breaches. After Align alone the sweater is down to
**28 faces, 20 of them at the hands**, from 57 and 35.

The report tells you how many vertices were pushed clear.

## Why the arm was being missed

Both tools used to read the elbow and wrist off the **tails** of the arm bones. On the GTA
freemode skeleton every bone is a fixed 50 mm long with its tail pointing nowhere in
particular — `SKEL_L_UpperArm`'s tail sits 1 mm from its own head. That put the "elbow" on
top of the shoulder and the "wrist" at the elbow, and made the arm measure **275 mm instead
of its real 533 mm**.

Anything aimed along that axis missed. It is why Align used to swing sleeves off the arm,
and why the first version of Tighten left the whole lower half of a bell sleeve untouched:
those vertices measured past the end of an arm that was only half as long as the real one.

Both now read each joint as the **head of its own bone** — `SKEL_L_UpperArm`,
`SKEL_L_Forearm`, `SKEL_L_Hand` — falling back to tails only for a rig that lacks them.

## Common problems

**"Sleeves already sit within the clearance"** — nothing is further from the arm than the
clearance you asked for. Lower `Clearance`, or the sleeves are already fine.

**"Left alone — pulling these towards the arms measured further from the body"** — the
geometry out at the shoulders is straps or a cap sleeve, not a tube around the arm. Move
it by hand.

**The sleeve is now inside the arm** — raise `Clearance`, or lower `Strength`. Then run
[poke-through](poke-through.md) to push out what is left.

**The cuff is too short or too long** — that is length, not width. Use `Lengthen`, in
millimetres, positive or negative.

**The cuff came out too tight anyway** — raise `Keep cuff`. At `0.5` the outer half of the
sleeve is left alone entirely.

**Align Sleeves' *Stretch to wrist* does nothing** — it only fires when the cuff falls
*short* of the wrist. A bell sleeve that already hangs past the hand is not stretched;
use `Lengthen` instead.
