# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_right

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = sorted(a[i] - b[i] for i in range(n))

    ans = 0
    for i in range(n):
        ans += n - bisect_right(d, -d[i], i + 1)

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
