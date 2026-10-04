# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def masks_with_bits(k):
    result = []
    stack = [(0, 0, 0)]
    while stack:
        pos, used, mask = stack.pop()
        if used == k:
            result.append(mask)
            continue
        if pos == 14:
            continue
        if 14 - pos < k - used:
            continue
        stack.append((pos + 1, used, mask))
        stack.append((pos + 1, used + 1, mask | (1 << pos)))
    return result

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    k = int(raw[1])
    arr = [int(x) for x in raw[2:2 + n]]

    if k > 14:
        print(0)
        return

    counts = Counter(arr)

    if k == 0:
        print(sum(c * (c - 1) // 2 for c in counts.values()))
        return

    masks = masks_with_bits(k)
    total = 0
    for x, c in counts.items():
        for m in masks:
            total += c * counts.get(x ^ m, 0)

    print(total // 2)

# CLAUSE: finish_program
main()
