import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    pos = 2
    known = []
    for _ in range(n):
        count = data[pos]
        pos += 1
        known.append(data[pos:pos + count])
        pos += count
    return m, known

# Clause find_root [Confidence: 1.00]
def find_root(parent, node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node

# Clause least_cost [Confidence: 1.00]
def least_cost(m, known):
    n = len(known)
    parent = [i for i in range(n + m + 1)]
    speaks = False
    for i in range(n):
        for language in known[i]:
            speaks = True
            a = find_root(parent, i)
            b = find_root(parent, n + language)
            if a != b:
                parent[a] = b
    groups = set()
    for i in range(n):
        groups.add(find_root(parent, i))
    if not speaks:
        return n
    return len(groups) - 1

# Clause main [Confidence: 1.00]
def main():
    m, known = read_input()
    sys.stdout.write("%d\n" % least_cost(m, known))


if __name__ == "__main__":
    main()

