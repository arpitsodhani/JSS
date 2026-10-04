import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    a = numbers[2:2 + n]
    offset = 2 + n
    queries = [(numbers[offset + 2 * i], numbers[offset + 2 * i + 1]) for i in range(m)]
    return a, queries


# --- clause: closest_equals :: (a: list[int], queries: list[tuple[int, int]]) -> list[int] ---
def closest_equals(a, queries):
    n = len(a)
    big = n + 1
    tree = [big] * (n + 2)
    seen = {}
    pairs = [0] * (n + 1)
    for i in range(n):
        value = a[i]
        pairs[i + 1] = seen.get(value, 0)
        seen[value] = i + 1
    buckets = [[] for _ in range(n + 1)]
    for q in range(len(queries)):
        buckets[queries[q][1]].append(q)
    answers = [-1] * len(queries)
    for right in range(1, n + 1):
        spot = pairs[right]
        if spot:
            gap = right - spot
            i = n + 1 - spot
            while i <= n:
                if gap < tree[i]:
                    tree[i] = gap
                i += i & (-i)
        for q in buckets[right]:
            best = big
            i = n + 1 - queries[q][0]
            while i > 0:
                if tree[i] < best:
                    best = tree[i]
                i -= i & (-i)
            if best < big:
                answers[q] = best
    return answers


# --- clause: main :: () -> None ---
def main():
    a, queries = read_input()
    sys.stdout.write("\n".join(map(str, closest_equals(a, queries))) + "\n")


if __name__ == "__main__":
    main()
