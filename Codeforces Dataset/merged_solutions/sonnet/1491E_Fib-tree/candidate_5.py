# CLAUSE: setup_environment
import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    fib = [1, 1]
    index = {1: 1}
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
        index[fib[-1]] = len(fib) - 1
    if n not in index:
        print("NO")
        return
    neighbors = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        u = nums[1 + 2 * i]
        v = nums[2 + 2 * i]
        neighbors[u].append((v, i))
        neighbors[v].append((u, i))

# CLAUSE: solve_logic
    gone = [False] * max(1, n - 1)
    parent = [0] * (n + 1)
    edge_to_parent = [-1] * (n + 1)
    subtree = [0] * (n + 1)

    def choose_edge(root, k):
        a = fib[k - 1]
        b = fib[k - 2]
        order = []
        stack = [root]
        parent[root] = 0
        edge_to_parent[root] = -1
        while stack:
            v = stack.pop()
            order.append(v)
            for to, eid in neighbors[v]:
                if not gone[eid] and to != parent[v]:
                    parent[to] = v
                    edge_to_parent[to] = eid
                    stack.append(to)
        chosen = -1
        for v in reversed(order):
            subtotal = 1
            for to, eid in neighbors[v]:
                if not gone[eid] and parent[to] == v:
                    subtotal += subtree[to]
            subtree[v] = subtotal
            if chosen == -1 and v != root and (subtotal == a or subtotal == b):
                chosen = v
        return chosen

    stack = [(1, index[n])]
    possible = True
    while stack and possible:
        root, k = stack.pop()
        if k <= 1:
            continue
        child = choose_edge(root, k)
        if child == -1:
            possible = False
            break
        gone[edge_to_parent[child]] = True
        if subtree[child] == fib[k - 1]:
            stack.append((root, k - 2))
            stack.append((child, k - 1))
        else:
            stack.append((root, k - 1))
            stack.append((child, k - 2))

# CLAUSE: finish_program
    print("YES" if possible else "NO")

if __name__ == "__main__":
    main()
