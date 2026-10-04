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
    if a + (l - 1) * b > t:
        return -1
    low = l
    high = (t - a) // b + 2
    budget = t * m
    head = a + (l - 1) * b
    while low + 1 < high:
        mid = (low + high) // 2
        tail = a + (mid - 1) * b
        if (head + tail) * (mid - l + 1) // 2 <= budget:
            low = mid
        else:
            high = mid
    return low

# --- clause: main :: () -> None ---
def main():
    a, b, queries = read_input()
    out = []
    for l, t, m in queries:
        out.append(str(solve_query(a, b, l, t, m)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
