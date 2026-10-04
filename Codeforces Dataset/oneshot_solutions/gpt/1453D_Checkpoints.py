import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    if k % 2:
        print(-1)
        continue

    k //= 2
    ans = []
    first = True

    while k:
        x = k.bit_length() - 1
        if not first:
            ans.append(0)
        ans.extend([1] * x)
        k -= 1 << x
        first = False

    print(len(ans))
    print(*ans)
