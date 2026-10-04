import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: longest_run :: (n: int, parents: list[int]) -> int ---
def longest_run(n, parents):
    children = [[] for _ in range(n + 1)]
    for index, parent in enumerate(parents, start=2):
        children[parent].append(index)
    height = [1] * (n + 1)
    best = [1] * (n + 1)
    v = n
    while v >= 1:
        tall = 0
        summed = 0
        for child in children[v]:
            summed += best[child]
            if height[child] > tall:
                tall = height[child]
        height[v] = tall + 1
        best[v] = summed if summed > height[v] else height[v]
        v -= 1
    return best[1]


# --- clause: main :: () -> None ---
def main():
    n, parents = read_input()
    sys.stdout.write(str(longest_run(n, parents)) + "\n")


if __name__ == "__main__":
    main()
