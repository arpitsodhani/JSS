import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3], data[4]

# Clause count_bijous [Confidence: 1.00]
def count_bijous(vp, vd, t, f, c):
    if vd <= vp:
        return 0
    place = vp * t
    used = 0
    while True:
        meet = place * vd / float(vd - vp)
        if meet >= c:
            return used
        used += 1
        place = meet + vp * (meet / float(vd) + f)

# Clause main [Confidence: 1.00]
def main():
    vp, vd, t, f, c = read_input()
    sys.stdout.write("%d\n" % count_bijous(vp, vd, t, f, c))


if __name__ == "__main__":
    main()

