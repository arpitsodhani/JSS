# CLAUSE: setup_environment
import sys

reader = sys.stdin.readline
writer = sys.stdout.write

def request(left, right):
    writer(f"? {left} {right}\n")
    sys.stdout.flush()
    return int(reader())

# CLAUSE: solve_logic
n = int(reader())
answer = 0
layers = [[(1, n)]]

while layers:
    current_layer = layers.pop()
    next_layer = []
    for left, right in current_layer:
        if left == right:
            result = request(left, right)
            answer = max(answer, result)
        else:
            middle = (left + right) // 2
            next_layer.append((left, middle))
            next_layer.append((middle + 1, right))
    if next_layer:
        layers.append(next_layer)

# CLAUSE: finish_program
writer(f"! {answer}\n")
sys.stdout.flush()
