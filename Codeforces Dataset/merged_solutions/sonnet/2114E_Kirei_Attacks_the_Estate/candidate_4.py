import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[list[int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        danger = numbers[reader:reader + n]
        reader += n
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = numbers[reader]
            v = numbers[reader + 1]
            reader += 2
            adj[u].append(v)
            adj[v].append(u)
        cases.append((danger, adj))
    return cases


# --- clause: threat_values :: (danger: list[int], adj: list[list[int]]) -> list[int] ---
def threat_values(danger, adj):
    n = len(danger)
    high = [0] * (n + 1)
    low = [0] * (n + 1)
    high[1] = danger[0]
    low[1] = danger[0]
    seen = [False] * (n + 1)
    seen[1] = True
    stack = [1]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if seen[u]:
                continue
            seen[u] = True
            here = danger[u - 1]
            up = here - low[v]
            down = here - high[v]
            high[u] = up if up > here else here
            low[u] = down if down < here else here
            stack.append(u)
    return high[1:]


# --- clause: main :: () -> None ---
def main():
    out = []
    for danger, adj in read_input():
        out.append(" ".join(map(str, threat_values(danger, adj))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
