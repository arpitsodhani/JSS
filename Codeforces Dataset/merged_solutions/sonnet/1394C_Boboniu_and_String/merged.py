# Clause setup_environment [Confidence: 0.60]
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for s in data[1:1 + n]:
        b = s.count('B')
        points.append((len(s), 2 * b - len(s)))


# Clause solve_logic [Confidence: 0.60]
    def build(r):
        lu = 1
        hu = 10 ** 18
        lv = -10 ** 18
        hv = 10 ** 18
        for u, v in points:
            if u - r > lu:
                lu = u - r
            if u + r < hu:
                hu = u + r
            if v - r > lv:
                lv = v - r
            if v + r < hv:
                hv = v + r
        if lu > hu or lv > hv:
            return None
        for u in (lu, lu + 1):
            if u > hu:
                continue
            v = lv
            if (u - v) & 1:
                v += 1
            if v <= hv:
                b = (u + v) // 2
                c = (u - v) // 2
                if b >= 0 and c >= 0 and b + c > 0:
                    return b, c
        return None

    left = 0
    right = 10 ** 6
    while left < right:
        mid = (left + right) // 2
        if build(mid) is None:
            left = mid + 1
        else:
            right = mid
    b, c = build(left)


# Clause finish_program [Confidence: 0.60]
    sys.stdout.write(str(left) + "\n" + "B" * b + "N" * c + "\n")

if __name__ == "__main__":
    main()


