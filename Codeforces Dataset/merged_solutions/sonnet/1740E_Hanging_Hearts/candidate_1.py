import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: longest_run :: (n: int, parents: list[int]) -> int ---
def longest_run(n, parents):
    children = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        children[parents[v - 2]].append(v)
    height = [1] * (n + 1)
    best = [1] * (n + 1)
    for v in range(n, 0, -1):
        tallest = 0
        total = 0
        for c in children[v]:
            if height[c] > tallest:
                tallest = height[c]
            total += best[c]
        height[v] = tallest + 1
        best[v] = height[v] if height[v] > total else total
    return best[1]


# --- clause: main :: () -> None ---
def main():
    n, parents = read_input()
    sys.stdout.write(str(longest_run(n, parents)) + "\n")


if __name__ == "__main__":
    main()
