# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()

    n = int(data[0])
    pts = []
    for i in range(n):
        x = int(data[1 + 2 * i])
        y = int(data[2 + 2 * i])
        pts.append((x, y))

    if n % 2:
        print("NO")
    else:
        m = n // 2
        sx = pts[0][0] + pts[m][0]
        sy = pts[0][1] + pts[m][1]
        ok = True
        for i in range(1, m):
            if pts[i][0] + pts[i + m][0] != sx or pts[i][1] + pts[i + m][1] != sy:
                ok = False
                break
        print("YES" if ok else "NO")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
