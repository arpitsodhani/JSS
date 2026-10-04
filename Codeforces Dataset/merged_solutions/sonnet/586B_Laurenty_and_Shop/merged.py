import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    top = data[1:n]
    low = data[n:2 * n - 1]
    across = data[2 * n - 1:3 * n - 1]
    return top, low, across

# Clause route_costs [Confidence: 0.80]
def route_costs(top, low, across):
    n = len(across)
    costs = []
    for j in range(n):
        amount = across[j]
        for i in range(j):
            amount += top[i]
        for i in range(j, n - 1):
            amount += low[i]
        costs.append(amount)
    return costs

# Clause main [Confidence: 1.00]
def main():
    top, low, across = read_input()
    costs = sorted(route_costs(top, low, across))
    sys.stdout.write("%d\n" % (costs[0] + costs[1]))


if __name__ == "__main__":
    main()

