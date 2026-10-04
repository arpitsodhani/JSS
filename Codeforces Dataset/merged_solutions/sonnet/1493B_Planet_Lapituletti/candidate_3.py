import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        h = int(data[pos])
        m = int(data[pos + 1])
        stamp = data[pos + 2]
        pos += 3
        cases.append((h, m, int(stamp[0:2]), int(stamp[3:5])))
    return cases


# --- clause: mirrors_well :: (h: int, m: int, hours: int, minutes: int) -> bool ---
def mirrors_well(h, m, hours, minutes):
    shown = "%02d%02d" % (hours, minutes)
    table = {"0": "0", "1": "1", "2": "5", "5": "2", "8": "8"}
    flipped = []
    for ch in reversed(shown):
        if ch not in table:
            return False
        flipped.append(table[ch])
    text = "".join(flipped)
    return int(text[:2]) < h and int(text[2:]) < m


# --- clause: next_moment :: (h: int, m: int, hours: int, minutes: int) -> str ---
def next_moment(h, m, hours, minutes):
    span = h * m
    start = hours * m + minutes
    moment = start
    while True:
        hh = moment // m
        mm = moment - hh * m
        if mirrors_well(h, m, hh, mm):
            return "%02d:%02d" % (hh, mm)
        moment += 1
        if moment == span:
            moment = 0
        if moment == start:
            return "%02d:%02d" % (hours, minutes)


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, hours, minutes in read_input():
        out.append(next_moment(h, m, hours, minutes))
    print("\n".join(out))


if __name__ == "__main__":
    main()
