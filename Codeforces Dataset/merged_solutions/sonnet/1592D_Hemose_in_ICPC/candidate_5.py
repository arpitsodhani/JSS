# CLAUSE: setup_environment
import sys

def make_range(left, right):
    return list(range(left, right + 1))

def ask(left, right):
    nodes = make_range(left, right)
    print("?", len(nodes), *nodes)
    sys.stdout.flush()
    return int(sys.stdin.readline())

def ask_nodes(nodes):
    print("?", len(nodes), *nodes)
    sys.stdout.flush()
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
def find_answer(n, target):
    left = 1
    right = n

    while right - left + 1 > 2:
        middle = (left + right) // 2

        if ask(left, middle) == target:
            right = middle
            continue

        if ask(middle + 1, right) == target:
            left = middle + 1
            continue

        a_low = left
        a_high = middle
        other = make_range(middle + 1, right)
        while a_low < a_high:
            cut = (a_low + a_high) // 2
            probe = make_range(a_low, cut) + other
            if ask_nodes(probe) == target:
                a_high = cut
            else:
                a_low = cut + 1

        first = a_low
        b_low = middle + 1
        b_high = right
        while b_low < b_high:
            cut = (b_low + b_high) // 2
            probe = [first] + make_range(b_low, cut)
            if ask_nodes(probe) == target:
                b_high = cut
            else:
                b_low = cut + 1

        return [first, b_low]

    return [left, right]

n = int(sys.stdin.readline())
for _ in range(n - 1):
    sys.stdin.readline()

target = ask(1, n)
ans = find_answer(n, target)

# CLAUSE: finish_program
print("!", ans[0], ans[1])
sys.stdout.flush()
