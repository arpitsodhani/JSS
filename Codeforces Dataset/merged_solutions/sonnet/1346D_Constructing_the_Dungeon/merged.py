import sys

# Clause read_input [Confidence: 0.80]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        edges = [int(token) for token in data[pos:pos + 3 * m]]
        pos += 3 * m
        cases.append((n, m, edges))
    return cases

# Clause assign_monsters [Confidence: 1.00]
def assign_monsters(n, m, edges):
    values = [0] * (n + 1)
    for i in range(m):
        u = edges[3 * i]
        v = edges[3 * i + 1]
        w = edges[3 * i + 2]
        if w > values[u]:
            values[u] = w
        if w > values[v]:
            values[v] = w
    for i in range(m):
        u = edges[3 * i]
        v = edges[3 * i + 1]
        w = edges[3 * i + 2]
        low = values[u] if values[u] < values[v] else values[v]
        if low != w:
            return None
    return values[1:]

# Clause main [Confidence: 0.60]
def main():
    out = []
    for n, m, edges in read_input():
        values = assign_monsters(n, m, edges)
        if values is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(" ".join(map(str, values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

