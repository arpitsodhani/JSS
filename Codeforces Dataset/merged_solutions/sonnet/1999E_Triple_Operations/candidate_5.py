import sys

LIMIT = 200001


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        l = int(data[pos])
        pos += 1
        r = int(data[pos])
        pos += 1
        cases.append((l, r))
    return cases


# --- clause: build_prefix :: () -> list[int] ---
def build_prefix():
    steps = [0] * LIMIT
    for value in range(1, LIMIT):
        steps[value] = steps[value // 3] + 1
    prefix = [0] * LIMIT
    running = 0
    for value in range(1, LIMIT):
        running += steps[value]
        prefix[value] = running
    return prefix


# --- clause: solve_case :: (l: int, r: int, prefix: list[int]) -> int ---
def solve_case(l, r, prefix):
    left = prefix[l - 1]
    return (prefix[r] - left) + (prefix[l] - left)


# --- clause: main :: () -> None ---
def main():
    prefix = build_prefix()
    out = []
    for l, r in read_input():
        out.append(str(solve_case(l, r, prefix)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
