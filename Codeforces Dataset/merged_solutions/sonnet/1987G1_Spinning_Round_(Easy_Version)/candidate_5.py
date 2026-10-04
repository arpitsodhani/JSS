# CLAUSE: setup_environment
import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

def top2(a, b, c):
    if b > a:
        a, b = b, a
    if c > a:
        b = a
        a = c
    elif c > b:
        b = c
    return a + b

# CLAUSE: solve_logic
def solve_case(n, p):
    pos_of_value = [0] * (n + 1)
    for i, v in enumerate(p, 1):
        pos_of_value[v] = i

    def filter_states(states):
        pool = list(set(states))
        pool.sort(reverse=True)
        answer = []
        for st in pool:
            dominated = False
            for other in answer:
                if other[0] >= st[0] and other[1] >= st[1] and other[2] >= st[2] and other[3] >= st[3]:
                    dominated = True
                    break
            if not dominated:
                answer.append(st)
        return tuple(answer)

    @lru_cache(None)
    def highest_inside(l, r):
        for value in range(n, 0, -1):
            pos = pos_of_value[value]
            if l <= pos <= r:
                return pos
        return 0

    @lru_cache(None)
    def run(l, r, attach_left, attach_right):
        if l > r:
            return ((0, 0, 0, 0),)
        m = highest_inside(l, r)
        a_states = run(l, m - 1, attach_left, 1)
        b_states = run(m + 1, r, 1, attach_right)
        produced = []
        for a in a_states:
            lh, ld, ah, ad = a
            for b in b_states:
                bh, bd, rh, rd = b
                if attach_left:
                    lh2 = max(lh, ah + 1, bh + 1)
                    ld2 = max(ld, ad, bd, top2(lh + 1, ah, bh))
                    produced.append((lh2, ld2, rh, rd))
                if attach_right:
                    rh2 = max(rh, ah + 1, bh + 1)
                    rd2 = max(rd, ad, bd, top2(ah, bh, rh + 1))
                    produced.append((lh, ld, rh2, rd2))
        return filter_states(produced)

    root = pos_of_value[n]
    left_states = run(1, root - 1, 0, 1)
    right_states = run(root + 1, n, 1, 0)
    best = 0
    for l in left_states:
        for r in right_states:
            best = max(best, l[3], r[1], l[2] + r[0])
    return best

# CLAUSE: finish_program
def main():
    raw = sys.stdin.read().split()
    t = int(raw[0])
    i = 1
    ans = []
    for _ in range(t):
        n = int(raw[i])
        i += 1
        p = [int(x) for x in raw[i:i + n]]
        i += n
        i += 1
        ans.append(str(solve_case(n, p)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
