# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def state_class(x, y):
    if not x and not y:
        return -1
    if not x:
        return 0
    if not y:
        return 1

    turns = 0
    while x and y and x != y:
        if y > x:
            x, y = y, x
        take = x // y
        left = x - take * y
        if left:
            turns += take
            x, y = y, left
        else:
            turns += take - 1
            x = y

    return (turns + 2) % 3


def solve():
    nums = [int(v) for v in sys.stdin.buffer.read().split()]
    at = 1
    results = []

    for _ in range(nums[0]):
        n = nums[at]
        at += 1
        first = nums[at:at + n]
        at += n
        second = nums[at:at + n]
        at += n

        seen = set()
        for i in range(n):
            value = state_class(first[i], second[i])
            if value >= 0:
                seen.add(value)
                if len(seen) > 1:
                    break

        results.append("YES" if len(seen) <= 1 else "NO")

    print("\n".join(results))

# CLAUSE: finish_program
solve()
