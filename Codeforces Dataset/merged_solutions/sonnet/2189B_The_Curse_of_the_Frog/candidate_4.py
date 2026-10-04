import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        jumps = []
        for _ in range(n):
            jumps.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((n, x, jumps))
    return cases


# --- clause: fewest_rollbacks :: (n: int, x: int, jumps: list[tuple[int, int, int]]) -> int ---
def fewest_rollbacks(n, x, jumps):
    reach = 0
    step = 0
    for jump in jumps:
        a, b, c = jump
        reach += a * (b - 1)
        here = a * b - c
        if here > step:
            step = here
    if reach >= x:
        return 0
    if step < 1:
        return -1
    left = x - reach
    rounds = left // step
    if left % step:
        rounds += 1
    return rounds


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, jumps in read_input():
        out.append(str(fewest_rollbacks(n, x, jumps)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
