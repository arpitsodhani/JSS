import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        f = fields[cursor + 1]
        a = fields[cursor + 2]
        b = fields[cursor + 3]
        cursor += 4
        cases.append((f, a, b, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: charge_used :: (a: int, b: int, moments: list[int]) -> int ---
def charge_used(a, b, moments):
    tally = 0
    clock = 0
    for moment in moments:
        gap = (moment - clock) * a
        tally += gap if gap < b else b
        clock = moment
    return tally


# --- clause: main :: () -> None ---
def main():
    out = []
    for f, a, b, moments in read_input():
        out.append("YES" if charge_used(a, b, moments) < f else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
