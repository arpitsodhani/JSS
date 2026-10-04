import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: longest_run :: (n: int, parents: list[int]) -> int ---
def longest_run(n, parents):
    kids = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        kids[parents[v - 2]].append(v)
    depth = [1] * (n + 1)
    answer = [1] * (n + 1)
    order = list(range(1, n + 1))
    for v in reversed(order):
        pile = 0
        deepest = 0
        for child in kids[v]:
            pile += answer[child]
            if depth[child] > deepest:
                deepest = depth[child]
        depth[v] = deepest + 1
        answer[v] = max(depth[v], pile)
    return answer[1]


# --- clause: main :: () -> None ---
def main():
    n, parents = read_input()
    sys.stdout.write(str(longest_run(n, parents)) + "\n")


if __name__ == "__main__":
    main()
