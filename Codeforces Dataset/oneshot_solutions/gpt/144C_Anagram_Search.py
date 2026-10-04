import sys

data = sys.stdin.read().split()
if len(data) < 2:
    sys.exit()

s, p = data[0], data[1]
n, m = len(s), len(p)

if m > n:
    print(0)
    sys.exit()

need = [0] * 26
for ch in p:
    need[ord(ch) - 97] += 1

have = [0] * 26
bad = 0
q = 0

for i in range(m):
    ch = s[i]
    if ch == '?':
        q += 1
    else:
        idx = ord(ch) - 97
        have[idx] += 1
        if have[idx] == need[idx] + 1:
            bad += 1

ans = 1 if bad == 0 else 0

for r in range(m, n):
    left = s[r - m]
    if left == '?':
        q -= 1
    else:
        idx = ord(left) - 97
        if have[idx] == need[idx] + 1:
            bad -= 1
        have[idx] -= 1

    ch = s[r]
    if ch == '?':
        q += 1
    else:
        idx = ord(ch) - 97
        have[idx] += 1
        if have[idx] == need[idx] + 1:
            bad += 1

    if bad == 0:
        ans += 1

print(ans)
