# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    input = sys.stdin.readline

    t = int(input())
    ans = []

    for _ in range(t):
        n = int(input())
        c = list(map(int, input().split()))

        ok = min(c) == 1
        for i in range(n):
            if c[i] - c[i - 1] > 1:
                ok = False
                break

        ans.append("YES" if ok else "NO")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
