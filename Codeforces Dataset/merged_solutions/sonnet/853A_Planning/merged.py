# Clause setup_environment [Confidence: 0.40]
import sys
from heapq import heapify, heappush, heappop

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n, k = nums[0], nums[1]
    costs = nums[2:2 + n]


# Clause solve_logic [Confidence: 0.60]
    first_count = min(n, k + 1)
    candidates = [(-costs[i], i + 1) for i in range(first_count)]
    heapify(candidates)

    result = [0] * n
    total = 0
    add_at = first_count + 1

    for when in range(k + 1, k + n + 1):
        while add_at <= n and add_at <= when:
            heappush(candidates, (-costs[add_at - 1], add_at))
            add_at += 1

        value, flight = heappop(candidates)
        result[flight - 1] = when
        total += (-value) * (when - flight)


# Clause finish_program [Confidence: 0.60]
    lines = [str(total)]
    lines.append(" ".join(map(str, result)))
    print("\n".join(lines))

if __name__ == "__main__":
    main()


