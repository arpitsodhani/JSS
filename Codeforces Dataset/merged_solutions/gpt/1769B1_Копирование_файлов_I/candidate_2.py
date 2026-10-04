# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def ceil_div(a, b):
    return (a + b - 1) // b

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    total = sum(a)
    ok = [False] * 101
    ok[0] = True
    pref = 0
    for size in a:
        for p in range(101):
            if p == 100:
                l1 = r1 = size
                l2 = r2 = total
            else:
                l1 = ceil_div(p * size, 100)
                r1 = ceil_div((p + 1) * size, 100) - 1
                l2 = ceil_div(p * total, 100)
                r2 = ceil_div((p + 1) * total, 100) - 1
            l = max(1, l1, l2 - pref)
            r = min(size, r1, r2 - pref)
            if l <= r:
                ok[p] = True
        pref += size
    print('\n'.join((str(i) for i in range(101) if ok[i])))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
