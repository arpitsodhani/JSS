import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    c = input().strip()
    a = input().strip()

    groups = [[] for _ in range(4)]
    for i, (x, y) in enumerate(zip(c, a), 1):
        if x == '0' and y == '0':
            groups[0].append(i)
        elif x == '0' and y == '1':
            groups[1].append(i)
        elif x == '1' and y == '0':
            groups[2].append(i)
        else:
            groups[3].append(i)

    cnt00, cnt01, cnt10, cnt11 = map(len, groups)
    need_size = n // 2
    total_a = cnt01 + cnt11

    for take11 in range(cnt11 + 1):
        take_sum1 = total_a - 2 * take11
        take00 = need_size - take_sum1 - take11

        if take_sum1 < 0 or take00 < 0 or take00 > cnt00:
            continue

        lo = max(0, take_sum1 - cnt10)
        hi = min(cnt01, take_sum1)

        if lo <= hi:
            take01 = lo
            take10 = take_sum1 - take01

            ans = (
                groups[0][:take00] +
                groups[1][:take01] +
                groups[2][:take10] +
                groups[3][:take11]
            )
            print(*ans)
            return

    print(-1)

if __name__ == "__main__":
    main()
