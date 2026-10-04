# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = []
        for i, v in enumerate(a, 1):
            p = 1
            while p < v:
                p <<= 1
            ans.append((i, p - v))
        print(len(ans))
        for i, x in ans:
            print(i, x)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
