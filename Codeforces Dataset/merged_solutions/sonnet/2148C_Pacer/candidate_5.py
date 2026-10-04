import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        m = raw[reader + 1]
        reader += 2
        wants = []
        for _ in range(n):
            wants.append((raw[reader], raw[reader + 1]))
            reader += 2
        cases.append((m, wants))
    return cases


# --- clause: most_points :: (m: int, wants: list[tuple[int, int]]) -> int ---
def most_points(m, wants):
    amount = 0
    clock = 0
    side = 0
    for moment, want in wants:
        gap = moment - clock
        if (gap - (want ^ side)) % 2:
            gap -= 1
        amount += gap
        clock = moment
        side = want
    return amount + m - clock


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, wants in read_input():
        out.append(most_points(m, wants))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
