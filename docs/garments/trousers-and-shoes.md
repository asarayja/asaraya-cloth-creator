# Trousers, and the shoe they are worn with

Two things go wrong at the bottom of a trouser leg, and they are unrelated.

## The hem lands in the floor

A trouser fitted by landmarks comes out too long. Measured on two imported trousers, the hem
landed **64 mm and 61 mm below the plane the ped stands on** — below the sole of every flat
shoe in the reference set. In game the leg disappears into the pavement.

**Fit to Body now lifts it.** The band from the garment's lowest point up to 80 mm above
the ground is squeezed into the band from the ground up to 80 mm; everything higher is
untouched, the two meet exactly at the top of the band so there is no step, and the order
of the vertices is kept so the hem holds its shape instead of being flattened onto one
line. Both test trousers now finish 4 mm and 10 mm above the ground.

It is a function of height alone, which is what makes it safe on a game mesh: two vertices
sharing a position share a z and move together, so no UV seam can open.

Length *over* a shoe is a design choice and is left alone. Only cloth below the sole is
touched, so a garment that never reaches the ground never moves.

## The shoe and the trouser have to agree

**Fit Trousers to Shoes** handles this, and it genuinely goes both ways — skinny jeans sit
over a boot, and a boot is just as often worn over the trouser. Nothing in the geometry can
tell you which one a garment wants, so you choose.

Import the shoe into the scene first: its height is then read straight off it, and for
*Trousers cover the shoe* its actual shape is what the leg is widened to.

| Worn how | What happens |
| --- | --- |
| **Trousers cover the shoe** | The leg is widened until the shoe fits inside it |
| **Trousers end above the shoe** | The leg is shortened to just above the shoe's top |

### Trousers cover the shoe

How wide the shoe is, band by band around the leg's own axis, becomes a floor: any trouser
vertex narrower than that is pushed straight out until it clears, plus the clearance.
Radially, so the leg keeps its section instead of being dented, and only outwards, so a leg
already wide enough is untouched.

**It stops at the ankle**, and that is not a shortcut. Past the ankle the radius around the
leg axis is the *foot* sticking out forwards, not the shaft: on a knee-high boot it runs
66–95 mm the whole way down the calf, then balloons to 125 mm just below the ankle and
191 mm at the toes. Widening a 65 mm trouser to 133 mm there turned the bottom of the leg
into flaps. A trouser does not have to encircle the foot — the hem hangs over it.

Judge the result by the shaft, which is the part that belongs inside the trouser. Shoe
geometry pushing through:

| Boot | Shaft, above the ankle | Foot, below it |
| --- | --- | --- |
| reaching 430 mm up the calf | 158 → **2** of 759 | 1059 → 600 of 1305 |
| mid boot | 1082 → **154** of 4598 | 501 → 366 of 1270 |

The foot staying outside is correct — that is the shoe being visible. A single number over
the whole shoe mixes the two and reads as a regression when the shaft has in fact gone
almost perfectly inside.

### Trousers end above the shoe

The band from the hem up to the knee is squeezed so its bottom lands just above the shoe
and its top stays where it is. The waist and seat do not move and the two bands meet at the
knee with no step. All three test shoes landed exactly 8 mm above their tops.

**A knee-high boot is the exception.** One reference boot reaches 19 mm *past* the knee
joint, and pivoting on the knee then left the hem at the knee instead of above the boot.
The hip takes over there, which turns the trousers into breeches — which is what ending
above a knee-high boot means.

## It cleans up after itself

Both modes finish with [poke-through](../tools/poke-through.md) and another hem lift.

That is not housekeeping. Squeezing a leg upwards carries narrow cloth onto a wider part of
the thigh, and the thigh comes straight through it — plainly visible in a render even
though the hem had landed exactly where it was asked to. The tidy pass pushed 2065 vertices
clear and the trousers came out solid.

Seams held at **0 opened** across every combination tested.

## Common problems

**"No shoe in the scene and no height given"** — import the shoe, or type how far up the
leg it reaches in millimetres.

**"Covering the shoe needs the shoe itself in the scene"** — a height is enough to shorten
a leg, but widening one needs the shoe's actual shape.

**The trousers still clip the boot** — raise `Clearance`, or the boot is wider than the
trouser can reasonably become; end above it instead.

**The hem is at the ground but I wanted it longer** — it is capped at the ground on
purpose. Anything below the sole is in the pavement.
