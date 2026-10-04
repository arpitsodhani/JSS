# CLAUSE: setup_environment
import sys

def query(values):
    print("?", len(values), *values, flush=True)
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
def choose_crossing(left_part, right_part, target):
    low = 0
    high = len(left_part)
    while high - low > 1:
        mid = (low + high) // 2
        if query(left_part[low:mid] + right_part) == target:
            high = mid
        else:
            low = mid
    left_node = left_part[low]

    low = 0
    high = len(right_part)
    while high - low > 1:
        mid = (low + high) // 2
        if query([left_node] + right_part[low:mid]) == target:
            high = mid
        else:
            low = mid
    return [left_node, right_part[low]]

def locate(group, target):
    size = len(group)
    if size == 2:
        return group

    split = size // 2
    a = group[:split]
    b = group[split:]

    value_a = query(a)
    if value_a == target:
        return locate(a, target)

    value_b = query(b)
    if value_b == target:
        return locate(b, target)

    return choose_crossing(a, b, target)

n = int(sys.stdin.readline())
for _ in range(n - 1):
    sys.stdin.readline()

initial = list(range(1, n + 1))
target = query(initial)
answer = locate(initial, target)

# CLAUSE: finish_program
print("!", answer[0], answer[1], flush=True)
