import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def height_plan(counterCm, gapLow, gapHigh):
    if not (counterCm > 0):
        return {"error": "the counter height must be positive"}
    if not (gapLow >= 0) or not (gapHigh >= gapLow):
        return {"error": "the knee gap must be a range from low to high, zero or more"}
    low = round1(counterCm - gapHigh)
    high = round1(counterCm - gapLow)
    if not (low > 0):
        return {"error": "the gap is taller than the counter"}
    if counterCm < 75: verdict = "a table-height counter"
    elif counterCm < 92: verdict = "a kitchen counter"
    elif counterCm < 105: verdict = "a tall counter"
    else: verdict = "a bar-height counter"
    return {"low": low, "high": high, "verdict": verdict}

def space_plan(lenCm, perStoolCm):
    if not (lenCm > 0) or not (perStoolCm > 0):
        return {"error": "the counter length and the labeled width must be positive"}
    stools = math.floor(lenCm / perStoolCm)
    if stools < 1:
        return {"error": "the counter is shorter than one labeled seat width"}
    leftover = round1(lenCm - stools * perStoolCm)
    if stools <= 2: verdict = "an intimate row"
    elif stools <= 4: verdict = "a family row"
    else: verdict = "a long bar"
    return {"stools": stools, "leftover": leftover, "verdict": verdict}

def foot_plan(seatCm, dropCm):
    if not (seatCm > 0):
        return {"error": "the seat height must be positive"}
    if not (dropCm >= 0):
        return {"error": "the drop cannot be negative"}
    footrest = round1(seatCm - dropCm)
    if not (footrest > 0):
        return {"error": "the drop is more than the seat height"}
    if seatCm < 50: verdict = "a low seat"
    elif seatCm < 65: verdict = "a table-height seat"
    elif seatCm < 80: verdict = "a counter-height seat"
    else: verdict = "a bar-height seat"
    return {"footrest": footrest, "verdict": verdict}

def render_height(r, counterCm, gapLow, gapHigh):
    return ("A counter " + fmt(counterCm) + " cm tall with a labeled knee gap of " + fmt(gapLow) + "-" + fmt(gapHigh)
            + " cm seats best at " + fmt(r["low"]) + "-" + fmt(r["high"]) + " cm - " + r["verdict"] + ".")

def render_space(r, lenCm, perStoolCm):
    return ("A counter " + fmt(lenCm) + " cm long at a labeled " + fmt(perStoolCm) + " cm a stool fits "
            + plural(r["stools"], "stool") + " with " + fmt(r["leftover"]) + " cm to spare - " + r["verdict"] + ".")

def render_foot(r, seatCm, dropCm):
    return ("A seat " + fmt(seatCm) + " cm tall wants its footrest near " + fmt(r["footrest"]) + " cm, a labeled "
            + fmt(dropCm) + " cm below - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[90,25,30],[75,25,30],[105,25,30],[110,25,30],[60,25,30],[92.5,25,30],[90,20,25],[0,25,30],[90,-1,30],[90,30,25],[90,95,100],[40,25,30]]:
    add("heightPlan", height_plan, render_height, a)
for a in [[240,60],[120,60],[150,60],[480,60],[59,60],[0,60],[240,0],[300,65],[200,70],[61.5,60],[305.5,65],[1000,60]]:
    add("spacePlan", space_plan, render_space, a)
for a in [[65,45],[45,45],[75,45],[85,45],[60,40],[62.5,45],[0,45],[65,-5],[40,45],[45,45.5],[90,45],[55,42]]:
    add("footPlan", foot_plan, render_foot, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
