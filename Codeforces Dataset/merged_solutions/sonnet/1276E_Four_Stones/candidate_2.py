# CLAUSE: setup_environment
import sys
from collections import Counter, deque
from math import gcd

# CLAUSE: solve_logic
def pair_gcd(v):
    ans = 0
    for i in range(4):
        for j in range(i + 1, 4):
            ans = gcd(ans, abs(v[i] - v[j]))
    return ans

def packed(v, g):
    return sorted(x % (2 * g) for x in v)

def canon(v, base, g):
    return tuple(sorted((x - base) // g for x in v))

def next_states(state, bound):
    cur = list(state)
    out = []
    for i, x in enumerate(cur):
        for j, y in enumerate(cur):
            if i != j and x != y:
                z = y + y - x
                if -bound <= z <= bound:
                    nxt = cur[:]
                    nxt[i] = z
                    out.append((tuple(sorted(nxt)), (x, y)))
    return out

def restore(mid, left_parent, right_parent):
    left = []
    node = mid
    while left_parent[node] is not None:
        prev, op = left_parent[node]
        left.append(op)
        node = prev
    left.reverse()
    right = []
    node = mid
    while right_parent[node] is not None:
        prev, op = right_parent[node]
        x, y = op
        right.append((y + y - x, y))
        node = prev
    return left + right

def search(start, goal):
    if start == goal:
        return []
    bound = max(80, 2 * max(max(map(abs, start)), max(map(abs, goal)), 10) + 20)
    q1, q2 = deque([start]), deque([goal])
    p1, p2 = {start: None}, {goal: None}
    while q1 and q2 and len(p1) + len(p2) <= 250000:
        if len(q1) <= len(q2):
            for _ in range(len(q1)):
                state = q1.popleft()
                for nxt, op in next_states(state, bound):
                    if nxt in p1:
                        continue
                    p1[nxt] = (state, op)
                    if nxt in p2:
                        return restore(nxt, p1, p2)
                    q1.append(nxt)
        else:
            for _ in range(len(q2)):
                state = q2.popleft()
                for nxt, op in next_states(state, bound):
                    if nxt in p2:
                        continue
                    p2[nxt] = (state, op)
                    if nxt in p1:
                        return restore(nxt, p1, p2)
                    q2.append(nxt)
    return None

def main():
    nums = list(map(int, sys.stdin.read().split()))
    if len(nums) != 8:
        return
    a, b = nums[:4], nums[4:]
    if Counter(a) == Counter(b):
        print(0)
        return
    ga, gb = pair_gcd(a), pair_gcd(b)
    if ga == 0 or gb == 0 or ga != gb:
        print(-1)
        return
    g = ga
    if packed(a, g) != packed(b, g):
        print(-1)
        return
    base = a[0] % g
    if any(x % g != base for x in b):
        print(-1)
        return
    route = search(canon(a, base, g), canon(b, base, g))
    if route is None or len(route) > 1000:
        print(-1)
        return
    lines = [str(len(route))]
    for x, y in route:
        lines.append(f"{base + x * g} {base + y * g}")
    print("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
