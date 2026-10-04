# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1

        circles = []
        for _ in range(n):
            x = data[idx]
            y = data[idx + 1]
            idx += 2
            circles.append((x, y))

        xs = data[idx]
        ys = data[idx + 1]
        xt = data[idx + 2]
        yt = data[idx + 3]
        idx += 4

        need = (xs - xt) * (xs - xt) + (ys - yt) * (ys - yt)

        ok = True
        for x, y in circles:
            d = (x - xt) * (x - xt) + (y - yt) * (y - yt)
            if d <= need:
                ok = False
                break

        ans.append("YES" if ok else "NO")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
