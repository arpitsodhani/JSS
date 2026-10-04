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
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = power[i - 1] * 2 % MOD
    running = 0
    lowest = 0
    for value in a:
        running += value
        if running < lowest:
            lowest = running
    if lowest == 0:
        return power[n]
    total = 0
    running = 0
    free = 0
    position = 0
    while position < n:
        running += a[position]
        position += 1
        if running == lowest:
            total += power[free] * power[n - position]
        if running >= 0:
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
