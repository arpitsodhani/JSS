# CLAUSE: setup_environment
import sys

def relax(target, source, distance, amount, need, inf):
    for eaten in range(need + 1):
        cost = source[eaten]
        if cost == inf:
            continue
        nxt = eaten + amount
        if nxt > need:
            nxt = need
        candidate = cost + distance
        if candidate < target[nxt]:
            target[nxt] = candidate

def main():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    s = int(raw[1]) - 1
    k = int(raw[2])
    candies = list(map(int, raw[3:3 + n]))
    colors = raw[3 + n]
    inf = 10 ** 18

# CLAUSE: solve_logic
    states = []
    for i in range(n):
        row = [inf] * (k + 1)
        row[min(k, candies[i])] = abs(i - s)
        states.append(row)

    order = sorted(range(n), key=candies.__getitem__)

    for right_index in range(n):
        box = order[right_index]
        for left_index in range(right_index):
            before = order[left_index]
            if candies[before] == candies[box]:
                continue
            if colors[before] == colors[box]:
                continue
            relax(states[box], states[before], abs(box - before), candies[box], k, inf)

    result = inf
    for row in states:
        if row[k] < result:
            result = row[k]

# CLAUSE: finish_program
    print(-1 if result == inf else result)

if __name__ == "__main__":
    main()
