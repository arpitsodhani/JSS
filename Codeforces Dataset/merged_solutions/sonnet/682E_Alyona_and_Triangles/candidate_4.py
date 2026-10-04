# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    points = []
    t = 1
    for _ in range(n):
        x = int(data[t])
        y = int(data[t + 1])
        points.append((x, y))
        t += 2

    hull = monotone_chain(points)
    m = len(hull)

    if m == 1:
        answer = [hull[0], hull[0], hull[0]]
    elif m == 2:
        answer = [hull[0], hull[1], hull[0]]
    else:
        bi = 0
        bj = 1
        bk = 2
        best = -1
        for i in range(m):
            k = i + 2
            if k >= m:
                k -= m
            for j in range(i + 1, m):
                if k == j:
                    k += 1
                    if k == m:
                        k = 0
                current = tri_area2(hull, i, j, k)
                while True:
                    nxt = k + 1
                    if nxt == m:
                        nxt = 0
                    if nxt == i:
                        break
                    trial = tri_area2(hull, i, j, nxt)
                    if trial <= current:
                        break
                    k = nxt
                    current = trial
                if current > best:
                    best = current
                    bi = i
                    bj = j
                    bk = k
        a = hull[bi]
        b = hull[bj]
        c = hull[bk]
        answer = [
            (a[0] + b[0] - c[0], a[1] + b[1] - c[1]),
            (a[0] + c[0] - b[0], a[1] + c[1] - b[1]),
            (b[0] + c[0] - a[0], b[1] + c[1] - a[1]),
        ]

# CLAUSE: finish_program
    print_points(answer)

if __name__ == "__main__":
    main()
