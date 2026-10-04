import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
grades = data[1:1 + n]

grades.sort()
total = sum(grades)
target = 5 * n - n // 2

ans = 0
for g in grades:
    if total >= target:
        break
    total += 5 - g
    ans += 1

print(ans)
