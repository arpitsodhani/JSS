# CLAUSE: setup_environment
import sys

def get_sum(left, right):
    sys.stdout.write("? " + str(left) + " " + str(right) + "\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
segments = [(1, n)]
maximum = 0
index = 0

while index < len(segments):
    left, right = segments[index]
    index += 1
    if left == right:
        current = get_sum(left, right)
        if current > maximum:
            maximum = current
        continue
    middle = (left + right) // 2
    segments.append((left, middle))
    segments.append((middle + 1, right))

# CLAUSE: finish_program
sys.stdout.write("! " + str(maximum) + "\n")
sys.stdout.flush()
