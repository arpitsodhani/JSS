# CLAUSE: setup_environment
import sys

def compatible(x1, x2, y1, y2):
    if x1 > y2 + 1:
        return False
    if y1 > x2 + 1:
        return False
    return True

# CLAUSE: solve_logic
def minimum_operations(values):
    n = len(values)
    for i, x in enumerate(values[:-1]):
        if abs(x - values[i + 1]) <= 1:
            return 0
    limit = n
    ans = limit
    for split in range(1, n):
        left_ranges = []
        mn = mx = values[split - 1]
        j = split - 1
        while j >= 0:
            y = values[j]
            mn = min(mn, y)
            mx = max(mx, y)
            left_ranges.append((j, mn, mx))
            j -= 1
        rmn = rmx = values[split]
        for r in range(split, n):
            y = values[r]
            rmn = min(rmn, y)
            rmx = max(rmx, y)
            for l, lmn, lmx in left_ranges:
                if compatible(lmn, lmx, rmn, rmx):
                    cost = r - l - 1
                    if cost < ans:
                        ans = cost
                    break
    return -1 if ans == limit else ans

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    index = 1
    res = []
    for _ in range(t):
        n = raw[index]
        index += 1
        res.append(str(minimum_operations(raw[index:index + n])))
        index += n
    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
