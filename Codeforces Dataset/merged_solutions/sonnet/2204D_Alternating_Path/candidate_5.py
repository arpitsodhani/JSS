import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        m = raw[reader + 1]
        reader += 2
        edges = []
        for _ in range(m):
            edges.append((raw[reader], raw[reader + 1]))
            reader += 2
        cases.append((n, edges))
    return cases


# --- clause: beautiful_count :: (n: int, edges: list[tuple[int, int]]) -> int ---
def beautiful_count(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    side = [-1] * (n + 1)
    amount = 0
    for start in range(1, n + 1):
        if side[start] >= 0:
            continue
        side[start] = 0
        stack = [start]
        counts = [1, 0]
        fine = True
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if side[u] < 0:
                    side[u] = 1 - side[v]
                    counts[side[u]] += 1
                    stack.append(u)
                elif side[u] == side[v]:
                    fine = False
        if fine:
            amount += counts[0] if counts[0] > counts[1] else counts[1]
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, edges in read_input():
        out.append(beautiful_count(n, edges))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
