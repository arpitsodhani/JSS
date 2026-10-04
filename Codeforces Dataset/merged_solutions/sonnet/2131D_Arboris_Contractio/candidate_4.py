import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        edges = []
        for _ in range(n - 1):
            edges.append((numbers[cursor], numbers[cursor + 1]))
            cursor += 2
        cases.append((n, edges))
    return cases


# --- clause: fewest_moves :: (n: int, edges: list[tuple[int, int]]) -> int ---
def fewest_moves(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    tips = []
    for v in range(1, n + 1):
        if len(adj[v]) == 1:
            tips.append(v)
    best = len(tips)
    reach = [0] * (n + 1)
    for tip in tips:
        reach[adj[tip][0]] += 1
        reach[tip] += 1
    for v in range(1, n + 1):
        here = len(tips) - reach[v]
        if here < best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, edges in read_input():
        out.append(fewest_moves(n, edges))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
