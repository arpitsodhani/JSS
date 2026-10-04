import sys

data = sys.stdin.read().split()
s = data[0]
t = data[1]

n = len(s)
m = len(t)

cnt = [0] * 26
for ch in s:
    cnt[ord(ch) - 97] += 1

limit = min(n, m)
snapshots = [cnt.copy()]

for i in range(limit):
    x = ord(t[i]) - 97
    if cnt[x] == 0:
        break
    cnt[x] -= 1
    snapshots.append(cnt.copy())

p = len(snapshots) - 1

def tail(counts):
    return ''.join(chr(i + 97) * counts[i] for i in range(26))

if n > m and p >= m:
    print(t + tail(snapshots[m]))
    sys.exit()

for k in range(min(p, limit - 1), -1, -1):
    counts = snapshots[k].copy()
    need = ord(t[k]) - 97
    for c in range(need + 1, 26):
        if counts[c] > 0:
            counts[c] -= 1
            print(t[:k] + chr(c + 97) + tail(counts))
            sys.exit()

print(-1)
