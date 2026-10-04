# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, a = (data[0], data[1], data[2])
    b = data[3:3 + n]
    p = data[3 + n:3 + n + m]
    b.sort()
    p.sort()
    pref = [0]
    for x in p:
        pref.append(pref[-1] + x)

    def can(k):
        need = 0
        start = n - k
        for i in range(k):
            if p[i] > b[start + i]:
                need += p[i] - b[start + i]
                if need > a:
                    return False
        return True
    lo, hi = (0, min(n, m))
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1
    k = lo
    personal = max(0, pref[k] - a)
    print(k, personal)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
