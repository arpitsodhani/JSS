# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        deg = [0] * n
        edges = []

        for _ in range(n - 1):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            edges.append((u, v))
            deg[u] += 1
            deg[v] += 1

        if n <= 3:
            ans.append("0")
            continue

        leaves = sum(1 for d in deg if d == 1)
        near = [0] * n

        for u, v in edges:
            if deg[u] == 1:
                near[v] += 1
            if deg[v] == 1:
                near[u] += 1

        ans.append(str(leaves - max(near)))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
