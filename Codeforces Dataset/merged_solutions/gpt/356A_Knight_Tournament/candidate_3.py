# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n, m = data[0], data[1]
    parent = list(range(n + 2))
    ans = [0] * (n + 1)

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    idx = 2
    for _ in range(m):
        l, r, x = data[idx], data[idx + 1], data[idx + 2]
        idx += 3

        cur = find(l)
        while cur <= r:
            if cur == x:
                cur = find(cur + 1)
            else:
                ans[cur] = x
                parent[cur] = find(cur + 1)
                cur = find(cur)

    print(" ".join(map(str, ans[1:])))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
