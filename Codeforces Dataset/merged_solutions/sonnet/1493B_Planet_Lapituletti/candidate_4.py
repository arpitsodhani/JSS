import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        h = int(data[3 * i + 1])
        m = int(data[3 * i + 2])
        stamp = data[3 * i + 3]
        cases.append((h, m, int(stamp[0:2]), int(stamp[3:5])))
    return cases


# --- clause: mirrors_well :: (h: int, m: int, hours: int, minutes: int) -> bool ---
def mirrors_well(h, m, hours, minutes):
    flip = (0, 1, 5, -1, -1, 2, -1, -1, 8, -1)
    h_hi = hours // 10
    h_lo = hours % 10
    m_hi = minutes // 10
    m_lo = minutes % 10
    if flip[h_hi] < 0 or flip[h_lo] < 0:
        return False
    if flip[m_hi] < 0 or flip[m_lo] < 0:
        return False
    if flip[m_lo] * 10 + flip[m_hi] >= h:
        return False
    if flip[h_lo] * 10 + flip[h_hi] >= m:
        return False
    return True


# --- clause: next_moment :: (h: int, m: int, hours: int, minutes: int) -> str ---
def next_moment(h, m, hours, minutes):
    good = []
    for hh in range(h):
        for mm in range(m):
            if mirrors_well(h, m, hh, mm):
                good.append(hh * m + mm)
    if not good:
        return "%02d:%02d" % (hours, minutes)
    start = hours * m + minutes
    pick = good[0]
    for moment in good:
        if moment >= start:
            pick = moment
            break
    return "%02d:%02d" % (pick // m, pick % m)


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(next_moment(case[0], case[1], case[2], case[3]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
