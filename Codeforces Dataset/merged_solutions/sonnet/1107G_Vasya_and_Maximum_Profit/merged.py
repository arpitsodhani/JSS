import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    reward = data[1]
    difficulty = []
    price = []
    pos = 2
    for _ in range(n):
        difficulty.append(data[pos])
        price.append(data[pos + 1])
        pos += 2
    return n, reward, difficulty, price

# Clause best_profit [Confidence: 1.00]
def best_profit(n, reward, difficulty, price):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + reward - price[i]
    best = 0
    for i in range(n):
        gain = reward - price[i]
        if gain > best:
            best = gain
    parent = list(range(n))
    low = [prefix[i] for i in range(n)]
    high = [prefix[i + 1] for i in range(n)]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    order = sorted(range(n - 1), key=lambda i: difficulty[i + 1] - difficulty[i])
    for i in order:
        gap = difficulty[i + 1] - difficulty[i]
        left = find(i)
        right = find(i + 1)
        candidate = high[right] - low[left] - gap * gap
        if candidate > best:
            best = candidate
        parent[left] = right
        if low[left] < low[right]:
            low[right] = low[left]
        if high[left] > high[right]:
            high[right] = high[left]
    return best

# Clause main [Confidence: 1.00]
def main():
    n, reward, difficulty, price = read_input()
    sys.stdout.write(str(best_profit(n, reward, difficulty, price)) + "\n")


if __name__ == "__main__":
    main()

