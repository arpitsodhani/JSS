# CLAUSE: setup_environment
import sys

def f(line, x):
    return line[0] * x + line[1]

def bad(a, b, c):
    return (b[1] - a[1]) * (b[0] - c[0]) >= (c[1] - b[1]) * (a[0] - b[0])

def make(lines):
    lines = sorted(lines)
    compact = []
    for line in lines:
        if compact and compact[-1][0] == line[0]:
            if line[1] > compact[-1][1]:
                compact[-1] = line
        else:
            compact.append(line)
    stack = []
    for line in compact:
        while len(stack) >= 2 and bad(stack[-2], stack[-1], line):
            stack.pop()
        stack.append(line)
    return stack

def get(hull, x):
    low = 0
    high = len(hull)
    while high - low > 1:
        mid = (low + high) // 2
        if f(hull[mid - 1], x) <= f(hull[mid], x):
            low = mid
        else:
            high = mid
    return f(hull[low], x)

# CLAUSE: solve_logic
def main():
    tokens = [int(x) for x in sys.stdin.buffer.read().split()]
    if not tokens:
        return
    n = tokens[0]
    p = 1
    open_lines = {}
    closed = []
    xs = [0] * (n + 1)
    asks = []
    for idx in range(1, n + 1):
        t = tokens[p]
        p += 1
        if t == 1:
            a = tokens[p]
            b = tokens[p + 1]
            p += 2
            open_lines[idx] = (a, b)
        elif t == 2:
            who = tokens[p]
            p += 1
            if who in open_lines:
                closed.append((idx - 1, who, open_lines.pop(who)))
        else:
            xs[idx] = tokens[p]
            p += 1
            asks.append(idx)
    for left, line in open_lines.items():
        closed.append((n, left, line))
    limit = 1
    while limit < n:
        limit <<= 1
    seg = [[] for _ in range(limit << 1)]
    for right, left, line in closed:
        l = left + limit - 1
        r = right + limit - 1
        while l <= r:
            if l & 1:
                seg[l].append(line)
                l += 1
            if r & 1 == 0:
                seg[r].append(line)
                r -= 1
            l >>= 1
            r >>= 1
    ans = [None] * (n + 1)
    grouped = [[] for _ in range(limit << 1)]
    for qid in asks:
        node = qid + limit - 1
        while node:
            grouped[node].append(qid)
            node >>= 1
    for node, lines in enumerate(seg):
        if not lines:
            continue
        hull = make(lines)
        for qid in grouped[node]:
            cur = get(hull, xs[qid])
            if ans[qid] is None or cur > ans[qid]:
                ans[qid] = cur
    out = []
    for qid in asks:
        out.append("EMPTY SET" if ans[qid] is None else str(ans[qid]))
# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
