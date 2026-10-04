import sys

a = list(map(int, sys.stdin.read().split()))
ans = 10**18

for start in range(3):
    for length in range(sum(a), sum(a) + 10):
        cnt = [0, 0, 0]
        for i in range(length):
            cnt[(start + i) % 3] += 1
        if all(cnt[i] >= a[i] for i in range(3)):
            ans = min(ans, length - sum(a))

print(ans)
