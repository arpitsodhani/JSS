import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        m = numbers[cursor + 1]
        cursor += 2
        wants = []
        for _ in range(n):
            wants.append((numbers[cursor], numbers[cursor + 1]))
            cursor += 2
        cases.append((m, wants))
    return cases


# --- clause: most_points :: (m: int, wants: list[tuple[int, int]]) -> int ---
def most_points(m, wants):
    idle = 0
    clock = 0
    side = 0
    for moment, want in wants:
        if (moment - clock) % 2 != (want ^ side):
            idle += 1
        clock = moment
        side = want
    return m - idle


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, wants in read_input():
        out.append(most_points(m, wants))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
