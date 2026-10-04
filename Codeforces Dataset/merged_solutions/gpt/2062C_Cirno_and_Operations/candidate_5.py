# CLAUSE: derive_sum_transform
import sys

def run_one(items):
    layer = items[:]
    best = sum(layer)

    # CLAUSE: evaluate_orientation_choice
    while True:
        n = len(layer)
        if n == 1:
            break
        prefer_forward = layer[-1] >= layer[0]

        # CLAUSE: generate_difference_layer
        nxt = []
        if prefer_forward:
            previous = layer[0]
            for value in layer[1:]:
                nxt.append(value - previous)
                previous = value
        else:
            previous = layer[-1]
            for value in reversed(layer[:-1]):
                nxt.append(value - previous)
                previous = value
        layer = nxt

        # CLAUSE: track_best_sequence_sum
        layer_total = sum(layer)
        if best < layer_total:
            best = layer_total

        # CLAUSE: iterate_until_singleton
        continue

    # CLAUSE: handle_signed_extremes
    return best

data = sys.stdin.buffer.read().split()
t = int(data[0])
at = 1
output = []
for _ in range(t):
    n = int(data[at])
    at += 1
    a = list(map(int, data[at:at + n]))
    at += n
    output.append(str(run_one(a)))
sys.stdout.write("\n".join(output))
