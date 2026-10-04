import sys

LIMIT = 200001


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases


# --- clause: build_prefix :: () -> list[int] ---
def build_prefix():
    prefix = [0] * LIMIT
    for value in range(1, LIMIT):
        depth = 0
        rest = value
        while rest:
            rest //= 3
            depth += 1
        prefix[value] = prefix[value - 1] + depth
    return prefix


# --- clause: solve_case :: (l: int, r: int, prefix: list[int]) -> int ---
def solve_case(l, r, prefix):
    single = prefix[l] - prefix[l - 1]
    return prefix[r] - prefix[l - 1] + single


# --- clause: main :: () -> None ---
def main():
    prefix = build_prefix()
    out = []
    for l, r in read_input():
        out.append(str(solve_case(l, r, prefix)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
