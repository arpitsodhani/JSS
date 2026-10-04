# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def read_points():
    values = sys.stdin.buffer.read().split()
    if not values:
        return []
    count = int(values[0])
    return [(int(values[i]), int(values[i + 1])) for i in range(1, 2 * count, 2)]

def valid(points):
    n = len(points)
    if n % 2 == 1:
        return False

    half = n // 2
    sums = set()
    for left, right in zip(points[:half], points[half:]):
        sums.add((left[0] + right[0], left[1] + right[1]))
        if len(sums) > 1:
            return False
    return True

def main():
    points = read_points()
    if not points:
        return
    sys.stdout.write("YES\n" if valid(points) else "NO\n")

# CLAUSE: finish_program
main()
