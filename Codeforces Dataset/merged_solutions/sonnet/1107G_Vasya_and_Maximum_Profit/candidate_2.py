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
    running = 0
    for i in range(n):
        running += reward - price[i]
        prefix[i + 1] = running
    best = 0
    for value in price:
        if reward - value > best:
            best = reward - value
    parent = list(range(n))
    smallest = prefix[:n]
    largest = prefix[1:]
    edges = sorted((difficulty[i + 1] - difficulty[i], i) for i in range(n - 1))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    for gap, i in edges:
        left = find(i)
        right = find(i + 1)
        here = largest[right] - smallest[left] - gap * gap
        if here > best:
            best = here
        parent[left] = right
        if smallest[left] < smallest[right]:
            smallest[right] = smallest[left]
        if largest[left] > largest[right]:
            largest[right] = largest[left]
    return best


# --- clause: main :: () -> None ---
def main():
    n, reward, difficulty, price = read_input()
    sys.stdout.write(str(best_profit(n, reward, difficulty, price)) + "\n")


if __name__ == "__main__":
    main()
