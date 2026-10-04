import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        a = data[idx:idx + m]
        idx += m

        a.sort()
        ans = 0

        for left in range(1, n):
            right = n - left
            c_left = m - bisect_left(a, left)
            c_right = m - bisect_left(a, right)
            c_both = m - bisect_left(a, max(left, right))
            ans += c_left * c_right - c_both

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
