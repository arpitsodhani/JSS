import sys
from math import gcd


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: build_edges :: (n: int, m: int) -> list[tuple[int, int]] | None ---
def build_edges(n, m):
    if m < n - 1:
        return None
    edges = [(1, v) for v in range(2, n + 1)]
    if len(edges) > m:
        return None
    need = m - len(edges)
    u = 2
    while need and u <= n:
        v = u + 1
        while need and v <= n:
            if gcd(u, v) == 1:
                edges.append((u, v))
                need -= 1
            v += 1
        u += 1
    if need:
        return None
    return edges


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    edges = build_edges(n, m)
    if edges is None:
        sys.stdout.write("Impossible\n")
        return
    out = ["Possible"]
    for u, v in edges:
        out.append(str(u) + " " + str(v))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
