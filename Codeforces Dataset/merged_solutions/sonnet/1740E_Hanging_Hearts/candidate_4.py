import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: longest_run :: (n: int, parents: list[int]) -> int ---
def longest_run(n, parents):
    height = [1] * (n + 1)
    stacked = [0] * (n + 1)
    for v in range(n, 1, -1):
        parent = parents[v - 2]
        value = height[v] if height[v] > stacked[v] else stacked[v]
        stacked[parent] += value
        if height[v] >= height[parent]:
            height[parent] = height[v] + 1
    return height[1] if height[1] > stacked[1] else stacked[1]


# --- clause: main :: () -> None ---
def main():
    n, parents = read_input()
    sys.stdout.write(str(longest_run(n, parents)) + "\n")


if __name__ == "__main__":
    main()
