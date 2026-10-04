# CLAUSE: derive_sum_transform
import sys

def compute(a):
    layer = a[:]
    best_seen = sum(layer)

    # CLAUSE: evaluate_orientation_choice
    while len(layer) != 1:
        left = layer[0]
        right = layer[-1]
        sign = 1
        if right - left < 0:
            sign = -1

        # CLAUSE: generate_difference_layer
        next_layer = [0] * (len(layer) - 1)
        for j in range(len(next_layer)):
            next_layer[j] = sign * (layer[j + 1] - layer[j])
        layer = next_layer

        # CLAUSE: track_best_sequence_sum
        candidate = sum(layer)
        if candidate > best_seen:
            best_seen = candidate
    # CLAUSE: handle_signed_extremes
    return best_seen

raw = sys.stdin.buffer.read().split()
t = int(raw[0])
p = 1
answers = []
for _ in range(t):
    n = int(raw[p])
    p += 1
    arr = [int(raw[p + i]) for i in range(n)]
    p += n
    answers.append(str(compute(arr)))
print("\n".join(answers))
