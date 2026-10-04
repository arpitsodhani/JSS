# CLAUSE: setup_environment
import sys
from itertools import permutations

# CLAUSE: solve_logic
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    p = 1
    costs = [tokens[p:p + n], tokens[p + n:p + 2 * n], tokens[p + 2 * n:p + 3 * n]]
    p += 3 * n

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a = tokens[p] - 1
        b = tokens[p + 1] - 1
        p += 2
        graph[a].append(b)
        graph[b].append(a)

    if n == 1:
        c = min(range(3), key=lambda x: costs[x][0])
        sys.stdout.write(str(costs[c][0]) + "\n" + str(c + 1) + "\n")
        return

    if n == 2:
        ans = []
        total = 0
        for i in range(2):
            c = min(range(3), key=lambda x: costs[x][i])
            ans.append(c + 1)
            total += costs[c][i]
        sys.stdout.write(str(total) + "\n" + " ".join(map(str, ans)) + "\n")
        return

    if any(len(x) > 2 for x in graph):
        sys.stdout.write("-1\n")
        return

    start = next(i for i, adj in enumerate(graph) if len(adj) == 1)
    order = []
    prev = -1
    node = start
    while node != -1:
        order.append(node)
        nxt = -1
        for v in graph[node]:
            if v != prev:
                nxt = v
                break
        prev, node = node, nxt

    best = None
    best_answer = None
    for pattern in permutations((0, 1, 2)):
        total = 0
        answer = [0] * n
        for i, node in enumerate(order):
            c = pattern[i % 3]
            total += costs[c][node]
            answer[node] = c + 1
        if best is None or total < best:
            best = total
            best_answer = answer

    sys.stdout.write(str(best) + "\n" + " ".join(map(str, best_answer)) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
