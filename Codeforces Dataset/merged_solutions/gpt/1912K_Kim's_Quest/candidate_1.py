# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1 + n]

single = [0, 0]
pair = [[0, 0], [0, 0]]
ans = 0

for v in a:
    x = v & 1

    nsingle = single[:]
    npair = [row[:] for row in pair]

    nsingle[x] = (nsingle[x] + 1) % MOD

    for y in range(2):
        npair[y][x] = (npair[y][x] + single[y]) % MOD

    for u in range(2):
        for y in range(2):
            if (u + y + x) % 2 == 0:
                cnt = pair[u][y]
                npair[y][x] = (npair[y][x] + cnt) % MOD
                ans = (ans + cnt) % MOD

    single = nsingle
    pair = npair

print(ans % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
