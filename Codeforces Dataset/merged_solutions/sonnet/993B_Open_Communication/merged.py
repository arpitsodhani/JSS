# Clause setup_environment [Confidence: 0.40]
import sys

def common_number(a, b, c, d):
    result = 0
    count = 0
    if a == c or a == d:
        result = a
        count += 1
    if b == c or b == d:
        result = b
        count += 1
    if count == 1:
        return result
    return 0


# Clause solve_logic [Confidence: 0.40]
def main():
    nums = list(map(int, sys.stdin.read().split()))
    n, m = nums[0], nums[1]
    pos = 2
    left = []
    for i in range(n):
        left.append((nums[pos], nums[pos + 1]))
        pos += 2
    right = []
    for i in range(m):
        right.append((nums[pos], nums[pos + 1]))
        pos += 2

    certain = set()
    for p in left:
        for q in right:
            value = shared_value(p, q)
            if value is not None:
                certain.add(value)

    if len(certain) == 1:
        sys.stdout.write(str(next(iter(certain))))
        return

    for p in left:
        seen = set()
        for q in right:
            value = shared_value(p, q)
            if value is not None:
                seen.add(value)
        if len(seen) > 1:
            sys.stdout.write("-1")
            return

    for q in right:
        seen = set()
        for p in left:
            value = shared_value(p, q)
            if value is not None:
                seen.add(value)
        if len(seen) > 1:
            sys.stdout.write("-1")
            return

    sys.stdout.write("0")


# Clause finish_program [Confidence: 0.40]
main()


