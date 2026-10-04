import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        a = int(data[pos + 1])
        pos += 2
        marbles = list(map(int, data[pos:pos + n]))
        pos += n
        cases.append((a, marbles))
    return cases


# --- clause: pick_number :: (a: int, marbles: list[int]) -> int ---
def pick_number(a, marbles):
    lo = 0
    hi = len(marbles)
    while lo < hi:
        mid = (lo + hi) // 2
        if marbles[mid] < a:
            lo = mid + 1
        else:
            hi = mid
    below = lo
    lo = 0
    hi = len(marbles)
    while lo < hi:
        mid = (lo + hi) // 2
        if marbles[mid] <= a:
            lo = mid + 1
        else:
            hi = mid
    above = len(marbles) - lo
    if below > above:
        return a - 1
    return a + 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, marbles in read_input():
        out.append(str(pick_number(a, marbles)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
