import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[list[tuple[int, int, int]]]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    n = int(tokens[pos])
    m = int(tokens[pos + 1])
    k = int(tokens[pos + 2])
    pos += 3
    planets = []
    for _ in range(n):
        pos += 1
        rows = []
        for _ in range(m):
            buy = int(tokens[pos])
            sell = int(tokens[pos + 1])
            stock = int(tokens[pos + 2])
            pos += 3
            rows.append((buy, sell, stock))
        planets.append(rows)
    return n, m, k, planets

# --- clause: route_profit :: (source: list[tuple[int, int, int]], target: list[tuple[int, int, int]], k: int) -> int ---
def route_profit(source, target, k):
    deals = []
    for j in range(len(source)):
        buy, _sell, stock = source[j]
        gain = target[j][1] - buy
        if gain > 0 and stock > 0:
            deals.append((gain, stock))
    deals.sort(reverse=True)
    profit = 0
    room = k
    for gain, stock in deals:
        if room <= 0:
            break
        take = stock if stock < room else room
        profit += gain * take
        room -= take
    return profit

# --- clause: best_profit :: (n: int, m: int, k: int, planets: list) -> int ---
def best_profit(n, m, k, planets):
    answer = 0
    for pair in range(n * n):
        i, j = divmod(pair, n)
        if i == j:
            continue
        value = route_profit(planets[i], planets[j], k)
        if value > answer:
            answer = value
    return answer

# --- clause: main :: () -> None ---
def main():
    n, m, k, planets = read_input()
    sys.stdout.write(str(best_profit(n, m, k, planets)) + "\n")


if __name__ == "__main__":
    main()
