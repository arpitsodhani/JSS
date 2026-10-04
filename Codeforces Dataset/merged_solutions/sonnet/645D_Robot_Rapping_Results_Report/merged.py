import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    battles = []
    pos = 2
    for _ in range(m):
        u = int(data[pos])
        v = int(data[pos + 1])
        pos += 2
        battles.append((u, v))
    return n, m, battles

# Clause unique_order [Confidence: 1.00]
def unique_order(n, battles, k):
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(k):
        u, v = battles[i]
        adj[u].append(v)
        indeg[v] += 1
    ready = []
    for node in range(1, n + 1):
        if indeg[node] == 0:
            ready.append(node)
    for _ in range(n):
        if len(ready) != 1:
            return False
        node = ready.pop()
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                ready.append(nxt)
    return True

# Clause find_answer [Confidence: 1.00]
def find_answer(n, m, battles):
    if not unique_order(n, battles, m):
        return -1
    low = 1
    high = m
    while low < high:
        mid = (low + high) // 2
        if unique_order(n, battles, mid):
            high = mid
        else:
            low = mid + 1
    return low

# Clause main [Confidence: 1.00]
def main():
    n, m, battles = read_input()
    sys.stdout.write(str(find_answer(n, m, battles)) + "\n")


if __name__ == "__main__":
    main()

