import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int, int]]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        claims = []
        for _ in range(m):
            i = int(data[pos])
            j = int(data[pos + 1])
            same = 1 if data[pos + 2] == b"crewmate" else 0
            pos += 3
            claims.append((i, j, same))
        cases.append((n, claims))
    return cases


# --- clause: most_imposters :: (n: int, claims: list[tuple[int, int, int]]) -> int ---
def most_imposters(n, claims):
    adj = [[] for _ in range(n + 1)]
    for i, j, same in claims:
        adj[i].append((j, same))
        adj[j].append((i, same))
    side = [-1] * (n + 1)
    total = 0
    for start in range(1, n + 1):
        if side[start] >= 0:
            continue
        side[start] = 0
        stack = [start]
        seen = [start]
        while stack:
            v = stack.pop()
            for u, same in adj[v]:
                want = side[v] if same else 1 - side[v]
                if side[u] < 0:
                    side[u] = want
                    seen.append(u)
                    stack.append(u)
                elif side[u] != want:
                    return -1
        liars = 0
        for v in seen:
            liars += side[v]
        total += liars if liars > len(seen) - liars else len(seen) - liars
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, claims in read_input():
        out.append(most_imposters(n, claims))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
