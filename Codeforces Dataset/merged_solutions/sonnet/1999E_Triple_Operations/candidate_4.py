import sys

LIMIT = 200001


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(t)]


# --- clause: build_prefix :: () -> list[int] ---
def build_prefix():
    prefix = [0] * LIMIT
    low = 1
    depth = 1
    while low < LIMIT:
        high = low * 3
        if high > LIMIT:
            high = LIMIT
        for value in range(low, high):
            prefix[value] = prefix[value - 1] + depth
        low = high
        depth += 1
    return prefix


# --- clause: solve_case :: (l: int, r: int, prefix: list[int]) -> int ---
def solve_case(l, r, prefix):
    whole = prefix[r] - prefix[l - 1]
    cheapest = prefix[l] - prefix[l - 1]
    return whole + cheapest


# --- clause: main :: () -> None ---
def main():
    prefix = build_prefix()
    out = []
    for pair in read_input():
        out.append(str(solve_case(pair[0], pair[1], prefix)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
