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
    high = (t - a) // b + 1
    low = l
    budget = t * m
    while low < high:
        mid = (low + high + 1) // 2
        first = a + (l - 1) * b
        last = a + (mid - 1) * b
        if (first + last) * (mid - l + 1) // 2 <= budget:
            low = mid
        else:
            high = mid - 1
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
