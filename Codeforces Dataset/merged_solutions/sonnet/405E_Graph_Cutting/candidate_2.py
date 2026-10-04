import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    return n, m, data[2:2 + 2 * m]


# --- clause: build_adjacency :: (n: int, m: int, flat: list[int]) -> tuple[list[int], list[int], list[int]] ---
def build_adjacency(n, m, flat):
    head = [-1] * (n + 1)
    nxt = [-1] * (2 * m)
    to = [0] * (2 * m)
    arc = 0
    index = 0
    while index < 2 * m:
        a = flat[index]
        b = flat[index + 1]
        index += 2
        to[arc] = b
        nxt[arc] = head[a]
        head[a] = arc
        arc += 1
        to[arc] = a
        nxt[arc] = head[b]
        head[b] = arc
        arc += 1
    return head, nxt, to


# --- clause: cut_paths :: (n: int, m: int, head: list[int], nxt: list[int], to: list[int]) -> list[tuple[int, int, int]] | None ---
def cut_paths(n, m, head, nxt, to):
    if m % 2:
        return None
    used = [False] * m
    visited = [False] * (n + 1)
    cursor = head[:]
    paths = []
    for root in range(1, n + 1):
        if visited[root]:
            continue
        visited[root] = True
        stack = [(root, 0, [])]
        while stack:
            node, parent, pending = stack[-1]
            arc = cursor[node]
            while arc != -1 and used[arc >> 1]:
                arc = nxt[arc]
            cursor[node] = arc
            if arc != -1:
                used[arc >> 1] = True
                cursor[node] = nxt[arc]
                other = to[arc]
                if visited[other]:
                    pending.append(other)
                    while len(pending) >= 2:
                        first = pending.pop()
                        second = pending.pop()
                        paths.append((first, node, second))
                else:
                    visited[other] = True
                    stack.append((other, node, []))
                continue
            stack.pop()
            while len(pending) >= 2:
                first = pending.pop()
                second = pending.pop()
                paths.append((first, node, second))
            if pending:
                paths.append((pending.pop(), node, parent))
            elif parent:
                stack[-1][2].append(node)
                while len(stack[-1][2]) >= 2:
                    first = stack[-1][2].pop()
                    second = stack[-1][2].pop()
                    paths.append((first, parent, second))
    return paths


# --- clause: main :: () -> None ---
def main():
    n, m, flat = read_input()
    head, nxt, to = build_adjacency(n, m, flat)
    paths = cut_paths(n, m, head, nxt, to)
    if paths is None:
        sys.stdout.write("No solution\n")
    else:
        sys.stdout.write("\n".join("%d %d %d" % p for p in paths) + "\n")


if __name__ == "__main__":
    main()
