# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    parents = values[1:n]
    colors = values[n:n + n]

    head = [-1] * n
    to = [0] * max(0, n - 1)
    nxt = [0] * max(0, n - 1)

    for edge, parent in enumerate(parents):
        child = edge + 1
        to[edge] = child
        nxt[edge] = head[parent]
        head[parent] = edge

    stack = [(0, 0)]
    order = []
    while stack:
        node, seen = stack.pop()
        if seen:
            order.append(node)
        else:
            stack.append((node, 1))
            edge = head[node]
            while edge != -1:
                stack.append((to[edge], 0))
                edge = nxt[edge]

    dp0 = [0] * n
    dp1 = [0] * n

    for node in order:
        zero = 0 if colors[node] else 1
        one = 1 if colors[node] else 0
        edge = head[node]
        while edge != -1:
            child = to[edge]
            total = (dp0[child] + dp1[child]) % MOD
            next_zero = zero * total % MOD
            next_one = (one * total + zero * dp1[child]) % MOD
            zero = next_zero
            one = next_one
            edge = nxt[edge]
        dp0[node] = zero
        dp1[node] = one

    print(dp1[0] % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
