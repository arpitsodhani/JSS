import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# --- clause: build :: (values: list[int], k: int) -> list[int] ---
def build(values, k):
    if k == 1:
        return list(values)
    total = len(values)
    keep = (1 << (k - 2)) + 1
    survivors = build(values[total - keep:], k - 1)
    fillers = values[:total - keep]
    gaps = fillers[len(fillers) - keep + 1:]
    result = fillers[:len(fillers) - keep + 1]
    for survivor, filler in zip(survivors, gaps):
        result.append(survivor)
        result.append(filler)
    result.append(survivors[-1])
    return result

# --- clause: solve_case :: (n: int, k: int) -> str ---
def solve_case(n, k):
    if (1 << (k - 1)) >= n:
        return "-1"
    return " ".join(map(str, build(list(range(1, n + 1)), k)))


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k in read_input():
        out.append(solve_case(n, k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
