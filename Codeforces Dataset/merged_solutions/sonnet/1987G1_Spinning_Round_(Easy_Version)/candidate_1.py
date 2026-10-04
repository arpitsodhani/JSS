# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

def top_two_sum(values):
    first = second = 0
    for x in values:
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x
    return first + second

def solve_case(n, p):
    size = 1
    while size < n:
        size *= 2
    
    seg = [0] * (2 * size)
    for i in range(n):
        seg[size + i] = i + 1
    
    def better(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        return a if p[a - 1] > p[b - 1] else b
    
    for i in range(size - 1, 0, -1):
        seg[i] = better(seg[2 * i], seg[2 * i + 1])
    
    def max_pos(l, r):
        l += size - 1
        r += size - 1
        ans = 0
        while l <= r:
            if l % 2 == 1:
                ans = better(ans, seg[l])
                l += 1
            if r % 2 == 0:
                ans = better(ans, seg[r])
                r -= 1
            l //= 2
            r //= 2
        return ans
    
    def prune(states):
        states = list(set(states))
        result = []
        
        for state in states:
            dominated = False
            for other in states:
                if other == state:
                    continue
                if (other[0] >= state[0] and other[1] >= state[1] and
                    other[2] >= state[2] and other[3] >= state[3]):
                    dominated = True
                    break
            if not dominated:
                result.append(state)
        
        return tuple(result)
    
    @lru_cache(None)
    def dp(l, r, has_left, has_right):
        if l > r:
            return ((0, 0, 0, 0),)
        
        m = max_pos(l, r)
        left_states = dp(l, m - 1, has_left, True)
        right_states = dp(m + 1, r, True, has_right)
        
        states = []
        for left in left_states:
            lh, ld, mh_left, md_left = left
            for right in right_states:
                mh_right, md_right, rh, rd = right
                
                if has_left:
                    new_lh = max(lh, 1 + max(mh_left, mh_right))
                    new_ld = max(
                        ld,
                        md_left,
                        md_right,
                        top_two_sum([1 + lh, mh_left, mh_right])
                    )
                    states.append((new_lh, new_ld, rh, rd))
                
                if has_right:
                    new_rh = max(rh, 1 + max(mh_left, mh_right))
                    new_rd = max(
                        rd,
                        md_left,
                        md_right,
                        top_two_sum([mh_left, mh_right, 1 + rh])
                    )
                    states.append((lh, ld, new_rh, new_rd))
        
        return prune(states)
    
    root = p.index(n) + 1
    left_states = dp(1, root - 1, False, True)
    right_states = dp(root + 1, n, True, False)
    
    answer = 0
    for left in left_states:
        for right in right_states:
            answer = max(
                answer,
                left[3],
                right[1],
                left[2] + right[0]
            )
    
    return answer

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        idx += 1  # s, all question marks in the easy version
        answers.append(str(solve_case(n, p)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
