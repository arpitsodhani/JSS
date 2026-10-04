# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = int(sys.stdin.readline())

    ans = []
    cur = 1
    while n >= cur:
        ans.append(cur)
        n -= cur
        cur += 1

    if n:
        ans[-1] += n

    print(len(ans))
    print(*ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
