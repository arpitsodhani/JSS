import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        f = data[pos + 1]
        a = data[pos + 2]
        b = data[pos + 3]
        pos += 4
        cases.append((f, a, b, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: charge_used :: (a: int, b: int, moments: list[int]) -> int ---
def charge_used(a, b, moments):
    total = 0
    clock = 0
    for moment in moments:
        gap = (moment - clock) * a
        total += gap if gap < b else b
        clock = moment
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for f, a, b, moments in read_input():
        out.append("YES" if charge_used(a, b, moments) < f else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
