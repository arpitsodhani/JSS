import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        c = data[pos + 1]
        d = data[pos + 2]
        pos += 3
        cases.append((n, c, d, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: solve_case :: (n: int, c: int, d: int, a: list[int]) -> int ---
def solve_case(n, c, d, a):
    values = sorted(set(a))
    best = n * c + d
    for i, value in enumerate(values, start=1):
        cost = (n - i) * c + (value - i) * d
        if cost < best:
            best = cost
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, c, d, a in read_input():
        out.append(str(solve_case(n, c, d, a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
