# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def opposite_pairs_share_center(points):
    n = len(points)
    if n & 1:
        return False
    half = n >> 1
    center_sum = (points[0][0] + points[half][0], points[0][1] + points[half][1])
    return all(
        points[i][0] + points[i + half][0] == center_sum[0]
        and points[i][1] + points[i + half][1] == center_sum[1]
        for i in range(1, half)
    )

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return
    n = tokens[0]
    coords = tokens[1:]
    points = list(zip(coords[0::2], coords[1::2]))
    print("YES" if opposite_pairs_share_center(points) else "NO")

# CLAUSE: finish_program
main()
