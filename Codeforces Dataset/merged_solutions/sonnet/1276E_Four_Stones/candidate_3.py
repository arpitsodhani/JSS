# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

def multiset_equal(x, y):
    return sorted(x) == sorted(y)

def distance_unit(values):
    g = 0
    for i, j in PAIRS:
        g = gcd(g, abs(values[i] - values[j]))
    return g

def residue_key(values, unit):
    mod = unit + unit
    ans = []
    for value in values:
        ans.append(value % mod)
    ans.sort()
    return ans

def reduced(values, origin, unit):
    ans = [(value - origin) // unit for value in values]
    ans.sort()
    return tuple(ans)

def transitions(state, cap):
    source = list(state)
    for i in range(4):
        x = source[i]
        for y in source:
            if x == y:
                continue
            z = 2 * y - x
            if abs(z) <= cap:
                nxt = source[:]
                nxt[i] = z
                nxt.sort()
                yield tuple(nxt), (x, y)

def make_answer(join, parent_start, parent_goal):
    first = []
    cur = join
    while parent_start[cur][0] is not None:
        cur, op = parent_start[cur]
        first.append(op)
    first.reverse()
    second = []
    cur = join
    while parent_goal[cur][0] is not None:
        prev, op = parent_goal[cur]
        x, y = op
        second.append((2 * y - x, y))
        cur = prev
    return first + second

def meet_search(start, target):
    if start == target:
        return []
    lim = max(80, max(abs(v) for v in start + target) * 2 + 20, 40)
    queues = [[start], [target]]
    heads = [0, 0]
    parents = [{start: (None, None)}, {target: (None, None)}]
    while heads[0] < len(queues[0]) and heads[1] < len(queues[1]) and len(parents[0]) + len(parents[1]) <= 250000:
        side = 0 if len(queues[0]) - heads[0] <= len(queues[1]) - heads[1] else 1
        other = 1 - side
        stop = len(queues[side])
        while heads[side] < stop:
            cur = queues[side][heads[side]]
            heads[side] += 1
            for nxt, op in transitions(cur, lim):
                if nxt in parents[side]:
                    continue
                parents[side][nxt] = (cur, op)
                if nxt in parents[other]:
                    if side == 0:
                        return make_answer(nxt, parents[0], parents[1])
                    return make_answer(nxt, parents[0], parents[1])
                queues[side].append(nxt)
    return None

def main():
    data = sys.stdin.buffer.read().split()
    if len(data) != 8:
        return
    nums = [int(x) for x in data]
    start_raw = nums[:4]
    target_raw = nums[4:]
    if multiset_equal(start_raw, target_raw):
        sys.stdout.write("0\n")
        return
    g1 = distance_unit(start_raw)
    g2 = distance_unit(target_raw)
    if g1 == 0 or g1 != g2:
        sys.stdout.write("-1\n")
        return
    if residue_key(start_raw, g1) != residue_key(target_raw, g1):
        sys.stdout.write("-1\n")
        return
    root = start_raw[0] % g1
    for value in target_raw:
        if value % g1 != root:
            sys.stdout.write("-1\n")
            return
    path = meet_search(reduced(start_raw, root, g1), reduced(target_raw, root, g1))
    if path is None or len(path) > 1000:
        sys.stdout.write("-1\n")
        return
    out = [str(len(path))]
    out.extend(str(root + x * g1) + " " + str(root + y * g1) for x, y in path)
    sys.stdout.write("\n".join(out) + "\n")

# CLAUSE: finish_program
main()
