# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, root, arr, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [-2] * (n + 1)
    parent[root] = -1
    children = [[] for _ in range(n + 1)]
    order = [root]
    i = 0
    while i < len(order):
        v = order[i]
        i += 1
        for u in graph[v]:
            if parent[u] == -2:
                parent[u] = v
                children[v].append(u)
                order.append(u)

    size = [1] * (n + 1)
    sub = arr[:]
    for v in reversed(order):
        for u in children[v]:
            size[v] += size[u]
            sub[v] += sub[u]

    total = sub[root]
    parity = total & 1

    def feasible(moves):
        if moves < total or ((moves - total) & 1) != 0:
            return False
        whole, first = divmod(moves, n)

        prefix_hits = [0] * (n + 1)
        for v in range(1, n + 1):
            if v <= first:
                prefix_hits[v] = 1
        for v in reversed(order):
            for u in children[v]:
                prefix_hits[v] += prefix_hits[u]

        need = [0] * (n + 1)
        for v in reversed(order):
            child_sum = 0
            for u in children[v]:
                child_sum += need[u]
            lack = whole * size[v] + prefix_hits[v] - sub[v]
            best = child_sum
            if lack > best:
                best = lack
            if best < 0:
                best = 0
            if best & 1:
                best += 1
            need[v] = best

        demand = 0
        for u in children[root]:
            demand += need[u]
        return moves - total >= demand

    high = total
    while not feasible(high):
        high = high * 2 + 2

    low = parity - 2
    while high - low > 2:
        mid = low + ((high - low) // 2)
        if (mid & 1) != parity:
            mid += 1
        if mid >= high:
            mid -= 2
        if feasible(mid):
            high = mid
        else:
            low = mid
    return high

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    res = []
    for _ in range(t):
        n = data[idx]
        root = data[idx + 1]
        idx += 2
        arr = [0] + data[idx:idx + n]
        idx += n
        edges = []
        for _ in range(n - 1):
            edges.append((data[idx], data[idx + 1]))
            idx += 2
        res.append(str(solve_case(n, root, arr, edges)))
    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
