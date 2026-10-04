# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    pos = 1
    active = {}
    queries = [None] * (n + 1)
    intervals = []
    find_queries = []
    for t in range(1, n + 1):
        typ = data[pos]
        pos += 1
        if typ == 1:
            a = data[pos]
            b = data[pos + 1]
            pos += 2
            active[t] = (a, b)
        elif typ == 2:
            k = data[pos]
            pos += 1
            if k in active:
                intervals.append((active[k], k, t - 1))
                del active[k]
        else:
            q = data[pos]
            pos += 1
            queries[t] = q
            find_queries.append(t)
    for k, line in active.items():
        intervals.append((line, k, n))
    size = 1
    while size < n:
        size <<= 1
    tree = [[] for _ in range(size * 2)]
    for line, left, right in intervals:
        left += size - 1
        right += size - 1
        while left <= right:
            if left & 1:
                tree[left].append(line)
                left += 1
            if not (right & 1):
                tree[right].append(line)
                right -= 1
            left >>= 1
            right >>= 1
    node_queries = [[] for _ in range(size * 2)]
    for t in find_queries:
        node_queries[t + size - 1].append(t)
    for node in range(size - 1, 0, -1):
        if node_queries[node * 2] or node_queries[node * 2 + 1]:
            node_queries[node] = node_queries[node * 2] + node_queries[node * 2 + 1]
    best = [None] * (n + 1)
    for node in range(1, size * 2):
        if tree[node] and node_queries[node]:
            hull = build_hull(tree[node])
            for t in node_queries[node]:
                got = ask(hull, queries[t])
                if best[t] is None or got > best[t]:
                    best[t] = got
    output = []
    for t in find_queries:
        output.append("EMPTY SET" if best[t] is None else str(best[t]))
# CLAUSE: finish_program
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
