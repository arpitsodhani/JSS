import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        m = fields[offset + 1]
        offset += 2
        wants = []
        for _ in range(n):
            wants.append((fields[offset], fields[offset + 1]))
            offset += 2
        cases.append((m, wants))
    return cases


# --- clause: most_points :: (m: int, wants: list[tuple[int, int]]) -> int ---
def most_points(m, wants):
    summed = 0
    clock = 0
    side = 0
    for moment, want in wants:
        gap = moment - clock
        if (gap - (want ^ side)) % 2:
            gap -= 1
        summed += gap
        clock = moment
        side = want
    return summed + m - clock


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, wants in read_input():
        out.append(most_points(m, wants))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
