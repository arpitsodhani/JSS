# CLAUSE: setup_environment
import sys

def prepare(lines):
    lines.sort()
    cleaned = []
    for m, b in lines:
        if cleaned and cleaned[-1][0] == m:
            if cleaned[-1][1] < b:
                cleaned[-1] = (m, b)
        else:
            cleaned.append((m, b))
    hull = []
    for m, b in cleaned:
        item = (m, b)
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            if (y2 - y1) * (x2 - m) >= (b - y2) * (x1 - x2):
                hull.pop()
            else:
                break
        hull.append(item)
    return hull

def maximum(hull, q):
    lo = 0
    hi = len(hull) - 1
    while lo != hi:
        mid = (lo + hi) // 2
        a = hull[mid]
        b = hull[mid + 1]
        if a[0] * q + a[1] < b[0] * q + b[1]:
            lo = mid + 1
        else:
            hi = mid
    return hull[lo][0] * q + hull[lo][1]

def add_interval(tree, base, left, right, line):
    left = left + base - 1
    right = right + base - 1
    while left <= right:
        if left & 1:
            tree[left].append(line)
            left += 1
        if not right & 1:
            tree[right].append(line)
            right -= 1
        left >>= 1
        right >>= 1

# CLAUSE: solve_logic
def main():
    arr = sys.stdin.buffer.read().split()
    if not arr:
        return
    n = int(arr[0])
    ptr = 1
    live = {}
    intervals = []
    q_at = {}
    query_order = []
    for number in range(1, n + 1):
        typ = int(arr[ptr])
        ptr += 1
        if typ == 1:
            live[number] = (int(arr[ptr]), int(arr[ptr + 1]))
            ptr += 2
        elif typ == 2:
            rem = int(arr[ptr])
            ptr += 1
            if rem in live:
                intervals.append((rem, number - 1, live[rem]))
                del live[rem]
        else:
            q_at[number] = int(arr[ptr])
            ptr += 1
            query_order.append(number)
    for number, line in live.items():
        intervals.append((number, n, line))
    base = 1 << ((n - 1).bit_length())
    tree = [[] for _ in range(base * 2)]
    for left, right, line in intervals:
        add_interval(tree, base, left, right, line)
    answer = {}
    node_queries = [[] for _ in range(base * 2)]
    for query in query_order:
        node_queries[query + base - 1].append(query)
    for node in range(base - 1, 0, -1):
        left_part = node_queries[node * 2]
        right_part = node_queries[node * 2 + 1]
        if left_part or right_part:
            node_queries[node] = left_part + right_part
    for node in range(1, base * 2):
        if tree[node] and node_queries[node]:
            hull = prepare(tree[node])
            for query in node_queries[node]:
                got = maximum(hull, q_at[query])
                old = answer.get(query)
                if old is None or got > old:
                    answer[query] = got
    result = []
    for query in query_order:
        result.append(str(answer[query]) if query in answer else "EMPTY SET")
# CLAUSE: finish_program
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
