# CLAUSE: setup_environment
import sys
import bisect

# CLAUSE: solve_logic
tokens = list(map(int, sys.stdin.buffer.read().split()))
it = iter(tokens)
n = next(it)
m = next(it)

rows = {}
bad = set()
ys = []
for _ in range(n):
    x = next(it)
    y = next(it)
    bad.add((x, y))
    if x in rows:
        rows[x].append(y)
    else:
        rows[x] = [y]
    ys.append(y)

asked = []
row_questions = {}
timeline = set(rows)
for pos in range(m):
    x = next(it)
    y = next(it)
    asked.append((x, y))
    timeline.add(x)
    row_questions.setdefault(x, []).append((pos, y))

ys = sorted(set(ys))
tree = [0] * (len(ys) + 1)
seen_columns = set()

def put_column(y):
    if y in seen_columns:
        return
    seen_columns.add(y)
    k = bisect.bisect_left(ys, y) + 1
    while k < len(tree):
        tree[k] += 1
        k += k & -k

def prefix(k):
    total = 0
    while k > 0:
        total += tree[k]
        k -= k & -k
    return total

def taken_between(left, right):
    a = bisect.bisect_left(ys, left)
    b = bisect.bisect_right(ys, right)
    return prefix(b) - prefix(a)

def select_free(base, number):
    low = base
    high = base + number + len(ys) + 7
    while low < high:
        mid = (low + high) >> 1
        if mid - base + 1 - taken_between(base, mid) >= number:
            high = mid
        else:
            low = mid + 1
    return low

for x in rows:
    rows[x].sort()

out = [""] * m
current_free = 0
last_row = -1

for x in sorted(timeline):
    gap = x - last_row - 1
    if gap:
        current_free = select_free(current_free, gap + 1)

    row_shortcuts = rows.get(x)
    if row_shortcuts is None:
        produced = current_free
    elif current_free < row_shortcuts[0]:
        produced = current_free
    else:
        produced = -1

    for idx, y in row_questions.get(x, ()):
        out[idx] = "LOSE" if (x, y) in bad or y == produced else "WIN"

    if produced != -1:
        current_free = select_free(current_free, 2)

    if row_shortcuts is not None:
        for y in row_shortcuts:
            put_column(y)

    current_free = select_free(current_free, 1)
    last_row = x

# CLAUSE: finish_program
sys.stdout.write("\n".join(out))
