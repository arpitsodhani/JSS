# Clause setup_environment [Confidence: 0.60]
import sys

def value(line, x):
    return line[0] * x + line[1]

def build_hull(lines):
    if not lines:
        return []
    lines.sort()
    unique = []
    for m, b in lines:
        if unique and unique[-1][0] == m:
            if b > unique[-1][1]:
                unique[-1] = (m, b)
        else:
            unique.append((m, b))
    hull = []
    for line in unique:
        while len(hull) >= 2:
            a = hull[-2]
            c = hull[-1]
            if (c[1] - a[1]) * (c[0] - line[0]) >= (line[1] - c[1]) * (a[0] - c[0]):
                hull.pop()
            else:
                break
        hull.append(line)
    return hull

def ask(hull, x):
    lo = 0
    hi = len(hull) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if value(hull[mid], x) <= value(hull[mid + 1], x):
            lo = mid + 1
        else:
            hi = mid
    return value(hull[lo], x)


# Clause solve_logic [Confidence: 0.80]
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    ptr = 1
    added = {}
    requests = {}
    ranges = []
    order = []
    for i in range(1, n + 1):
        kind = int(raw[ptr])
        ptr += 1
        if kind == 1:
            x = int(raw[ptr])
            y = int(raw[ptr + 1])
            ptr += 2
            added[i] = (x, y)
        elif kind == 2:
            old = int(raw[ptr])
            ptr += 1
            line = added.pop(old, None)
            if line is not None:
                ranges.append((old, i - 1, line))
        else:
            q = int(raw[ptr])
            ptr += 1
            requests[i] = q
            order.append(i)
    for start, line in added.items():
        ranges.append((start, n, line))
    base = 1
    while base < n:
        base *= 2
    buckets = [[] for _ in range(base + base)]
    for left, right, line in ranges:
        left += base - 1
        right += base - 1
        while left <= right:
            if left % 2 == 1:
                buckets[left].append(line)
                left += 1
            if right % 2 == 0:
                buckets[right].append(line)
                right -= 1
            left //= 2
            right //= 2
    by_node = [[] for _ in range(base + base)]
    for i in order:
        by_node[base + i - 1] = [i]
    for i in range(base - 1, 0, -1):
        by_node[i] = by_node[i + i] + by_node[i + i + 1]
    ans = {}
    for i, lines in enumerate(buckets):
        if lines and by_node[i]:
            hull = Hull(lines)
            for at in by_node[i]:
                val = hull.query(requests[at])
                if at not in ans or val > ans[at]:
                    ans[at] = val
    res = []
    for i in order:
        res.append(str(ans[i]) if i in ans else "EMPTY SET")


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()


