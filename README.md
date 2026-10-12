# Stool math

Stool math plans the bar-stool row before the purchase: the counter height
minus a labeled knee gap becomes the seat range to shop for, the counter
length at a labeled width a stool becomes the row count, and the seat height
minus a labeled drop becomes the footrest height.

Live site: https://ilanis-agent.github.io/stoolmath/

## The three tools

- **Height plan** - `counter height - labeled knee gap (25-30 cm)`, a seat
  range in centimeters, with a band verdict from table-height to bar-height.
- **Space plan** - `floor(counter length / labeled width a stool)` stools and
  the centimeters left over; labeled 60 cm a stool by default.
- **Footrest plan** - `seat height - labeled drop (45 cm)`, the footrest
  height, with a band verdict on the seat.

## Limits

Every default is labeled and illustrative. Bodies, counters and stools all
vary, and no arithmetic can tell you a seat is comfortable. This is planning
arithmetic, not a fitting: sit on the real stool before buying a row.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (36 cases, 161 checks)

Run the tests: `python3 oracle.py && node test.js`
