# CLAUSE: setup_environment
import sys
from collections import Counter, defaultdict

# CLAUSE: solve_logic
def solve_one(a):
    counts = Counter(a)
    first_rank = {}
    offset = 0
    for value in sorted(counts):
        first_rank[value] = offset
        offset += counts[value]

    seen = defaultdict(int)
    original_index = [0] * len(a)
    for index, value in enumerate(a):
        rank = first_rank[value] + seen[value]
        seen[value] += 1
        original_index[rank] = index

    longest = 1 if a else 0
    length = 1 if a else 0
    for i in range(1, len(original_index)):
        if original_index[i - 1] < original_index[i]:
            length += 1
        else:
            length = 1
        longest = max(longest, length)
    return len(a) - longest

def main():
    data = sys.stdin.buffer.read().split()
    at = 1
    results = []
    for _ in range(int(data[0])):
        n = int(data[at])
        at += 1
        a = [int(x) for x in data[at:at + n]]
        at += n
        results.append(str(solve_one(a)))
    sys.stdout.write("\n".join(results))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
