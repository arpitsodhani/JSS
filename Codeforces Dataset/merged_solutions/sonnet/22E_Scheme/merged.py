# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return

    n = raw[0]
    to = [0] + raw[1:n + 1]

    incoming = [[] for _ in range(n + 1)]
    indegree_nodes = [0] * (n + 1)
    for v in range(1, n + 1):
        incoming[to[v]].append(v)
        indegree_nodes[to[v]] += 1

    removed = [False] * (n + 1)
    q = deque(i for i in range(1, n + 1) if indegree_nodes[i] == 0)
    while q:
        v = q.popleft()
        removed[v] = True
        u = to[v]
        indegree_nodes[u] -= 1
        if indegree_nodes[u] == 0:
            q.append(u)

    comp = [0] * (n + 1)
    reps = []
    for start in range(1, n + 1):
        if removed[start] or comp[start]:
            continue
        reps.append(start)
        cid = len(reps)
        v = start
        while comp[v] == 0:
            comp[v] = cid
            v = to[v]

    for v in range(1, n + 1):
        if comp[v] == 0:
            reps.append(v)
            comp[v] = len(reps)

    total = len(reps)
    if total == 1:
        sys.stdout.write("0\n")
        return

    indeg = [0] * (total + 1)
    outdeg = [0] * (total + 1)
    for v in range(1, n + 1):
        a = comp[v]
        b = comp[to[v]]
        if a != b:
            outdeg[a] = 1
            indeg[b] += 1

    sources = []
    sinks = []
    for cid in range(1, total + 1):
        if indeg[cid] == 0:
            sources.append(cid)
        if outdeg[cid] == 0:
            sinks.append(cid)

    m = max(len(sources), len(sinks))
    result = [str(m)]
    for i in range(m):
        result.append("{} {}".format(reps[sinks[i % len(sinks)] - 1], reps[sources[(i + 1) % len(sources)] - 1]))

    sys.stdout.write("\n".join(result) + "\n")


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


