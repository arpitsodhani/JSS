import sys

def solve(a, b, c):
    positions = sorted([a, b, c])
    diff = positions[2] - positions[0]
    if diff <= 2:
        return 0
    else:
        return 2 * (diff - 2)

input_data = sys.stdin.read().strip().split()
idx = 0
q = int(input_data[idx])
idx += 1

for _ in range(q):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    c = int(input_data[idx + 2])
    idx += 3
    print(solve(a, b, c))
