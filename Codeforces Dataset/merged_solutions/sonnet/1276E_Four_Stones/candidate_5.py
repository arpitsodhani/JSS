# CLAUSE: setup_environment
import sys
from collections import deque
from functools import reduce
from math import gcd

# CLAUSE: solve_logic
def same_bag(a, b):
    return tuple(sorted(a)) == tuple(sorted(b))

def all_diffs(values):
    for i in range(4):
        for j in range(i + 1, 4):
            yield abs(values[i] - values[j])

def gcd_all(values):
    return reduce(gcd, all_diffs(values), 0)

def normalize_values(values, residue, step):
    normalized = []
    for value in values:
        normalized.append((value - residue) // step)
    normalized.sort()
    return tuple(normalized)

def residue_list(values, step):
    modulo = step * 2
    result = [value % modulo for value in values]
    result.sort()
    return result

def expand(state, limit):
    arr = list(state)
    result = []
    seen = set()
    for i in range(4):
        x = arr[i]
        for j in range(4):
            if i == j:
                continue
            y = arr[j]
            if x == y:
                continue
            z = 2 * y - x
            if z < -limit or z > limit:
                continue
            nxt = arr[:i] + [z] + arr[i + 1:]
            nxt.sort()
            key = tuple(nxt)
            if key in seen:
                continue
            seen.add(key)
            result.append((key, (x, y)))
    return result

def join_path(touch, parents):
    path = []
    cur = touch
    while parents[0][cur] is not None:
        prev, op = parents[0][cur]
        path.append(op)
        cur = prev
    path.reverse()
    cur = touch
    while parents[1][cur] is not None:
        prev, op = parents[1][cur]
        x, y = op
        path.append((2 * y - x, y))
        cur = prev
    return path

def solve_path(start, target):
    if start == target:
        return []
    limit = max(80, max([10] + [abs(x) for x in start] + [abs(x) for x in target]) * 2 + 20)
    queues = [deque([start]), deque([target])]
    parents = [{start: None}, {target: None}]
    while queues[0] and queues[1]:
        if len(parents[0]) + len(parents[1]) > 250000:
            break
        side = 0
        if len(queues[1]) < len(queues[0]):
            side = 1
        other = 1 - side
        layer_count = len(queues[side])
        for _ in range(layer_count):
            cur = queues[side].popleft()
            for nxt, op in expand(cur, limit):
                if nxt in parents[side]:
                    continue
                parents[side][nxt] = (cur, op)
                if nxt in parents[other]:
                    return join_path(nxt, parents)
                queues[side].append(nxt)
    return None

def main():
    raw = sys.stdin.buffer.read().split()
    if len(raw) != 8:
        return
    nums = list(map(int, raw))
    a = nums[:4]
    b = nums[4:]
    if same_bag(a, b):
        print(0)
        return
    ga = gcd_all(a)
    gb = gcd_all(b)
    if ga == 0 or gb == 0 or ga != gb:
        print(-1)
        return
    if residue_list(a, ga) != residue_list(b, ga):
        print(-1)
        return
    base = a[0] % ga
    ok = True
    for item in b:
        ok = ok and item % ga == base
    if not ok:
        print(-1)
        return
    start = normalize_values(a, base, ga)
    target = normalize_values(b, base, ga)
    answer = solve_path(start, target)
    if answer is None or len(answer) > 1000:
        print(-1)
        return
    output = [str(len(answer))]
    for x, y in answer:
        output.append("{} {}".format(base + x * ga, base + y * ga))
    print("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
