# CLAUSE: derive_sum_transform
import sys

def maximum_sum(sequence):
    layer = sequence[:]
    result = sum(layer)

    # CLAUSE: evaluate_orientation_choice
    for width in range(len(layer), 1, -1):
        forward_sum = layer[-1] - layer[0]
        take_reversed = forward_sum < 0

        # CLAUSE: generate_difference_layer
        built = []
        if take_reversed:
            for i in range(width - 1, 0, -1):
                built.append(layer[i - 1] - layer[i])
        else:
            for i in range(width - 1):
                built.append(layer[i + 1] - layer[i])
        layer = built

        # CLAUSE: track_best_sequence_sum
        s = sum(layer)
        result = result if result >= s else s

        # CLAUSE: iterate_until_singleton
        if len(layer) == 1:
            break

    # CLAUSE: handle_signed_extremes
    return result

nums = list(map(int, sys.stdin.buffer.read().split()))
q = nums[0]
k = 1
lines = []
for _ in range(q):
    m = nums[k]
    k += 1
    lines.append(str(maximum_sum(nums[k:k + m])))
    k += m
sys.stdout.write("\n".join(lines))
