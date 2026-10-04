import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pos = 2
    friends = []
    for _ in range(k):
        friends.append((data[pos], data[pos + 1]))
        pos += 2
    m = data[pos]
    pos += 1
    foes = []
    for _ in range(m):
        foes.append((data[pos], data[pos + 1]))
        pos += 2
    return n, friends, foes

# Clause largest_party [Confidence: 1.00]
def largest_party(n, friends, foes):
    adj = [[] for _ in range(n + 1)]
    for a, b in friends:
        adj[a].append(b)
        adj[b].append(a)
    group = [0] * (n + 1)
    sizes = [0]
    for start in range(1, n + 1):
        if group[start]:
            continue
        sizes.append(0)
        label = len(sizes) - 1
        stack = [start]
        group[start] = label
        while stack:
            node = stack.pop()
            sizes[label] += 1
            for nxt in adj[node]:
                if not group[nxt]:
                    group[nxt] = label
                    stack.append(nxt)
    blocked = [False] * len(sizes)
    for a, b in foes:
        if group[a] == group[b]:
            blocked[group[a]] = True
    best = 0
    for label in range(1, len(sizes)):
        if not blocked[label] and sizes[label] > best:
            best = sizes[label]
    return best

# Clause main [Confidence: 1.00]
def main():
    n, friends, foes = read_input()
    sys.stdout.write(str(largest_party(n, friends, foes)) + "\n")


if __name__ == "__main__":
    main()

