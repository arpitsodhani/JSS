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
    high = max(a)
    low = min(a)
    spread = high - low
    if spread > k:
        if spread > k + 1 or a.count(high) > 1:
            return "Jerry"
    return "Tom" if sum(a) % 2 == 1 else "Jerry"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, a in read_input():
        out.append(solve_case(n, k, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
