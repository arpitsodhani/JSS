# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(300000)

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    nxt = [0] + values[1:n + 1]
    back = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        back[nxt[i]].append(i)

    index = 0
    stack = []
    in_stack = [False] * (n + 1)
    tin = [0] * (n + 1)
    low = [0] * (n + 1)
    comp = [0] * (n + 1)
    reps = []

    def dfs(v):
        nonlocal index
        index += 1
        tin[v] = index
        low[v] = index
        stack.append(v)
        in_stack[v] = True

        to = nxt[v]
        if tin[to] == 0:
            dfs(to)
            if low[to] < low[v]:
                low[v] = low[to]
        elif in_stack[to] and tin[to] < low[v]:
            low[v] = tin[to]

        if low[v] == tin[v]:
            reps.append(v)
            cid = len(reps)
            while True:
                u = stack.pop()
                in_stack[u] = False
                comp[u] = cid
                if u == v:
                    break

    for node in range(1, n + 1):
        if tin[node] == 0:
            dfs(node)

    comp_count = len(reps)
    if comp_count == 1:
        print(0)
        return

    indeg = [0] * (comp_count + 1)
    outdeg = [0] * (comp_count + 1)
    for v in range(1, n + 1):
        a = comp[v]
        b = comp[nxt[v]]
        if a != b:
            outdeg[a] += 1
            indeg[b] += 1

    sources = []
    sinks = []
    for cid in range(1, comp_count + 1):
        if indeg[cid] == 0:
            sources.append(cid)
        if outdeg[cid] == 0:
            sinks.append(cid)

    need = len(sources)
    if len(sinks) > need:
        need = len(sinks)

    answer = [str(need)]
    s_len = len(sources)
    t_len = len(sinks)
    for i in range(need):
        x = reps[sinks[i % t_len] - 1]
        y = reps[sources[(i + 1) % s_len] - 1]
        answer.append(f"{x} {y}")

    sys.stdout.write("\n".join(answer) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
