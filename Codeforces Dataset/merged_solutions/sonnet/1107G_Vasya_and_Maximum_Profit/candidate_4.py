import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
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


# --- clause: best_profit :: (n: int, reward: int, difficulty: list[int], price: list[int]) -> int ---
def best_profit(n, reward, difficulty, price):
    prefix = [0] * (n + 1)
    for i, cost in enumerate(price):
        prefix[i + 1] = prefix[i] + reward - cost
    best = 0
    for i in range(n):
        if reward - price[i] > best:
            best = reward - price[i]
    parent = list(range(n))
    low = [prefix[i] for i in range(n)]
    high = [prefix[i + 1] for i in range(n)]
    gaps = []
    for i in range(n - 1):
        gaps.append((difficulty[i + 1] - difficulty[i], i))
    gaps.sort()

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            nxt = parent[x]
            parent[x] = root
            x = nxt
        return root

    for gap, i in gaps:
        left = find(i)
        right = find(i + 1)
        total = high[right] - low[left] - gap * gap
        if total > best:
            best = total
        parent[left] = right
        if low[left] < low[right]:
            low[right] = low[left]
        if high[left] > high[right]:
            high[right] = high[left]
    return best


# --- clause: main :: () -> None ---
def main():
    n, reward, difficulty, price = read_input()
    sys.stdout.write(str(best_profit(n, reward, difficulty, price)) + "\n")


if __name__ == "__main__":
    main()
