import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: longest_run :: (n: int, parents: list[int]) -> int ---
def longest_run(n, parents):
    height = [1] * (n + 2)
    total = [0] * (n + 2)
    best = [1] * (n + 2)
    for v in range(n, 1, -1):
        parent = parents[v - 2]
        best[v] = height[v] if height[v] > total[v] else total[v]
        total[parent] += best[v]
        if height[v] + 1 > height[parent]:
            height[parent] = height[v] + 1
    best[1] = height[1] if height[1] > total[1] else total[1]
    return best[1]


# --- clause: main :: () -> None ---
def main():
    n, parents = read_input()
    sys.stdout.write(str(longest_run(n, parents)) + "\n")


if __name__ == "__main__":
    main()
