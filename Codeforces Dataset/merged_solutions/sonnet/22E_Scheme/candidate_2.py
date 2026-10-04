# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    f = [0] + data[1:n + 1]

    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].append(f[i])
        rev[f[i]].append(i)

    seen = [0] * (n + 1)
    order = []
    for start in range(1, n + 1):
        if seen[start]:
            continue
        stack = [(start, 0)]
        seen[start] = 1
        while stack:
            v, idx = stack[-1]
            if idx < len(graph[v]):
                to = graph[v][idx]
                stack[-1] = (v, idx + 1)
                if not seen[to]:
                    seen[to] = 1
                    stack.append((to, 0))
            else:
                order.append(v)
                stack.pop()

    comp = [0] * (n + 1)
    reps = []
    count = 0
    for start in reversed(order):
        if comp[start]:
            continue
        count += 1
        reps.append(start)
        comp[start] = count
        stack = [start]
        while stack:
            v = stack.pop()
            for to in rev[v]:
                if comp[to] == 0:
                    comp[to] = count
                    stack.append(to)

    if count == 1:
        sys.stdout.write("0\n")
        return

    indeg = [0] * (count + 1)
    outdeg = [0] * (count + 1)
    for v in range(1, n + 1):
        a = comp[v]
        b = comp[f[v]]
        if a != b:
            outdeg[a] += 1
            indeg[b] += 1

    sources = [i for i in range(1, count + 1) if indeg[i] == 0]
    sinks = [i for i in range(1, count + 1) if outdeg[i] == 0]
    k = max(len(sources), len(sinks))

    lines = [str(k)]
    for i in range(k):
        lines.append(str(reps[sinks[i % len(sinks)] - 1]) + " " + str(reps[sources[(i + 1) % len(sources)] - 1]))
    sys.stdout.write("\n".join(lines) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
