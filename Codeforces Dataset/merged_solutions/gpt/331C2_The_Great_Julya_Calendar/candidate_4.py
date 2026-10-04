# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from array import array

    B = 10 ** 6
    n = int(sys.stdin.readline())

    mx = bytearray(B + 1)
    for i in range(1, B + 1):
        q = i // 10
        r = i - q * 10
        v = mx[q]
        mx[i] = r if r > v else v

    last = array('I', [0]) * B
    for i in range(1, B):
        last[i] = last[i - mx[i]] + 1

    cnt = [None] * 10
    neg = [None] * 10

    for h in range(1, 10):
        c = array('I', [0]) * B
        e = array('b', [0]) * B
        for x in range(B):
            m = mx[x]
            d = h if h > m else m
            y = x - d
            if y < 0:
                c[x] = 1
                e[x] = y
            else:
                c[x] = c[y] + 1
                e[x] = e[y]
        cnt[h] = c
        neg[h] = e

    ans = 0
    while n >= B:
        a, b = divmod(n, B)
        h = mx[a]
        ans += cnt[h][b]
        n = a * B + neg[h][b]

    ans += last[n]
    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
