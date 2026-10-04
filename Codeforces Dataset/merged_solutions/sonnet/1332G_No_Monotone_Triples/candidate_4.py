# CLAUSE: setup_environment
import sys

def bit_update(tree, index, size):
    while index <= size:
        tree[index] += 1
        index += index & -index

def bit_query(tree, index):
    value = 0
    while index > 0:
        value += tree[index]
        index -= index & -index
    return value

def bit_select(tree, target):
    idx = 0
    step = 1 << (len(tree).bit_length() - 1)
    while step:
        nxt = idx + step
        if nxt < len(tree) and tree[nxt] < target:
            idx = nxt
            target -= tree[nxt]
        step >>= 1
    return idx + 1

def first_ready(tree, start, sentinel):
    target = bit_query(tree, start - 1) + 1
    if bit_query(tree, sentinel) < target:
        return sentinel
    return bit_select(tree, target)

def count_smaller_on_stack(stack, top, a, x):
    lo = 1
    hi = top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[stack[mid]] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

def count_larger_on_stack(stack, top, a, x):
    lo = 1
    hi = top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[stack[mid]] > x:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

def first_stack_position(stack, top, r):
    lo = 1
    hi = top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if stack[mid] > r:
            lo = mid + 1
        else:
            hi = mid
    return lo

# CLAUSE: solve_logic
def solve_all(a, queries):
    n = len(a) - 1
    end3 = [n + 1 for _ in range(n + 2)]
    end4 = [n + 1 for _ in range(n + 2)]
    have3 = [[0, 0, 0] for _ in range(n + 2)]
    have4 = [[0, 0, 0, 0] for _ in range(n + 2)]
    membership = [0] * (n + 2)
    up = [0] * (n + 2)
    down = [0] * (n + 2)
    top_up = 0
    top_down = 0
    streak_up = 0
    streak_down = 0
    tree = [0] * (n + 3)
    bit_update(tree, n + 1, n + 1)
    i = n
    while i >= 1:
        while top_up and a[up[top_up]] > a[i]:
            old = up[top_up]
            membership[old] -= 1
            if membership[old] == 0:
                bit_update(tree, old, n + 1)
            top_up -= 1
            streak_up = 0
        while top_down and a[down[top_down]] < a[i]:
            old = down[top_down]
            membership[old] -= 1
            if membership[old] == 0:
                bit_update(tree, old, n + 1)
            top_down -= 1
            streak_down = 0
        less = count_smaller_on_stack(up, top_up, a, a[i])
        greater = count_larger_on_stack(down, top_down, a, a[i])
        end3[i] = i + max(streak_up, streak_down) + 1
        have3[i][0] = i
        have3[i][1] = end3[i] - 1
        have3[i][2] = end3[i]
        if less and greater:
            boundary = up[less]
            if down[greater] > boundary:
                boundary = down[greater]
            end4[i] = first_ready(tree, boundary, n + 1)
            if end4[i] <= n:
                pos_up = first_stack_position(up, top_up, end4[i])
                pos_down = first_stack_position(down, top_down, end4[i])
                left = up[pos_up]
                right = down[pos_down]
                if left > right:
                    left, right = right, left
                have4[i] = [i, left, right, end4[i]]
        top_up += 1
        up[top_up] = i
        top_down += 1
        down[top_down] = i
        streak_up += 1
        streak_down += 1
        membership[i] += 2
        if i < n:
            if end3[i + 1] < end3[i]:
                end3[i] = end3[i + 1]
                have3[i] = have3[i + 1][:]
            if end4[i + 1] < end4[i]:
                end4[i] = end4[i + 1]
                have4[i] = have4[i + 1][:]
        i -= 1
    out = []
    for l, r in queries:
        if r >= end4[l]:
            out.append("4")
            out.append(" ".join(str(x) for x in have4[l]))
        elif r >= end3[l]:
            out.append("3")
            out.append(" ".join(str(x) for x in have3[l]))
        else:
            out.append("0")
    return out

# CLAUSE: finish_program
tokens = list(map(int, sys.stdin.buffer.read().split()))
n = tokens[0]
q = tokens[1]
a = [0] + tokens[2:2 + n]
query_tokens = tokens[2 + n:]
queries = [(query_tokens[i], query_tokens[i + 1]) for i in range(0, 2 * q, 2)]
sys.stdout.write("\n".join(solve_all(a, queries)))
