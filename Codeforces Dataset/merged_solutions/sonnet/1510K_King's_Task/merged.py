import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + 2 * n]

# Clause apply_op [Confidence: 1.00]
def apply_op(n, perm, kind):
    result = list(perm)
    if kind == 0:
        for i in range(n):
            result[2 * i], result[2 * i + 1] = perm[2 * i + 1], perm[2 * i]
    else:
        for i in range(n):
            result[i] = perm[n + i]
            result[n + i] = perm[i]
    return result

# Clause min_operations [Confidence: 0.80]
def min_operations(n, perm):
    target = list(range(1, 2 * n + 1))
    limit = 4 * n + 5
    best = -1
    for first in (0, 1):
        current = list(perm)
        kind = first
        steps = 0
        while steps <= limit:
            if current == target:
                if best < 0 or steps < best:
                    best = steps
                break
            current = apply_op(n, current, kind)
            kind = 1 - kind
            steps += 1
    return best

# Clause main [Confidence: 1.00]
def main():
    n, perm = read_input()
    sys.stdout.write(str(min_operations(n, perm)) + "\n")


if __name__ == "__main__":
    main()

