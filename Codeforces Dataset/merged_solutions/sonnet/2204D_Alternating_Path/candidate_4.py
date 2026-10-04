import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        m = numbers[cursor + 1]
        cursor += 2
        edges = []
        for _ in range(m):
            edges.append((numbers[cursor], numbers[cursor + 1]))
            cursor += 2
        cases.append((n, edges))
    return cases


# --- clause: beautiful_count :: (n: int, edges: list[tuple[int, int]]) -> int ---
def beautiful_count(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    side = [-1] * (n + 1)
    total = 0
    for start in range(1, n + 1):
        if side[start] >= 0:
            continue
        side[start] = 0
        queue = [start]
        head = 0
        members = [start]
        while head < len(queue):
            v = queue[head]
            head += 1
            for u in adj[v]:
                if side[u] < 0:
                    side[u] = 1 - side[v]
                    queue.append(u)
                    members.append(u)
        broken = False
        for v in members:
            for u in adj[v]:
                if side[u] == side[v]:
                    broken = True
        if broken:
            continue
        ones = 0
        for v in members:
            ones += side[v]
        zeros = len(members) - ones
        total += ones if ones > zeros else zeros
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, edges in read_input():
        out.append(beautiful_count(n, edges))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
