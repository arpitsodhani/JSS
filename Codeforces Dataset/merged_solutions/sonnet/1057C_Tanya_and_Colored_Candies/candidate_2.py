# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    s = int(tokens[1]) - 1
    k = int(tokens[2])
    sweets = [int(x) for x in tokens[3:3 + n]]
    shades = tokens[3 + n]
    limit = 10 ** 18

# CLAUSE: solve_logic
    best = [[limit for _ in range(k + 1)] for _ in range(n)]
    for pos, amount in enumerate(sweets):
        best[pos][min(k, amount)] = abs(pos - s)

    positions = list(range(n))
    positions.sort(key=lambda pos: sweets[pos])

    for pos in positions:
        amount = sweets[pos]
        row = best[pos]
        for prev in positions:
            if sweets[prev] >= amount:
                break
            if shades[prev] == shades[pos]:
                continue
            step = abs(pos - prev)
            prev_row = best[prev]
            for eaten, old_cost in enumerate(prev_row):
                if old_cost == limit:
                    continue
                total = eaten + amount
                if total > k:
                    total = k
                new_cost = old_cost + step
                if new_cost < row[total]:
                    row[total] = new_cost

    ans = min(best[pos][k] for pos in range(n))

# CLAUSE: finish_program
    sys.stdout.write(str(-1 if ans == limit else ans))

if __name__ == "__main__":
    main()
