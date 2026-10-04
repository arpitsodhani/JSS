import sys

s = sys.stdin.readline().strip()
ans = 0

for i, ch in enumerate(s):
    if int(ch) % 4 == 0:
        ans += 1
    if i > 0:
        x = int(s[i - 1:i + 1])
        if x % 4 == 0:
            ans += i

print(ans)
