import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        wants = []
        for _ in range(n):
            wants.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((m, wants))
    return cases


# --- clause: most_points :: (m: int, wants: list[tuple[int, int]]) -> int ---
def most_points(m, wants):
    total = 0
    clock = 0
    side = 0
    for moment, want in wants:
        gap = moment - clock
        if (gap - (want ^ side)) % 2:
            gap -= 1
        total += gap
        clock = moment
        side = want
    return total + m - clock


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, wants in read_input():
        out.append(most_points(m, wants))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
