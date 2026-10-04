# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1:]
    pref = [0]
    cur = 0
    mn = 0
    for x in q:
        cur += x
        pref.append(cur)
        if cur < mn:
            mn = cur
    start = 1 - mn
    p = [start + x for x in pref]
    if min(p) == 1 and max(p) == n and (len(set(p)) == n):
        print(*p)
    else:
        print(-1)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
