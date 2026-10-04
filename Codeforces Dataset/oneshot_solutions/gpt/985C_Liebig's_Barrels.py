import sys
import bisect

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k, l = data[0], data[1], data[2]
    a = data[3:]
    a.sort()

    limit = a[0] + l
    cnt = bisect.bisect_right(a, limit)

    if cnt < n:
        print(0)
        return

    ans = 0
    idx = 0

    for i in range(n):
        ans += a[idx]
        remaining = n - i - 1
        idx += min(k, cnt - idx - remaining)

    print(ans)

if __name__ == "__main__":
    main()
