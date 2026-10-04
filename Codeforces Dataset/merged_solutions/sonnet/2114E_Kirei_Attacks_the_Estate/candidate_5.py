import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[list[int]]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        danger = raw[offset:offset + n]
        offset += n
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = raw[offset]
            v = raw[offset + 1]
            offset += 2
            adj[u].append(v)
            adj[v].append(u)
        cases.append((danger, adj))
    return cases


# --- clause: threat_values :: (danger: list[int], adj: list[list[int]]) -> list[int] ---
def threat_values(danger, adj):
    n = len(danger)
    ceiling_value = [0] * (n + 1)
    low = [0] * (n + 1)
    parent = [0] * (n + 1)
    parent[1] = 1
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    ceiling_value[1] = danger[0]
    low[1] = danger[0]
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if seen[u]:
                continue
            seen[u] = True
            parent[u] = v
            here = danger[u - 1]
            ceiling_value[u] = here if here > here - low[v] else here - low[v]
            low[u] = here if here < here - ceiling_value[v] else here - ceiling_value[v]
            order.append(u)
    return ceiling_value[1:]


# --- clause: main :: () -> None ---
def main():
    out = []
    for danger, adj in read_input():
        out.append(" ".join(map(str, threat_values(danger, adj))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
