# CLAUSE: setup_environment
import sys

def read_points():
    data = sys.stdin.buffer.read().split()
    res = []
    for word in data[1:]:
        blue = 0
        for ch in word:
            if ch == 66:
                blue += 1
        size = len(word)
        res.append((size, blue * 2 - size))
    return res

def main():
    points = read_points()

# CLAUSE: solve_logic
    def limits(distance):
        lo_size, hi_size = 1, 10 ** 18
        lo_diff, hi_diff = -10 ** 18, 10 ** 18
        for size, diff in points:
            lo_size = max(lo_size, size - distance)
            hi_size = min(hi_size, size + distance)
            lo_diff = max(lo_diff, diff - distance)
            hi_diff = min(hi_diff, diff + distance)
        return lo_size, hi_size, lo_diff, hi_diff

    def choose(distance):
        lo_size, hi_size, lo_diff, hi_diff = limits(distance)
        if lo_size > hi_size or lo_diff > hi_diff:
            return None
        size = lo_size
        for diff in (lo_diff, lo_diff + 1):
            if diff <= hi_diff and ((size + diff) & 1) == 0:
                blue = (size + diff) // 2
                other = (size - diff) // 2
                if blue >= 0 and other >= 0 and size:
                    return blue, other
        size += 1
        if size <= hi_size:
            diff = lo_diff + ((size - lo_diff) & 1)
            if diff <= hi_diff:
                blue = (size + diff) // 2
                other = (size - diff) // 2
                if blue >= 0 and other >= 0:
                    return blue, other
        return None

    ok_distance = 10 ** 6
    bad_distance = -1
    while ok_distance - bad_distance > 1:
        test = (ok_distance + bad_distance) // 2
        if choose(test) is None:
            bad_distance = test
        else:
            ok_distance = test
    blue, other = choose(ok_distance)

# CLAUSE: finish_program
    out = [str(ok_distance), "B" * blue + "N" * other]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
