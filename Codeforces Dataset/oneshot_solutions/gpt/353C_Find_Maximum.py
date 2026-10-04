import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:1 + n]))
s = data[1 + n].strip()

total = 0
ans = 0

for i in range(n):
    if s[i] == '1':
        total += a[i]

ans = total
lower_sum = 0

for i in range(n):
    if s[i] == '1':
        total -= a[i]
        candidate = total + lower_sum
        if candidate > ans:
            ans = candidate
    lower_sum += a[i]

print(ans)
