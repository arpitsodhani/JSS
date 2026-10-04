# CLAUSE: setup_environment
import sys

class Hull:
    def __init__(self, lines):
        lines.sort(key=lambda z: (z[0], z[1]))
        filtered = []
        last_m = None
        best_b = None
        for m, b in lines:
            if last_m is None or m != last_m:
                if last_m is not None:
                    filtered.append((last_m, best_b))
                last_m = m
                best_b = b
            elif b > best_b:
                best_b = b
        if last_m is not None:
            filtered.append((last_m, best_b))
        self.lines = []
        for line in filtered:
            while len(self.lines) > 1:
                p = self.lines[-2]
                q = self.lines[-1]
                if (q[1] - p[1]) * (q[0] - line[0]) >= (line[1] - q[1]) * (p[0] - q[0]):
                    self.lines.pop()
                else:
                    break
            self.lines.append(line)

    def query(self, x):
        arr = self.lines
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            one = arr[mid][0] * x + arr[mid][1]
            two = arr[mid + 1][0] * x + arr[mid + 1][1]
            if one <= two:
                left = mid + 1
            else:
                right = mid
        return arr[left][0] * x + arr[left][1]

# CLAUSE: solve_logic
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
# CLAUSE: finish_program
    print("\n".join(res))

if __name__ == "__main__":
    main()
