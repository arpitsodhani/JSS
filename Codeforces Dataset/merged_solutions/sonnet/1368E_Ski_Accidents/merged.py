import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        tracks = []
        for _ in range(m):
            tracks.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((n, tracks))
    return cases

# Clause pick_closures [Confidence: 1.00]
def pick_closures(n, tracks):
    down = [[] for _ in range(n + 1)]
    for x, y in tracks:
        down[x].append(y)
    level = [0] * (n + 1)
    closed = []
    for v in range(1, n + 1):
        if level[v] == 2:
            closed.append(v)
            continue
        for u in down[v]:
            if level[v] + 1 > level[u]:
                level[u] = level[v] + 1
    return closed

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, tracks in read_input():
        closed = pick_closures(n, tracks)
        lines.append(str(len(closed)))
        lines.append(" ".join(map(str, closed)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

