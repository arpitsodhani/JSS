# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def ask(l, r):
        print("?", l, r, flush=True)
        return int(sys.stdin.readline())

    n = int(sys.stdin.readline())
    s = ask(1, n)

    if s < n and ask(s, n) == s:
        l, r = s + 1, n
        while l < r:
            m = (l + r) // 2
            if ask(s, m) == s:
                r = m
            else:
                l = m + 1
        print("!", l, flush=True)
    else:
        l, r = 1, s - 1
        while l < r:
            m = (l + r + 1) // 2
            if ask(m, s) == s:
                l = m
            else:
                r = m - 1
        print("!", l, flush=True)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
