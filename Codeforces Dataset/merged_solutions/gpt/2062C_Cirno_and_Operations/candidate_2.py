# CLAUSE: derive_sum_transform
import sys

def answer(values):
    current = list(values)
    ans = sum(current)

    # CLAUSE: evaluate_orientation_choice
    length = len(current)
    while length > 1:
        if current[0] > current[-1]:
            current = current[::-1]

        # CLAUSE: generate_difference_layer
        diff = [current[i + 1] - current[i] for i in range(length - 1)]

        # CLAUSE: track_best_sequence_sum
        total = 0
        for x in diff:
            total += x
        ans = max(ans, total)

        # CLAUSE: iterate_until_singleton
        current = diff
        length -= 1

    # CLAUSE: handle_signed_extremes
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
