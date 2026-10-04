# CLAUSE: setup_environment
import sys
from array import array

def prepare_sparse(block, n):
    tables = []
    for base in block:
        levels = [base]
        jump = 1
        while jump << 1 <= n:
            last = levels[-1]
            m = n - (jump << 1) + 1
            now = array('i', [0]) * m
            for p in range(m):
                a = last[p]
                b = last[p + jump]
                now[p] = a if a >= b else b
            levels.append(now)
            jump <<= 1
        tables.append(levels)
    return tables

def maximum_between(tables, logs, budget, lo, hi):
    if hi < lo:
        return lo
    lg = logs[hi - lo + 1]
    row = tables[budget][lg]
    left = row[lo]
    right = row[hi - (1 << lg) + 1]
    return left if left >= right else right

def lift_once(previous, logs, max_k, n):
    tables = prepare_sparse(previous, n)
    result = []
    for budget in range(max_k + 1):
        current = array('i', [0]) * n
        for start in range(n):
            best = start
            remaining = budget
            while remaining >= 0:
                middle = previous[remaining][start]
                candidate = maximum_between(tables, logs, budget - remaining, start, middle)
                if candidate > best:
                    best = candidate
                remaining -= 1
            current[start] = best
        result.append(current)
    return result

# CLAUSE: solve_logic
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return

    n = tokens[0]
    q = tokens[1]
    a = tokens[2:2 + n]
    offset = 2 + n

    queries = []
    max_k = 0
    for idx in range(q):
        left = tokens[offset] - 1
        right = tokens[offset + 1] - 1
        k = tokens[offset + 2]
        offset += 3
        queries.append((left, right, k, idx))
        max_k = k if k > max_k else max_k

    logs = [0] * (n + 1)
    length = 2
    while length <= n:
        logs[length] = logs[length >> 1] + 1
        length += 1

    count = (n + 1).bit_length() + 1
    dp = []

    base = []
    for removed in range(max_k + 1):
        row = array('i', [0]) * n
        for i, value in enumerate(a):
            if value:
                dest = i + value + removed
                row[i] = n - 1 if dest >= n else dest
            else:
                row[i] = i
        base.append(row)
    dp.append(base)

    for _ in range(1, count):
        dp.append(lift_once(dp[-1], logs, max_k, n))

    answers = [0] * q
    pending = []
    for left, right, k, original in queries:
        if left == right:
            answers[original] = 0
        else:
            pending.append({"far": [left] * (k + 1), "hops": 0, "l": left, "r": right, "k": k, "id": original})

    active = list(range(len(pending)))
    for bit in reversed(range(count)):
        if len(active) == 0:
            break
        tables = prepare_sparse(dp[bit], n)
        for state_index in active:
            state = pending[state_index]
            l = state["l"]
            k = state["k"]
            far = state["far"]
            new_far = [l] * (k + 1)
            for budget in range(k + 1):
                best = l
                for used in range(budget, -1, -1):
                    right_edge = far[used]
                    if right_edge >= n:
                        right_edge = n - 1
                    reach = maximum_between(tables, logs, budget - used, l, right_edge)
                    if reach > best:
                        best = reach
                new_far[budget] = best
            if new_far[k] < state["r"]:
                state["far"] = new_far
                state["hops"] += 1 << bit

    for state in pending:
        idx = state["id"]
        answers[idx] = -1 if state["far"][state["k"]] < state["r"] else state["hops"] + 1

    sys.stdout.write("\n".join(str(answer) for answer in answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
