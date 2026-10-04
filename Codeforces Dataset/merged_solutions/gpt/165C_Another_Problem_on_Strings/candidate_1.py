# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
k = int(data[0])
s = data[1]

if k == 0:
    ans = 0
    cur = 0
    for ch in s:
        if ch == '0':
            cur += 1
        else:
            ans += cur * (cur + 1) // 2
            cur = 0
    ans += cur * (cur + 1) // 2
    print(ans)
else:
    ones = [-1]
    for i, ch in enumerate(s):
        if ch == '1':
            ones.append(i)
    ones.append(len(s))

    ans = 0
    m = len(ones) - 2
    for i in range(1, m - k + 2):
        left = ones[i] - ones[i - 1]
        right = ones[i + k] - ones[i + k - 1]
        ans += left * right

    print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
