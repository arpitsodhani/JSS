# CLAUSE: setup_environment
import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

def merge_diameter(x, y, z):
    if x > y:
        a, b = x, y
    else:
        a, b = y, x
    if z > a:
        return z + a
    if z > b:
        return a + z
    return a + b

# CLAUSE: solve_logic
def solve_case(n, p):
    left_child = [0] * (n + 1)
    right_child = [0] * (n + 1)
    parent = [0] * (n + 1)
    stack = []

    for i in range(1, n + 1):
        last = 0
        while stack and p[stack[-1] - 1] < p[i - 1]:
            last = stack.pop()
        if stack:
            right_child[stack[-1]] = i
            parent[i] = stack[-1]
        if last:
            left_child[i] = last
            parent[last] = i
        stack.append(i)

    root = p.index(n) + 1

    def prune(states):
        states = list(set(states))
        alive = []
        for i, s in enumerate(states):
            bad = False
            for j, o in enumerate(states):
                if i != j and o[0] >= s[0] and o[1] >= s[1] and o[2] >= s[2] and o[3] >= s[3]:
                    bad = True
                    break
            if not bad:
                alive.append(s)
        return tuple(alive)

    @lru_cache(None)
    def calc(node, can_left, can_right):
        if node == 0:
            return ((0, 0, 0, 0),)
        left_states = calc(left_child[node], can_left, 1)
        right_states = calc(right_child[node], 1, can_right)
        states = []
        for ls in left_states:
            lh, ld, mid_h_l, mid_d_l = ls
            for rs in right_states:
                mid_h_r, mid_d_r, rh, rd = rs
                if can_left:
                    height = max(lh, 1 + mid_h_l, 1 + mid_h_r)
                    dia = max(ld, mid_d_l, mid_d_r, merge_diameter(1 + lh, mid_h_l, mid_h_r))
                    states.append((height, dia, rh, rd))
                if can_right:
                    height = max(rh, 1 + mid_h_l, 1 + mid_h_r)
                    dia = max(rd, mid_d_l, mid_d_r, merge_diameter(mid_h_l, mid_h_r, 1 + rh))
                    states.append((lh, ld, height, dia))
        return prune(states)

    left_states = calc(left_child[root], 0, 1)
    right_states = calc(right_child[root], 1, 0)
    ans = 0
    for l in left_states:
        for r in right_states:
            v = l[2] + r[0]
            if l[3] > v:
                v = l[3]
            if r[1] > v:
                v = r[1]
            if v > ans:
                ans = v
    return ans

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        idx += 1
        out.append(str(solve_case(n, p)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
