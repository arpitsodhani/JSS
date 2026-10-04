# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        b = a[:]
        b[0::2] = sorted(b[0::2])
        b[1::2] = sorted(b[1::2])

        print("YES" if b == sorted(a) else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
