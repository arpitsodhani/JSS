# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
ans = []
for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2
    a = data[idx:idx + n]
    idx += n
    diffs = [abs(a[i] - a[i - 1]) for i in range(1, n)]
    total = sum(diffs)
    diffs.sort(reverse=True)
    ans.append(str(total - sum(diffs[:k - 1])))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
