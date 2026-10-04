# CLAUSE: setup_environment
import sys
from collections import defaultdict, deque

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    numbers = data[1:]
    if len(numbers) != n:
        return

    buckets = [defaultdict(deque), defaultdict(deque), defaultdict(deque)]
    for index, value in enumerate(numbers, 1):
        buckets[value % 3][value].append(index)

    ordered_values = [sorted(bucket) for bucket in buckets]
    cursor = [0, 0, 0]
    answer = []
    limit = 0

    for position in range(n):
        residue = position % 3
        values = ordered_values[residue]
        at = cursor[residue]

        while at < len(values) and not buckets[residue][values[at]]:
            at += 1
        cursor[residue] = at

        if at == len(values) or values[at] > limit:
            sys.stdout.write("Impossible\n")
            return

        chosen = values[at]
        answer.append(buckets[residue][chosen].popleft())
        limit = chosen + 1

    sys.stdout.write("Possible\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
