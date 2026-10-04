import sys

# Clause read_input [Confidence: 1.00]
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

# Clause route_profit [Confidence: 0.80]
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

# Clause best_profit [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    n, m, k, planets = read_input()
    sys.stdout.write(str(best_profit(n, m, k, planets)) + "\n")


if __name__ == "__main__":
    main()

