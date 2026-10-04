import sys


# --- clause: read_input :: () -> tuple[list[int], list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    top = numbers[1:n]
    low = numbers[n:2 * n - 1]
    across = numbers[2 * n - 1:3 * n - 1]
    return top, low, across


# --- clause: route_costs :: (top: list[int], low: list[int], across: list[int]) -> list[int] ---
def route_costs(top, low, across):
    n = len(across)
    ahead = [0] * (n + 1)
    for i in range(n - 1):
        ahead[i + 1] = ahead[i] + top[i]
    behind = [0] * (n + 1)
    for i in range(n - 2, -1, -1):
        behind[i] = behind[i + 1] + low[i]
    costs = []
    for j in range(n):
        costs.append(ahead[j] + across[j] + behind[j])
    return costs


# --- clause: main :: () -> None ---
def main():
    top, low, across = read_input()
    costs = sorted(route_costs(top, low, across))
    sys.stdout.write("%d\n" % (costs[0] + costs[1]))


if __name__ == "__main__":
    main()
