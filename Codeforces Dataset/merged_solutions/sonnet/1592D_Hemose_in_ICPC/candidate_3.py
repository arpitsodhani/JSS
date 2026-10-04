# CLAUSE: setup_environment
import sys

def ask(group):
    sys.stdout.write("? " + str(len(group)) + " " + " ".join(map(str, group)) + "\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
def narrow_left(options, other, target):
    current = options[:]
    while len(current) > 1:
        half = len(current) // 2
        first = current[:half]
        if ask(first + other) == target:
            current = first
        else:
            current = current[half:]
    return current[0]

def narrow_right(anchor, options, target):
    current = options[:]
    while len(current) > 1:
        half = len(current) // 2
        first = current[:half]
        if ask([anchor] + first) == target:
            current = first
        else:
            current = current[half:]
    return current[0]

def find_pair(group, target):
    current = group[:]
    while len(current) > 2:
        half = len(current) // 2
        first = current[:half]
        second = current[half:]

        first_value = ask(first)
        if first_value == target:
            current = first
            continue

        second_value = ask(second)
        if second_value == target:
            current = second
            continue

        one = narrow_left(first, second, target)
        two = narrow_right(one, second, target)
        return [one, two]
    return current

n = int(sys.stdin.readline())
for _ in range(n - 1):
    sys.stdin.readline()

all_nodes = [i for i in range(1, n + 1)]
best = ask(all_nodes)
result = find_pair(all_nodes, best)

# CLAUSE: finish_program
sys.stdout.write("! " + str(result[0]) + " " + str(result[1]) + "\n")
sys.stdout.flush()
