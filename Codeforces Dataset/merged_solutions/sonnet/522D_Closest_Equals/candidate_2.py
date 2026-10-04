import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    a = tokens[2:2 + n]
    cursor = 2 + n
    queries = [(tokens[cursor + 2 * i], tokens[cursor + 2 * i + 1]) for i in range(m)]
    return a, queries


# --- clause: closest_equals :: (a: list[int], queries: list[tuple[int, int]]) -> list[int] ---
def closest_equals(a, queries):
    n = len(a)
    big = n + 1
    tree = [big] * (n + 2)
    last = {}
    pairs = [0] * (n + 1)
    for i in range(n):
        value = a[i]
        if value in last:
            pairs[i + 1] = last[value]
        last[value] = i + 1
    order = sorted(range(len(queries)), key=lambda q: queries[q][1])
    answers = [-1] * len(queries)
    at = 0
    right = 0
    for q in order:
        left, bound = queries[q]
        while right < bound:
            right += 1
            spot = pairs[right]
            if spot:
                gap = right - spot
                i = n + 1 - spot
                while i <= n:
                    if tree[i] > gap:
                        tree[i] = gap
                    i += i & (-i)
        best = big
        i = n + 1 - left
        while i > 0:
            if tree[i] < best:
                best = tree[i]
            i -= i & (-i)
        answers[q] = -1 if best == big else best
    return answers


# --- clause: main :: () -> None ---
def main():
    a, queries = read_input()
    sys.stdout.write("\n".join(map(str, closest_equals(a, queries))) + "\n")


if __name__ == "__main__":
    main()
