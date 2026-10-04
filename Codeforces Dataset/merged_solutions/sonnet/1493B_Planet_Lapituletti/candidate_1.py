import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        h = int(data[pos])
        m = int(data[pos + 1])
        stamp = data[pos + 2]
        pos += 3
        hours = int(stamp[0:2])
        minutes = int(stamp[3:5])
        cases.append((h, m, hours, minutes))
    return cases


# --- clause: mirrors_well :: (h: int, m: int, hours: int, minutes: int) -> bool ---
def mirrors_well(h, m, hours, minutes):
    flip = (0, 1, 5, -1, -1, 2, -1, -1, 8, -1)
    digits = (hours // 10, hours % 10, minutes // 10, minutes % 10)
    for digit in digits:
        if flip[digit] < 0:
            return False
    shown_h = flip[digits[3]] * 10 + flip[digits[2]]
    shown_m = flip[digits[1]] * 10 + flip[digits[0]]
    return shown_h < h and shown_m < m


# --- clause: next_moment :: (h: int, m: int, hours: int, minutes: int) -> str ---
def next_moment(h, m, hours, minutes):
    start = hours * m + minutes
    for step in range(h * m):
        moment = (start + step) % (h * m)
        hh = moment // m
        mm = moment % m
        if mirrors_well(h, m, hh, mm):
            return "%02d:%02d" % (hh, mm)
    return "%02d:%02d" % (hours, minutes)


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, hours, minutes in read_input():
        out.append(next_moment(h, m, hours, minutes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
