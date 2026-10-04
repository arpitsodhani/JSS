import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        h = int(data[pos])
        pos += 1
        m = int(data[pos])
        pos += 1
        stamp = data[pos]
        pos += 1
        cases.append((h, m, int(stamp[0:2]), int(stamp[3:5])))
    return cases


# --- clause: mirrors_well :: (h: int, m: int, hours: int, minutes: int) -> bool ---
def mirrors_well(h, m, hours, minutes):
    flip = (0, 1, 5, -1, -1, 2, -1, -1, 8, -1)
    digits = [hours // 10, hours % 10, minutes // 10, minutes % 10]
    mirrored = []
    for digit in digits:
        value = flip[digit]
        if value < 0:
            return False
        mirrored.append(value)
    mirrored.reverse()
    return mirrored[0] * 10 + mirrored[1] < h and mirrored[2] * 10 + mirrored[3] < m


# --- clause: next_moment :: (h: int, m: int, hours: int, minutes: int) -> str ---
def next_moment(h, m, hours, minutes):
    hh = hours
    mm = minutes
    for _ in range(h * m):
        if mirrors_well(h, m, hh, mm):
            return "%02d:%02d" % (hh, mm)
        mm += 1
        if mm == m:
            mm = 0
            hh += 1
            if hh == h:
                hh = 0
    return "%02d:%02d" % (hours, minutes)


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, hours, minutes in read_input():
        out.append(next_moment(h, m, hours, minutes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
