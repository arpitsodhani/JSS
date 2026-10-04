# CLAUSE: setup_environment
import sys

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    p = 0
    n = data[p]
    m = data[p + 1]
    p += 2

    red = []
    for _ in range(n):
        red.append((data[p], data[p + 1]))
        p += 2

    blue = []
    for _ in range(m):
        blue.append((data[p], data[p + 1]))
        p += 2

    if m == 0:
        print(n * (n - 1) * (n - 2) // 6)
        return

    full = (1 << m) - 1
    left = [[0] * n for _ in range(n)]

    for i in range(n):
        a = red[i]
        for j in range(i + 1, n):
            b = red[j]
            mask = 0
            for t, point in enumerate(blue):
                if cross(a, b, point) > 0:
                    mask |= 1 << t
            left[i][j] = mask
            left[j][i] = full ^ mask

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if cross(red[i], red[j], red[k]) > 0:
                    inside = left[i][j] & left[j][k] & left[k][i]
                else:
                    inside = left[j][i] & left[k][j] & left[i][k]
                if inside == 0:
                    ans += 1
    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
