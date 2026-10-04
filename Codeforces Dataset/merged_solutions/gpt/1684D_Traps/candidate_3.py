# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        total = sum(a)
        gains = [a[i] + i for i in range(n)]
        gains.sort(reverse=True)
        ans = total - sum(gains[:k]) + k * (n - 1) - k * (k - 1) // 2
        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
