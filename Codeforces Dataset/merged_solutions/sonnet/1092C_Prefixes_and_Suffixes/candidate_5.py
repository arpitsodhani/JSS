# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_answer(original, buckets):
    total = sum(len(bucket) for bucket in buckets)
    answer = [""] * total

    for length, bucket in enumerate(buckets):
        if length == 0 or not bucket:
            continue

        wanted = [(original[:length], "P"), (original[-length:], "S")]
        first_index, first_value = bucket[0]
        second_index, second_value = bucket[1]

        if first_value == wanted[0][0] and second_value == wanted[1][0]:
            answer[first_index] = wanted[0][1]
            answer[second_index] = wanted[1][1]
        elif first_value == wanted[1][0] and second_value == wanted[0][0]:
            answer[first_index] = wanted[1][1]
            answer[second_index] = wanted[0][1]
        else:
            return None

    return "".join(answer)

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    pieces = data[1:]
    buckets = [[] for _ in range(n)]

    for order, piece in enumerate(pieces):
        buckets[len(piece)].append((order, piece))

    nearly_full = buckets[n - 1]
    first = nearly_full[0][1]
    second = nearly_full[1][1]

    for original in [first + second[-1], second + first[-1]]:
        answer = build_answer(original, buckets)
        if answer is not None:
            print(answer)
            return

# CLAUSE: finish_program
main()
