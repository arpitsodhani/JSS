import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        f = numbers[reader + 1]
        a = numbers[reader + 2]
        b = numbers[reader + 3]
        reader += 4
        cases.append((f, a, b, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: charge_used :: (a: int, b: int, moments: list[int]) -> int ---
def charge_used(a, b, moments):
    gaps = []
    clock = 0
    for moment in moments:
        gaps.append(moment - clock)
        clock = moment
    total = 0
    for gap in gaps:
        cost = gap * a
        if b < cost:
            cost = b
        total += cost
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for f, a, b, moments in read_input():
        out.append("YES" if charge_used(a, b, moments) < f else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
