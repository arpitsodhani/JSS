import sys


# --- clause: read_input :: () -> tuple[list[int], list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    top = data[1:n]
    low = data[n:2 * n - 1]
    across = data[2 * n - 1:3 * n - 1]
    return top, low, across


# --- clause: route_costs :: (top: list[int], low: list[int], across: list[int]) -> list[int] ---
def route_costs(top, low, across):
    n = len(across)
    costs = []
    for j in range(n):
        total = across[j]
        for i in range(j):
            total += top[i]
        for i in range(j, n - 1):
            total += low[i]
        costs.append(total)
    return costs


# --- clause: main :: () -> None ---
def main():
    top, low, across = read_input()
    costs = sorted(route_costs(top, low, across))
    sys.stdout.write("%d\n" % (costs[0] + costs[1]))


if __name__ == "__main__":
    main()
