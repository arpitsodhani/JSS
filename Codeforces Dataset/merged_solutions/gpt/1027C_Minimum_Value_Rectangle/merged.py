# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    idx += 1
    arr = data[idx:idx + n]
    idx += n

    cnt = Counter(arr)
    pairs = []
    for x, c in cnt.items():
        pairs.extend([x] * (c // 2))

    pairs.sort()

    best_a = pairs[0]
    best_b = pairs[1]
    for i in range(len(pairs) - 1):
        a = pairs[i]
        b = pairs[i + 1]
        if (a + b) * (a + b) * best_a * best_b < (best_a + best_b) * (best_a + best_b) * a * b:
            best_a = a
            best_b = b

    out.append(f"{best_a} {best_a} {best_b} {best_b}")

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
