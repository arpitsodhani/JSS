# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    parent[1] = -1
    stack = [1]
    while stack:
        v = stack.pop()
        order.append(v)
        for to in adj[v]:
            if to != parent[v]:
                parent[to] = v
                children[v].append(to)
                stack.append(to)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    timer = 0
    for v in reversed(order):
        timer += 1
        left[v] = timer
        for c in reversed(children[v]):
            timer += 1
            right[c] = timer
    timer += 1
    right[1] = timer
    out = []
    for i in range(1, n + 1):
        out.append(f'{left[i]} {right[i]}')
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
