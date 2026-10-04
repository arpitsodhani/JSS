import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m = data[0]
    pos = 1
    arrays = []
    for _ in range(m):
        n = data[pos]
        pos += 1
        arrays.append(data[pos:pos + n])
        pos += n
    return arrays


# --- clause: build_graph :: (arrays: list[list[int]]) -> tuple[int, list[int], list[int], list[int]] | None ---
def build_graph(arrays):
    m = len(arrays)
    labels = {}
    counts = []
    for row in arrays:
        for value in row:
            slot = labels.get(value, -1)
            if slot < 0:
                slot = len(counts)
                labels[value] = slot
                counts.append(0)
            counts[slot] += 1
    for total in counts:
        if total & 1:
            return None
    nodes = m + len(counts)
    head = [-1] * nodes
    nxt = []
    to = []
    for index in range(m):
        for value in arrays[index]:
            other = m + labels[value]
            edge = len(to)
            to.append(other)
            nxt.append(head[index])
            head[index] = edge
            to.append(index)
            nxt.append(head[other])
            head[other] = edge + 1
    return nodes, head, nxt, to


# --- clause: orient_edges :: (nodes: int, head: list[int], nxt: list[int], to: list[int]) -> list[int] ---
def orient_edges(nodes, head, nxt, to):
    total = len(to) // 2
    used = [False] * total
    side = [0] * total
    cursor = head[:]
    for start in range(nodes):
        if cursor[start] == -1:
            continue
        stack = [start]
        while stack:
            node = stack[-1]
            arc = cursor[node]
            while arc != -1 and used[arc >> 1]:
                arc = nxt[arc]
            cursor[node] = arc
            if arc == -1:
                stack.pop()
                continue
            used[arc >> 1] = True
            side[arc >> 1] = arc & 1
            cursor[node] = nxt[arc]
            stack.append(to[arc])
    return side


# --- clause: main :: () -> None ---
def main():
    arrays = read_input()
    graph = build_graph(arrays)
    if graph is None:
        sys.stdout.write("NO\n")
        return
    nodes, head, nxt, to = graph
    side = orient_edges(nodes, head, nxt, to)
    out = ["YES"]
    index = 0
    for row in arrays:
        letters = []
        for _ in row:
            letters.append("L" if side[index] == 0 else "R")
            index += 1
        out.append("".join(letters))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
