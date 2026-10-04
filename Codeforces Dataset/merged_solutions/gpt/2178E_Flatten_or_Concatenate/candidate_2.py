# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def ask(l, r):
    print('?', l, r, flush=True)
    x = int(sys.stdin.readline())
    if x == -1:
        sys.exit()
    return x

def answer(x):
    print('!', x, flush=True)

def solve(n):
    l, r = (1, n)
    total = ask(1, n)
    while l < r and total > 1:
        target = total // 2
        lo, hi = (l, r)
        while lo < hi:
            mid = (lo + hi) // 2
            s = ask(l, mid)
            if s >= target:
                hi = mid
            else:
                lo = mid + 1
        p = lo
        if p - l + 1 <= r - p:
            r = p
        else:
            l = p + 1
        total = target
    answer(total)

def main():
    t_line = sys.stdin.readline()
    if not t_line:
        return
    t = int(t_line)
    for _ in range(t):
        n = int(sys.stdin.readline())
        solve(n)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
