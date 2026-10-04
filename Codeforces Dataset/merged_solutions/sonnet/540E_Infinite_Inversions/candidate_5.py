# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    iterator = iter(tokens)
    n = int(next(iterator))
    value_at = {}
    used = set()

# CLAUSE: solve_logic
    for _ in range(n):
        a = int(next(iterator))
        b = int(next(iterator))
        first = value_at[a] if a in value_at else a
        second = value_at[b] if b in value_at else b
        value_at[a] = second
        value_at[b] = first
        used.add(a)
        used.add(b)

    coords = sorted(used)
    index = {x: i for i, x in enumerate(coords)}
    size = 1
    while size < len(coords):
        size <<= 1
    tree = [0] * (2 * size)
    inversions = 0

    for seen, x in enumerate(coords):
        rank = index[value_at.get(x, x)]
        left = rank + size
        count = 0
        while left > 1:
            if left % 2 == 1:
                count += tree[left - 1]
            left //= 2
        inversions += seen - count
        pos = rank + size
        while pos:
            tree[pos] += 1
            pos //= 2

    for x in coords:
        y = value_at.get(x, x)
        if x != y:
            inversions += abs(x - y) - abs(index[x] - index[y])

# CLAUSE: finish_program
    print(inversions)

if __name__ == "__main__":
    main()
