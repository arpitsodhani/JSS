# CLAUSE: setup_environment
import sys
from itertools import permutations

# CLAUSE: solve_logic
input = sys.stdin.readline
n, m = map(int, input().split())
s = input().strip()
patterns = [''.join(p) for p in permutations('abc')]
pref = [[0] * (n + 1) for _ in range(6)]
for k, p in enumerate(patterns):
    for i, ch in enumerate(s, 1):
        pref[k][i] = pref[k][i - 1] + (ch != p[(i - 1) % 3])
ans = []
for _ in range(m):
    l, r = map(int, input().split())
    ans.append(str(min((pref[k][r] - pref[k][l - 1] for k in range(6)))))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
