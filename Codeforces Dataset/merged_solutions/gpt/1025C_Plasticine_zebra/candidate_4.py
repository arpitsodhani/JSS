# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.readline().strip()
    n = len(s)

    if n == 0:
        print(0)
    else:
        t = s + s
        best = 1
        cur = 1

        for i in range(1, len(t)):
            if t[i] != t[i - 1]:
                cur += 1
            else:
                cur = 1
            if cur > best:
                best = cur

        print(min(best, n))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
