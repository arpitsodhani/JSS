import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    a = data[0]
    b = data[1]
    n = data[2]
    queries = []
    pos = 3
    for _ in range(n):
        queries.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return a, b, queries

# --- clause: solve_query :: (a: int, b: int, l: int, t: int, m: int) -> int ---
def solve_query(a, b, l, t, m):
    first = a + (l - 1) * b
    if first > t:
        return -1
    limit = (t - a) // b + 1
    budget = t * m
    best = l
    step = 1
    while step <= limit - l:
        step *= 2
    while step:
        candidate = best + step
        if candidate <= limit:
            span = candidate - l + 1
            if (first + a + (candidate - 1) * b) * span // 2 <= budget:
                best = candidate
        step //= 2
    return best

# --- clause: main :: () -> None ---
def main():
    a, b, queries = read_input()
    out = []
    for l, t, m in queries:
        out.append(str(solve_query(a, b, l, t, m)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
