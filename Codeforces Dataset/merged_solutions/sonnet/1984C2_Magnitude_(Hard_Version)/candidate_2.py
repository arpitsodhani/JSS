import sys

MOD = 998244353


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    n = len(a)
    prefix = []
    running = 0
    for value in a:
        running += value
        prefix.append(running)
    lowest = min(prefix)
    if lowest >= 0:
        return pow(2, n, MOD)
    total = 0
    free = 0
    for i, value in enumerate(prefix):
        if value == lowest:
            total += pow(2, free + n - i - 1, MOD)
        if value >= 0:
            free += 1
    return total % MOD

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
