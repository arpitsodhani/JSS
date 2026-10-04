import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, k, q = data[0], data[1], data[2]

MAX_T = 200000
diff = [0] * (MAX_T + 2)

idx = 3
for _ in range(n):
    l = data[idx]
    r = data[idx + 1]
    idx += 2
    diff[l] += 1
    diff[r + 1] -= 1

pref = [0] * (MAX_T + 1)
cur = 0
for t in range(1, MAX_T + 1):
    cur += diff[t]
    pref[t] = pref[t - 1] + (1 if cur >= k else 0)

out = []
for _ in range(q):
    a = data[idx]
    b = data[idx + 1]
    idx += 2
    out.append(str(pref[b] - pref[a - 1]))

sys.stdout.write("\n".join(out))
