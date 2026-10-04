import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    heroes = list(map(int, data[1:n + 1]))
    m = int(data[n + 1])
    dragons = [int(token) for token in data[n + 2:n + 2 + 2 * m]]
    return n, heroes, m, dragons

# Clause lower_bound [Confidence: 1.00]
def lower_bound(heroes, value):
    low = 0
    high = len(heroes)
    while low < high:
        mid = (low + high) // 2
        if heroes[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low

# Clause dragon_cost [Confidence: 1.00]
def dragon_cost(heroes, total, x, y):
    best = -1
    at = lower_bound(heroes, x)
    if at < len(heroes):
        rest = total - heroes[at]
        cost = y - rest
        if cost < 0:
            cost = 0
        best = cost
    if at > 0:
        picked = heroes[at - 1]
        rest = total - picked
        cost = x - picked
        if y > rest:
            cost += y - rest
        if best < 0 or cost < best:
            best = cost
    return best

# Clause main [Confidence: 1.00]
def main():
    n, heroes, m, dragons = read_input()
    heroes.sort()
    total = sum(heroes)
    out = []
    for i in range(m):
        out.append(str(dragon_cost(heroes, total, dragons[2 * i], dragons[2 * i + 1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

