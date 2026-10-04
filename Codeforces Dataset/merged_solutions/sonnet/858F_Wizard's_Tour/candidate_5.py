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
    for i in range(m):
        a = flat[2 * i]
        b = flat[2 * i + 1]
        to[2 * i] = b
        nxt[2 * i] = head[a]
        head[a] = 2 * i
        to[2 * i + 1] = a
        nxt[2 * i + 1] = head[b]
        head[b] = 2 * i + 1
    return head, nxt, to


# --- clause: plan_episodes :: (n: int, m: int, head: list[int], nxt: list[int], to: list[int]) -> list[tuple[int, int, int]] ---
def plan_episodes(n, m, head, nxt, to):
    used = [False] * m
    visited = [False] * (n + 1)
    cursor = head[:]
    shows = []
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
                else:
                    visited[other] = True
                    stack.append((other, node, []))
                continue
            stack.pop()
            while len(pending) >= 2:
                first = pending.pop()
                second = pending.pop()
                shows.append((first, node, second))
            if pending:
                leftover = pending.pop()
                if parent:
                    shows.append((leftover, node, parent))
            elif parent:
                stack[-1][2].append(node)
    return shows


# --- clause: main :: () -> None ---
def main():
    n, m, flat = read_input()
    head, nxt, to = build_adjacency(n, m, flat)
    shows = plan_episodes(n, m, head, nxt, to)
    out = [str(len(shows))]
    for x, y, z in shows:
        out.append("%d %d %d" % (x, y, z))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
