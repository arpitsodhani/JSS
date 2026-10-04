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
    supply = [0] * 1001
    for j, (buy, _sell, stock) in enumerate(source):
        gain = target[j][1] - buy
        if gain > 0:
            supply[gain] += stock
    profit = 0
    room = k
    gain = 1000
    while gain > 0 and room > 0:
        stock = supply[gain]
        if stock:
            take = stock if stock < room else room
            profit += gain * take
            room -= take
        gain -= 1
    return profit

# --- clause: best_profit :: (n: int, m: int, k: int, planets: list) -> int ---
def best_profit(n, m, k, planets):
    answer = 0
    for i in range(n):
        for j in range(n):
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
