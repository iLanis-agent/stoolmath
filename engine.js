(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function heightPlan(counterCm, gapLow, gapHigh) {
    if (!(counterCm > 0)) return { error: "the counter height must be positive" };
    if (!(gapLow >= 0) || !(gapHigh >= gapLow)) return { error: "the knee gap must be a range from low to high, zero or more" };
    var low = round1(counterCm - gapHigh);
    var high = round1(counterCm - gapLow);
    if (!(low > 0)) return { error: "the gap is taller than the counter" };
    var verdict;
    if (counterCm < 75) verdict = "a table-height counter";
    else if (counterCm < 92) verdict = "a kitchen counter";
    else if (counterCm < 105) verdict = "a tall counter";
    else verdict = "a bar-height counter";
    return { low: low, high: high, verdict: verdict };
  }

  function spacePlan(lenCm, perStoolCm) {
    if (!(lenCm > 0) || !(perStoolCm > 0)) return { error: "the counter length and the labeled width must be positive" };
    var stools = Math.floor(lenCm / perStoolCm);
    if (stools < 1) return { error: "the counter is shorter than one labeled seat width" };
    var leftover = round1(lenCm - stools * perStoolCm);
    var verdict;
    if (stools <= 2) verdict = "an intimate row";
    else if (stools <= 4) verdict = "a family row";
    else verdict = "a long bar";
    return { stools: stools, leftover: leftover, verdict: verdict };
  }

  function footPlan(seatCm, dropCm) {
    if (!(seatCm > 0)) return { error: "the seat height must be positive" };
    if (!(dropCm >= 0)) return { error: "the drop cannot be negative" };
    var footrest = round1(seatCm - dropCm);
    if (!(footrest > 0)) return { error: "the drop is more than the seat height" };
    var verdict;
    if (seatCm < 50) verdict = "a low seat";
    else if (seatCm < 65) verdict = "a table-height seat";
    else if (seatCm < 80) verdict = "a counter-height seat";
    else verdict = "a bar-height seat";
    return { footrest: footrest, verdict: verdict };
  }

  function renderHeight(r, counterCm, gapLow, gapHigh) {
    return "A counter " + counterCm + " cm tall with a labeled knee gap of " + gapLow + "-" + gapHigh + " cm seats best at " + r.low + "-" + r.high + " cm - " + r.verdict + ".";
  }

  function renderSpace(r, lenCm, perStoolCm) {
    return "A counter " + lenCm + " cm long at a labeled " + perStoolCm + " cm a stool fits " + plural(r.stools, "stool") + " with " + r.leftover + " cm to spare - " + r.verdict + ".";
  }

  function renderFoot(r, seatCm, dropCm) {
    return "A seat " + seatCm + " cm tall wants its footrest near " + r.footrest + " cm, a labeled " + dropCm + " cm below - " + r.verdict + ".";
  }

  var api = { heightPlan: heightPlan, spacePlan: spacePlan, footPlan: footPlan, renderHeight: renderHeight, renderSpace: renderSpace, renderFoot: renderFoot };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.StoolMath = api;
})(this);
