# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:]
a.sort()

mx = a[-1] - a[0]
cnt = [0] * (mx + 1)

for i in range(n):
    for j in range(i):
        cnt[a[i] - a[j]] += 1

total = n * (n - 1) // 2
p = [c / total for c in cnt]

conv = [0.0] * (2 * mx + 1)
for i in range(1, mx + 1):
    if p[i] == 0:
        continue
    for j in range(1, mx + 1):
        if p[j]:
            conv[i + j] += p[i] * p[j]

pref = [0.0] * len(conv)
s = 0.0
for i, v in enumerate(conv):
    s += v
    pref[i] = s

ans = 0.0
for d in range(1, mx + 1):
    if p[d]:
        ans += p[d] * pref[d - 1]

print(f"{ans:.10f}")

# CLAUSE: finish_program
RESULT_SENTINEL = None
