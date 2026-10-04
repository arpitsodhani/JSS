# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def edge_id(u, v, n):
    if u > v:
        u, v = v, u
    return u * (n + 1) + v

def decode_edge(key, n):
    return divmod(key, n + 1)

def restore(n, triples):
    if n == 3:
        return list(triples[0])

    seen = {}
    for a, b, c in triples:
        for u, v in ((a, b), (b, c), (a, c)):
            key = edge_id(u, v, n)
            seen[key] = seen.get(key, 0) + 1

    neighbors = [[] for _ in range(n + 1)]
    for key, value in seen.items():
        if value == 1:
            u, v = decode_edge(key, n)
            neighbors[u].append(v)
            neighbors[v].append(u)

    start = 0
    for i in range(1, n + 1):
        if neighbors[i]:
            start = i
            break

    answer = [start]
    previous = -1
    current = start

    while True:
        pair = neighbors[current]
        if len(pair) == 1:
            nxt = pair[0]
        elif pair[0] == previous:
            nxt = pair[1]
        else:
            nxt = pair[0]
        previous, current = current, nxt
        if current == start:
            return answer
        answer.append(current)

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    tests = data[p]
    p += 1
    lines = []

    for _ in range(tests):
        n = data[p]
        p += 1
        triples = []
        for _ in range(n - 2):
            triples.append(data[p:p + 3])
            p += 3
        lines.append(" ".join(map(str, restore(n, triples))))

    sys.stdout.write("\n".join(lines))

main()
