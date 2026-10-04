import sys

LIMIT = 200001


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases


# --- clause: build_prefix :: () -> list[int] ---
def build_prefix():
    steps = [0] * LIMIT
    prefix = [0] * LIMIT
    for value in range(1, LIMIT):
        steps[value] = steps[value // 3] + 1
        prefix[value] = prefix[value - 1] + steps[value]
    return prefix


# --- clause: solve_case :: (l: int, r: int, prefix: list[int]) -> int ---
def solve_case(l, r, prefix):
    span = prefix[r] - prefix[l - 1]
    return span + (prefix[l] - prefix[l - 1])


# --- clause: main :: () -> None ---
def main():
    prefix = build_prefix()
    out = []
    for l, r in read_input():
        out.append(str(solve_case(l, r, prefix)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
