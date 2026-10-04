# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]

    runs = []
    cnt = 1

    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            runs.append(cnt)
            cnt = 1

    runs.append(cnt)

    ans = 0
    for i in range(1, len(runs)):
        ans = max(ans, 2 * min(runs[i - 1], runs[i]))

    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
