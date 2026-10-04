# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    input = sys.stdin.readline

    t = int(input())
    out = []

    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))

        if n == 2 or m < n:
            out.append("-1")
            continue

        order = sorted(range(n), key=lambda i: a[i])
        x, y = order[0], order[1]

        cost = 2 * sum(a) + (m - n) * (a[x] + a[y])
        out.append(str(cost))

        for i in range(n):
            out.append(f"{i + 1} {(i + 1) % n + 1}")

        for _ in range(m - n):
            out.append(f"{x + 1} {y + 1}")

    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
