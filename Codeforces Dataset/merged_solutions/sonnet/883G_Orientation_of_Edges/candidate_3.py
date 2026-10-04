import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    s = fields[2]
    edges = []
    for i in range(m):
        edges.append((fields[3 + 3 * i], fields[4 + 3 * i], fields[5 + 3 * i]))
    return n, s, edges


# --- clause: reach_from :: (n: int, s: int, edges: list[tuple[int, int, int]], loose: bool) -> list[int] ---
def reach_from(n, s, edges, loose):
    adj = [[] for _ in range(n + 1)]
    for kind, u, v in edges:
        if kind == 1 or loose:
            adj[u].append(v)
        if kind == 2 and loose:
            adj[v].append(u)
    when = [-1] * (n + 1)
    when[s] = 0
    arranged = [s]
    front = 0
    while front < len(arranged):
        v = arranged[front]
        front += 1
        for u in adj[v]:
            if when[u] < 0:
                when[u] = len(arranged)
                arranged.append(u)
    return when


# --- clause: orient_edges :: (edges: list[tuple[int, int, int]], when: list[int], grow: bool) -> str ---
def orient_edges(edges, when, grow):
    marks = []
    for kind, u, v in edges:
        if kind == 1:
            continue
        if not grow:
            marks.append("-" if when[u] >= 0 and when[v] < 0 else "+")
        elif when[u] < 0:
            marks.append("+" if when[v] < 0 else "-")
        elif when[v] < 0 or when[u] <= when[v]:
            marks.append("+")
        else:
            marks.append("-")
    return "".join(marks)


# --- clause: main :: () -> None ---
def main():
    n, s, edges = read_input()
    wide = reach_from(n, s, edges, True)
    tight = reach_from(n, s, edges, False)
    out = [str(sum(1 for x in wide[1:] if x >= 0)), orient_edges(edges, wide, True),
           str(sum(1 for x in tight[1:] if x >= 0)), orient_edges(edges, tight, False)]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
