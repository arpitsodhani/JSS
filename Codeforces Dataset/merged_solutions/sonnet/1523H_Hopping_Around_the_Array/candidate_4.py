# CLAUSE: setup_environment
import sys
from array import array

def build_table(rows, n):
    result = []
    for values in rows:
        current = [values]
        width = 1
        while width * 2 <= n:
            previous = current[-1]
            count = n - width * 2 + 1
            merged = array('i', [0]) * count
            j = 0
            while j < count:
                left = previous[j]
                right = previous[j + width]
                merged[j] = left if left >= right else right
                j += 1
            current.append(merged)
            width *= 2
        result.append(current)
    return result

def query_table(table, logs, cost, left, right):
    if left > right:
        return left
    level = logs[right - left + 1]
    row = table[cost][level]
    x = row[left]
    y = row[right - (1 << level) + 1]
    return x if x >= y else y

def compose_next(prev, logs, max_k, n):
    table = build_table(prev, n)
    nxt = []
    for total in range(max_k + 1):
        row = array('i', [0]) * n
        for start in range(n):
            best = start
            for first in range(total + 1):
                stop = prev[first][start]
                value = query_table(table, logs, total - first, start, stop)
                if value > best:
                    best = value
            row[start] = best
        nxt.append(row)
    return nxt

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    q = data[1]
    values = data[2:2 + n]
    ptr = 2 + n

    queries = [None] * q
    max_k = 0
    for i in range(q):
        l = data[ptr] - 1
        r = data[ptr + 1] - 1
        k = data[ptr + 2]
        ptr += 3
        queries[i] = (l, r, k)
        if k > max_k:
            max_k = k

    logs = [0] * (n + 1)
    for length in range(2, n + 1):
        logs[length] = logs[length // 2] + 1

    depth = (n + 1).bit_length() + 1
    powers = []

    rows = []
    for cost in range(max_k + 1):
        one = array('i', [0]) * n
        for i in range(n):
            if values[i] == 0:
                one[i] = i
            else:
                reach = i + values[i] + cost
                if reach >= n:
                    reach = n - 1
                one[i] = reach
        rows.append(one)
    powers.append(rows)

    while len(powers) < depth:
        powers.append(compose_next(powers[-1], logs, max_k, n))

    answers = [0] * q
    items = []
    for idx, query in enumerate(queries):
        l, r, k = query
        if l == r:
            answers[idx] = 0
        else:
            items.append(([l] * (k + 1), 0, l, r, k, idx))

    live = list(range(len(items)))
    for bit in range(depth - 1, -1, -1):
        if not live:
            break
        table = build_table(powers[bit], n)
        for item_id in live:
            far, hops, l, r, k, idx = items[item_id]
            candidate = [l] * (k + 1)
            for budget in range(k + 1):
                best = l
                for used in range(budget + 1):
                    end = far[used]
                    if end >= n:
                        end = n - 1
                    value = query_table(table, logs, budget - used, l, end)
                    if value > best:
                        best = value
                candidate[budget] = best
            if candidate[k] < r:
                items[item_id] = (candidate, hops + (1 << bit), l, r, k, idx)

    for far, hops, l, r, k, idx in items:
        answers[idx] = -1 if far[k] < r else hops + 1

    sys.stdout.write("\n".join(map(str, answers)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
