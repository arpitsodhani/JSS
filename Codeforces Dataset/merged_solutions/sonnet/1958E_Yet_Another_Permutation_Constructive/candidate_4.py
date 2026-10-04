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
    total = len(values)
    sizes = [total]
    level = k
    while level > 1:
        sizes.append((1 << (level - 2)) + 1)
        level -= 1
    current = list(values[total - sizes[-1]:])
    for index in range(len(sizes) - 2, -1, -1):
        outer = sizes[index]
        keep = sizes[index + 1]
        pool = values[total - outer:total - keep]
        cut = len(pool) - keep + 1
        merged = list(pool[:cut])
        gaps = pool[cut:]
        for i, survivor in enumerate(current):
            merged.append(survivor)
            if i < len(gaps):
                merged.append(gaps[i])
        current = merged
    return current

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
