# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def can_meet(a, b, c, d):
    return max(a, c) <= min(b, d) + 1

def calc(a):
    n = len(a)
    i = 0
    while i + 1 < n:
        if abs(a[i] - a[i + 1]) <= 1:
            return 0
        i += 1
    best = None
    for start in range(n):
        small = a[start]
        large = a[start]
        for end in range(start, n):
            value = a[end]
            if value < small:
                small = value
            if value > large:
                large = value
            ops = end - start
            good = False
            if start:
                left = a[start - 1]
                good = can_meet(small, large, left, left)
            if not good and end + 1 < n:
                right = a[end + 1]
                good = can_meet(small, large, right, right)
            if good and (best is None or ops < best):
                best = ops
                if best == 1:
                    return 1
    if best is None:
        return -1
    return best

def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    k = 1
    lines = []
    for _ in range(items[0]):
        n = items[k]
        k += 1
        lines.append(str(calc(items[k:k + n])))
        k += n
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
