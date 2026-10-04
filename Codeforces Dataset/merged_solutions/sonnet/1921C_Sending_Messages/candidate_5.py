import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        f = raw[offset + 1]
        a = raw[offset + 2]
        b = raw[offset + 3]
        offset += 4
        cases.append((f, a, b, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: charge_used :: (a: int, b: int, moments: list[int]) -> int ---
def charge_used(a, b, moments):
    running = 0
    clock = 0
    for moment in moments:
        gap = (moment - clock) * a
        running += gap if gap < b else b
        clock = moment
    return running


# --- clause: main :: () -> None ---
def main():
    out = []
    for f, a, b, moments in read_input():
        out.append("YES" if charge_used(a, b, moments) < f else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
