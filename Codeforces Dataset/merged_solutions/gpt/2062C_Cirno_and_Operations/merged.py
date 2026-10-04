# Clause derive_sum_transform [Confidence: 1.00]
import sys

def compute(a):
    layer = a[:]
    best_seen = sum(layer)


# Clause evaluate_orientation_choice [Confidence: 0.20]
    while len(cur) > 1:
        edge_gain = cur[-1] - cur[0]
        if edge_gain < 0:
            cur.reverse()


# Clause generate_difference_layer [Confidence: 0.40]
        nxt = []
        for i in range(len(cur) - 1):
            nxt.append(cur[i + 1] - cur[i])
        cur = nxt


# Clause track_best_sequence_sum [Confidence: 0.60]
        candidate = sum(layer)
        if candidate > best_seen:
            best_seen = candidate


# Clause iterate_until_singleton [Confidence: 0.40]
        continue


# Clause handle_signed_extremes [Confidence: 1.00]
    return ans

tokens = list(map(int, sys.stdin.buffer.read().split()))
cases = tokens[0]
idx = 1
res = []
for _ in range(cases):
    size = tokens[idx]
    idx += 1
    res.append(str(answer(tokens[idx:idx + size])))
    idx += size
sys.stdout.write("\n".join(res))


