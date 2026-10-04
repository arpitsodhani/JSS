import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    a = data[2:2 + m]

    if n == 1:
        for i, v in enumerate(a, 1):
            if v > 0:
                print(i)
                return
        print(-1)
        return

    cap = n // 2

    if sum(min(x, cap) for x in a) < n:
        print(-1)
        return

    chosen = []
    rem = n
    for i, x in enumerate(a, 1):
        take = min(x, cap, rem)
        if take:
            chosen.append((take, i))
            rem -= take
        if rem == 0:
            break

    chosen.sort(reverse=True)

    positions = list(range(0, n, 2)) + list(range(1, n, 2))
    ans = [0] * n
    p = 0

    for cnt, idx in chosen:
        for _ in range(cnt):
            ans[positions[p]] = idx
            p += 1

    print(*ans)

if __name__ == "__main__":
    main()
