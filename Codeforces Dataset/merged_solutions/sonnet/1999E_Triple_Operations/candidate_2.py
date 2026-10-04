import sys

LIMIT = 200001


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    numbers = list(map(int, data[1:1 + 2 * t]))
    return list(zip(numbers[0::2], numbers[1::2]))


# --- clause: build_prefix :: () -> list[int] ---
def build_prefix():
    prefix = [0] * LIMIT
    power = 3
    depth = 1
    for value in range(1, LIMIT):
        if value >= power:
            power *= 3
            depth += 1
        prefix[value] = prefix[value - 1] + depth
    return prefix


# --- clause: solve_case :: (l: int, r: int, prefix: list[int]) -> int ---
def solve_case(l, r, prefix):
    return prefix[r] - prefix[l - 1] + prefix[l] - prefix[l - 1]


# --- clause: main :: () -> None ---
def main():
    prefix = build_prefix()
    out = []
    for l, r in read_input():
        out.append(str(solve_case(l, r, prefix)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
