import sys

data = sys.stdin.read().split()
a = int(data[0])
s = data[1]

digits = [ord(c) - 48 for c in s]
n = len(digits)
max_sum = 9 * n
cnt = [0] * (max_sum + 1)

for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += digits[j]
        cnt[sm] += 1

total = n * (n + 1) // 2

if a == 0:
    z = cnt[0]
    ans = z * total * 2 - z * z
else:
    ans = 0
    d = 1
    while d * d <= a:
        if a % d == 0:
            e = a // d
            if d <= max_sum and e <= max_sum:
                if d == e:
                    ans += cnt[d] * cnt[e]
                else:
                    ans += cnt[d] * cnt[e] * 2
        d += 1

print(ans)
