# CLAUSE: setup_environment
import sys
from itertools import permutations

# CLAUSE: solve_logic
def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    price = [[next(it) for _ in range(n)] for _ in range(3)]

    neighbours = [set() for _ in range(n)]
    for _ in range(n - 1):
        u = next(it) - 1
        v = next(it) - 1
        neighbours[u].add(v)
        neighbours[v].add(u)

    if n == 1:
        best = min(range(3), key=lambda c: price[c][0])
        print(price[best][0])
        print(best + 1)
        return

    if n == 2:
        colors = [min(range(3), key=lambda c: price[c][i]) for i in range(2)]
        print(price[colors[0]][0] + price[colors[1]][1])
        print(colors[0] + 1, colors[1] + 1)
        return

    bad = False
    first = -1
    for i, links in enumerate(neighbours):
        if len(links) > 2:
            bad = True
            break
        if len(links) == 1 and first == -1:
            first = i

    if bad:
        print(-1)
        return

    line = [first]
    previous = -1
    while len(line) < n:
        current = line[-1]
        candidates = neighbours[current]
        chosen = -1
        for x in candidates:
            if x != previous:
                chosen = x
                break
        previous = current
        line.append(chosen)

    best_sum = 10 ** 35
    best_assignment = None
    for a, b, c in permutations(range(3)):
        cycle = (a, b, c)
        cur_sum = 0
        assignment = [0] * n
        for index, vertex in enumerate(line):
            color = cycle[index % 3]
            cur_sum += price[color][vertex]
            assignment[vertex] = color + 1
        if cur_sum < best_sum:
            best_sum = cur_sum
            best_assignment = assignment

    print(best_sum)
    print(" ".join(map(str, best_assignment)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
