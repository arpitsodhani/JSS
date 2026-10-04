# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []

    for n in data[1:1 + t]:
        if n % 2 == 0:
            ans.append("-1")
        else:
            ans.append(" ".join(str((2 * i) % n + 1) for i in range(n)))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
