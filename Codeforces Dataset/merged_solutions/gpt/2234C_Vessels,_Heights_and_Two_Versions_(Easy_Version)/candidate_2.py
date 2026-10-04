# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
p = 1
out = []
for _ in range(t):
    n = data[p]
    p += 1
    h = data[p:p + n]
    p += n
    ans = []
    for s in range(n):
        w1 = [0] * n
        w2 = [0] * n
        for i in range(1, n):
            cur = (s + i) % n
            prev = (s + i - 1) % n
            w1[cur] = max(w1[prev], h[prev])
        for i in range(1, n):
            cur = (s - i) % n
            prev = (s - i + 1) % n
            w2[cur] = max(w2[prev], h[cur])
        ans.append(str(sum((min(w1[i], w2[i]) for i in range(n)))))
    out.append(' '.join(ans))
sys.stdout.write('\n'.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
