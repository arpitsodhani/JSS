# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    count = [0] * (n + 1)
    pos = 1
    for _ in range(n - 1):
        a = data[pos]
        b = data[pos + 1]
        pos += 2
        if a != n and b != n:
            sys.stdout.write("NO\n")
            return
        x = a + b - n
        if x == n:
            sys.stdout.write("NO\n")
            return
        count[x] += 1

    taken = [False] * (n + 1)
    for value in range(1, n):
        if count[value]:
            taken[value] = True

    free = []
    for value in range(1, n):
        if not taken[value]:
            heapq.heappush(free, value)

    edges = []
    roots = []
    for value in range(1, n):
        need = count[value]
        if need == 0:
            continue
        chain = []
        for _ in range(need - 1):
            if not free or free[0] > value:
                sys.stdout.write("NO\n")
                return
            chain.append(heapq.heappop(free))
        chain.append(value)
        roots.append(chain[0])
        for left, right in zip(chain, chain[1:]):
            edges.append((left, right))

    for root in roots:
        edges.append((n, root))

    if len(edges) != n - 1:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    out.extend(f"{a} {b}" for a, b in edges)
    sys.stdout.write("\n".join(out) + "\n")


# Clause finish_program [Confidence: 0.40]
main()


