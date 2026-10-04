import sys

s = sys.stdin.readline().strip()

boys = 0
ans = 0

for c in s:
    if c == 'M':
        boys += 1
    elif boys:
        ans = max(ans + 1, boys)

print(ans)
