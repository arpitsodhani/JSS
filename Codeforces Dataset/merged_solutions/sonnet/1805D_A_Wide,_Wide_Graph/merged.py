import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    pos = 1
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, adj

# Clause distances [Confidence: 1.00]
def distances(n, adj, source):
    dist = [-1] * (n + 1)
    dist[source] = 0
    queue = [source]
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        step = dist[node] + 1
        for nxt in adj[node]:
            if dist[nxt] < 0:
                dist[nxt] = step
                queue.append(nxt)
    return dist

# Clause component_counts [Confidence: 1.00]
def component_counts(n, adj):
    first = distances(n, adj, 1)
    far = 1
    for v in range(1, n + 1):
        if first[v] > first[far]:
            far = v
    from_one = distances(n, adj, far)
    other = far
    for v in range(1, n + 1):
        if from_one[v] > from_one[other]:
            other = v
    from_two = distances(n, adj, other)
    reach = [0] * (n + 2)
    for v in range(1, n + 1):
        span = from_one[v] if from_one[v] > from_two[v] else from_two[v]
        reach[span] += 1
    answer = []
    isolated = 0
    for k in range(1, n + 1):
        isolated += reach[k - 1]
        answer.append(isolated + (1 if isolated < n else 0))
    return answer

# Clause main [Confidence: 1.00]
def main():
    n, adj = read_input()
    sys.stdout.write(" ".join(map(str, component_counts(n, adj))) + "\n")


if __name__ == "__main__":
    main()

