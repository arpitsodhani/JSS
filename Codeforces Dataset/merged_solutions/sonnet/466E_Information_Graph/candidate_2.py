import sys


# --- clause: read_input :: () -> tuple[int, int, list[list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    events = []
    pos = 2
    for _ in range(m):
        kind = int(data[pos])
        pos += 1
        if kind != 2:
            events.append([kind, int(data[pos]), int(data[pos + 1])])
            pos += 2
        else:
            events.append([kind, int(data[pos])])
            pos += 1
    return n, m, events


# --- clause: replay :: (n: int, events: list[list[int]]) -> tuple[list[int], list, list] ---
def replay(n, events):
    parent = [0] * (n + 1)
    link = list(range(n + 1))

    packets = []
    queries = []
    for event in events:
        if event[0] == 1:
            x = event[1]
            y = event[2]
            parent[x] = y
            root = x
            while link[root] != root:
                link[root] = link[link[root]]
                root = link[root]
            link[root] = y
        elif event[0] == 2:
            x = event[1]
            root = x
            while link[root] != root:
                link[root] = link[link[root]]
                root = link[root]
            packets.append((x, root))
        else:
            queries.append((event[1], event[2]))
    return parent, packets, queries


# --- clause: answer_queries :: (n: int, parent: list[int], packets: list, queries: list) -> list[str] ---
def answer_queries(n, parent, packets, queries):
    children = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        if parent[v]:
            children[parent[v]].append(v)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    timer = 0
    for start in range(1, n + 1):
        if parent[start]:
            continue
        stack = [(start, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                timer += 1
                tin[node] = timer
                stack.append((node, 1))
                for kid in children[node]:
                    stack.append((kid, 0))
            else:
                tout[node] = timer
    out = []
    for x, idx in queries:
        start, top = packets[idx - 1]
        if tin[x] <= tin[start] <= tout[x] and tin[top] <= tin[x]:
            out.append("YES")
        else:
            out.append("NO")
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, events = read_input()
    parent, packets, queries = replay(n, events)
    sys.stdout.write("%s\n" % "\n".join(answer_queries(n, parent, packets, queries)))


if __name__ == "__main__":
    main()
