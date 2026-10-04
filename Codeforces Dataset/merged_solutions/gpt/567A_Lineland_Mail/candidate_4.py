# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1:]

    for i in range(n):
        if i == 0:
            mn = x[1] - x[0]
            mx = x[-1] - x[0]
        elif i == n - 1:
            mn = x[-1] - x[-2]
            mx = x[-1] - x[0]
        else:
            mn = min(x[i] - x[i - 1], x[i + 1] - x[i])
            mx = max(x[i] - x[0], x[-1] - x[i])
        print(mn, mx)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
