# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]

    b = [x.bit_count() for x in a]

    cnt = [1, 0]
    p = 0
    ans = 0

    for x in b:
        p ^= x & 1
        ans += cnt[p]
        cnt[p] += 1

    limit = 2 * max(b) + 1 if b else 0

    bad = 0
    for l in range(n):
        s = 0
        m = 0
        for r in range(l, min(n, l + limit)):
            s += b[r]
            if b[r] > m:
                m = b[r]
            if s % 2 == 0 and m * 2 > s:
                bad += 1

    print(ans - bad)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
