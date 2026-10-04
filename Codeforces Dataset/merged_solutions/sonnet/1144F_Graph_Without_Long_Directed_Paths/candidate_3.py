import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    edges = []
    pos = 2
    for _ in range(m):
        edges.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, edges


# --- clause: two_colour :: (n: int, edges: list[tuple[int, int]]) -> list[int] | None ---
def two_colour(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    colour = [-1] * (n + 1)
    for start in range(1, n + 1):
        if colour[start] >= 0:
            continue
        colour[start] = 0
        queue = [start]
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            shade = colour[node] ^ 1
            for nxt in adj[node]:
                if colour[nxt] < 0:
                    colour[nxt] = shade
                    queue.append(nxt)
                elif colour[nxt] == colour[node]:
                    return None
    return colour


# --- clause: main :: () -> None ---
def main():
    n, m, edges = read_input()
    colour = two_colour(n, edges)
    if colour is None:
        sys.stdout.write("NO\n")
        return
    letters = ["0" if colour[u] == 0 else "1" for u, v in edges]
    sys.stdout.write("YES\n" + "".join(letters) + "\n")


if __name__ == "__main__":
    main()
