# CLAUSE: derive_sum_transform
import sys

def solve_case(arr):
    best = sum(arr)
    cur = arr[:]

    # CLAUSE: evaluate_orientation_choice
    while len(cur) > 1:
        edge_gain = cur[-1] - cur[0]
        if edge_gain < 0:
            cur.reverse()

        # CLAUSE: generate_difference_layer
        nxt = []
        for i in range(len(cur) - 1):
            nxt.append(cur[i + 1] - cur[i])
        cur = nxt

        # CLAUSE: track_best_sequence_sum
        layer_sum = sum(cur)
        if layer_sum > best:
            best = layer_sum

        # CLAUSE: iterate_until_singleton
        continue

    # CLAUSE: handle_signed_extremes
    return best

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
pos = 1
out = []
for _ in range(t):
    n = data[pos]
    pos += 1
    a = data[pos:pos + n]
    pos += n
    out.append(str(solve_case(a)))
print("\n".join(out))
