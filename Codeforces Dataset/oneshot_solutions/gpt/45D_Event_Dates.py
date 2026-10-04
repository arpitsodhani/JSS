import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    intervals = []
    p = 1
    for i in range(n):
        l = data[p]
        r = data[p + 1]
        p += 2
        intervals.append((r, l, i))

    intervals.sort()

    used = set()
    ans = [0] * n

    for r, l, i in intervals:
        day = l
        while day in used:
            day += 1
        ans[i] = day
        used.add(day)

    print(*ans)

if __name__ == "__main__":
    main()
