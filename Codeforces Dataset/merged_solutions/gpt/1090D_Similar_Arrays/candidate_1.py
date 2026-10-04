# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [set() for _ in range(n)]

    idx = 2
    for _ in range(m):
        a = data[idx] - 1
        b = data[idx + 1] - 1
        idx += 2
        adj[a].add(b)
        adj[b].add(a)

    if m == n * (n - 1) // 2:
        print("NO")
        return

    u = v = -1
    for i in range(n):
        if len(adj[i]) < n - 1:
            u = i
            for j in range(n):
                if i != j and j not in adj[i]:
                    v = j
                    break
            break

    a = [0] * n
    b = [0] * n
    a[u] = 1
    a[v] = 2
    b[u] = 1
    b[v] = 1

    cur = 3
    for i in range(n):
        if i != u and i != v:
            a[i] = cur
            b[i] = cur
            cur += 1

    print("YES")
    print(*a)
    print(*b)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
