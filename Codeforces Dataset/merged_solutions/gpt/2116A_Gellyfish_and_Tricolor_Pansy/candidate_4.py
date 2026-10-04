# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []
    idx = 1

    for _ in range(t):
        a, b, c, d = data[idx:idx + 4]
        idx += 4
        if min(b, d) <= min(a, c):
            ans.append("Gellyfish")
        else:
            ans.append("Flower")

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
