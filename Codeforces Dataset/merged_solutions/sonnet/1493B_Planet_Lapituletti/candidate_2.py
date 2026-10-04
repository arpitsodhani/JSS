import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    idx = 1
    for _ in range(t):
        h, m = int(data[idx]), int(data[idx + 1])
        stamp = data[idx + 2].decode()
        idx += 3
        cases.append((h, m, int(stamp[:2]), int(stamp[3:])))
    return cases


# --- clause: mirrors_well :: (h: int, m: int, hours: int, minutes: int) -> bool ---
def mirrors_well(h, m, hours, minutes):
    flip = {0: 0, 1: 1, 2: 5, 5: 2, 8: 8}
    a, b = divmod(hours, 10)
    c, d = divmod(minutes, 10)
    for digit in (a, b, c, d):
        if digit not in flip:
            return False
    if flip[d] * 10 + flip[c] >= h:
        return False
    return flip[b] * 10 + flip[a] < m


# --- clause: next_moment :: (h: int, m: int, hours: int, minutes: int) -> str ---
def next_moment(h, m, hours, minutes):
    for extra in range(h + 1):
        hh = (hours + extra) % h
        first = minutes if extra == 0 else 0
        last = m if extra < h else minutes + 1
        for mm in range(first, last):
            if mirrors_well(h, m, hh, mm):
                return "%02d:%02d" % (hh, mm)
    return "%02d:%02d" % (hours, minutes)


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, m, hours, minutes in read_input():
        out.append(next_moment(h, m, hours, minutes))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
