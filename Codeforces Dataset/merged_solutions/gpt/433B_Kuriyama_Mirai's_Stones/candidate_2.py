# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0
n = data[idx]
idx += 1
v = data[idx:idx + n]
idx += n
pref = [0] * (n + 1)
for i, x in enumerate(v, 1):
    pref[i] = pref[i - 1] + x
v.sort()
spref = [0] * (n + 1)
for i, x in enumerate(v, 1):
    spref[i] = spref[i - 1] + x
m = data[idx]
idx += 1
out = []
for _ in range(m):
    t = data[idx]
    l = data[idx + 1]
    r = data[idx + 2]
    idx += 3
    if t == 1:
        out.append(str(pref[r] - pref[l - 1]))
    else:
        out.append(str(spref[r] - spref[l - 1]))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
