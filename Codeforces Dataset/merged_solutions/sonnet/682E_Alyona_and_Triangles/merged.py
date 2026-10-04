# Clause setup_environment [Confidence: 0.80]
import sys

def det(origin, one, two):
    return (one[0] - origin[0]) * (two[1] - origin[1]) - (one[1] - origin[1]) * (two[0] - origin[0])

def monotone_chain(points):
    ordered = sorted(set(points))
    if len(ordered) <= 2:
        return ordered
    bottom = []
    top = []
    for p in ordered:
        while len(bottom) >= 2 and det(bottom[-2], bottom[-1], p) <= 0:
            bottom.pop()
        bottom.append(p)
    for p in ordered:
        while len(top) >= 2 and det(top[-2], top[-1], p) >= 0:
            top.pop()
        top.append(p)
    return bottom + top[-2:0:-1]

def tri_area2(poly, i, j, k):
    value = det(poly[i], poly[j], poly[k])
    if value < 0:
        value = -value
    return value

def print_points(points):
    sys.stdout.write("\n".join(str(x) + " " + str(y) for x, y in points))


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.60]
    sys.stdout.write("\n".join(f"{x} {y}" for x, y in ans))

if __name__ == "__main__":
    main()


