# CLAUSE: setup_environment
import sys

def shared_value(x, y):
    a, b = x
    c, d = y
    found = []
    if a == c or a == d:
        found.append(a)
    if b == c or b == d:
        found.append(b)
    if len(found) == 1:
        return found[0]
    return None

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
