import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((n, k, data[pos:pos + n]))
        pos += n
    return cases

# --- clause: solve_case :: (n: int, k: int, a: list[int]) -> str ---
def solve_case(n, k, a):
    high = a[0]
    low = a[0]
    tops = 0
    total = 0
    for value in a:
        total += value
        if value >= high:
            if value > high:
                high = value
                tops = 0
            tops += 1
        if value < low:
            low = value
    if high - low == k + 1 and tops == 1:
        return "Tom" if total % 2 == 1 else "Jerry"
    if high - low > k:
        return "Jerry"
    return "Tom" if total % 2 == 1 else "Jerry"

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, a in read_input():
        out.append(solve_case(n, k, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
