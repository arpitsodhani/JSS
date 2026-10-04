# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    pts = []
    pos = 1
    for _ in range(n):
        pts.append((int(data[pos]), int(data[pos + 1])))
        pos += 2

    if n % 2:
        sys.stdout.write("NO")
        return

    half = n // 2
    target_x = pts[0][0] + pts[half][0]
    target_y = pts[0][1] + pts[half][1]

    for i in range(half):
        if pts[i][0] + pts[i + half][0] != target_x or pts[i][1] + pts[i + half][1] != target_y:
            sys.stdout.write("NO")
            return

    sys.stdout.write("YES")

# CLAUSE: finish_program
main()
