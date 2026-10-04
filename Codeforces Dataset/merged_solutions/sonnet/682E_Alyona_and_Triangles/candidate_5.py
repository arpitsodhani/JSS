# CLAUSE: setup_environment
import sys

def vector_cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2

def signed_area(a, b, c):
    return vector_cross(b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1])

def make_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    stack = []
    for group in (points, points[::-1]):
        start = len(stack)
        for p in group:
            while len(stack) >= start + 2 and signed_area(stack[-2], stack[-1], p) <= 0:
                stack.pop()
            stack.append(p)
        stack.pop()
    return stack

def dist_area(a, b, c):
    value = signed_area(a, b, c)
    return -value if value < 0 else value

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    n = nums[0]
    pts = list(zip(nums[1:1 + 2 * n:2], nums[2:1 + 2 * n:2]))

    hull = make_hull(pts)
    length = len(hull)

    if length == 1:
        result = [hull[0]] * 3
    elif length == 2:
        result = [hull[0], hull[1], hull[0]]
    else:
        best_area = 0
        best_triplet = [hull[0], hull[1], hull[2]]
        for i, base_left in enumerate(hull):
            far = (i + 2) % length
            for j in range(i + 1, length):
                base_right = hull[j]
                if far == j:
                    far = (far + 1) % length
                while True:
                    move = far + 1
                    if move == length:
                        move = 0
                    if move == i:
                        break
                    old_area = dist_area(base_left, base_right, hull[far])
                    new_area = dist_area(base_left, base_right, hull[move])
                    if new_area <= old_area:
                        break
                    far = move
                value = dist_area(base_left, base_right, hull[far])
                if value > best_area:
                    best_area = value
                    best_triplet = [base_left, base_right, hull[far]]
        p, q, r = best_triplet
        result = []
        for u, v, w in ((p, q, r), (p, r, q), (q, r, p)):
            result.append((u[0] + v[0] - w[0], u[1] + v[1] - w[1]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(["%d %d" % point for point in result]))

if __name__ == "__main__":
    main()
