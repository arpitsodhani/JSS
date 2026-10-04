import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    q = tokens[0]
    idx = 1
    cases = []
    for _ in range(q):
        n = tokens[idx]
        k = tokens[idx + 1]
        b = tokens[idx + 2]
        s = tokens[idx + 3]
        cases.append((n, k, b, s))
        idx += 4
    return cases


# --- clause: solve_case :: (n: int, k: int, b: int, s: int) -> str ---
def solve_case(n, k, b, s):
    floor_sum = k * b
    ceiling = floor_sum + n * (k - 1)
    if not (floor_sum <= s <= ceiling):
        return "-1"
    result = [0] * n
    big = min(s, floor_sum + k - 1)
    result[0] = big
    spare = s - big
    for i in range(1, n):
        share = min(k - 1, spare)
        result[i] = share
        spare -= share
    return " ".join(str(v) for v in result)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, k, b, s in read_input():
        lines.append(solve_case(n, k, b, s))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
