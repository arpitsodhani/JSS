# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import deque

def is_good(s, t):
    return (all(c == 'a' for c in s) and all(c == 'b' for c in t)) or \
           (all(c == 'b' for c in s) and all(c == 'a' for c in t))

def runs(x):
    result = []
    for c in x:
        if not result or result[-1] != c:
            result.append(c)
    return ''.join(result)

def apply_op(state, i, j):
    s, t = state
    return (t[:j] + s[i:], s[:i] + t[j:])

def solve():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    
    s, t = data[0], data[1]
    
    if is_good(s, t):
        print(0)
        return
    
    start = (s, t)
    q = deque([start])
    parent = {start: None}
    move = {}
    
    total_len = len(s) + len(t)
    
    while q:
        cur_s, cur_t = q.popleft()
        
        if len(move.get((cur_s, cur_t), [])) > 8:
            continue
        
        for i in range(len(cur_s) + 1):
            for j in range(len(cur_t) + 1):
                if i == 0 and j == 0:
                    continue
                
                ns, nt = apply_op((cur_s, cur_t), i, j)
                if (ns, nt) in parent:
                    continue
                
                parent[(ns, nt)] = (cur_s, cur_t)
                move[(ns, nt)] = (i, j)
                
                if is_good(ns, nt):
                    ans = []
                    state = (ns, nt)
                    while parent[state] is not None:
                        ans.append(move[state])
                        state = parent[state]
                    ans.reverse()
                    
                    print(len(ans))
                    for x, y in ans:
                        print(x, y)
                    return
                
                if runs(ns) == ns and runs(nt) == nt and len(ns) + len(nt) == total_len:
                    q.append((ns, nt))
    
    a_count = s.count('a') + t.count('a')
    b_count = total_len - a_count
    
    target1 = ('a' * a_count, 'b' * b_count)
    target2 = ('b' * b_count, 'a' * a_count)
    
    q = deque([start])
    parent = {start: None}
    move = {}
    
    while q:
        cur_s, cur_t = q.popleft()
        
        for i in range(len(cur_s) + 1):
            for j in range(len(cur_t) + 1):
                if i == 0 and j == 0:
                    continue
                
                ns, nt = apply_op((cur_s, cur_t), i, j)
                if (ns, nt) in parent:
                    continue
                
                parent[(ns, nt)] = (cur_s, cur_t)
                move[(ns, nt)] = (i, j)
                
                if (ns, nt) == target1 or (ns, nt) == target2:
                    ans = []
                    state = (ns, nt)
                    while parent[state] is not None:
                        ans.append(move[state])
                        state = parent[state]
                    ans.reverse()
                    
                    print(len(ans))
                    for x, y in ans:
                        print(x, y)
                    return
                
                q.append((ns, nt))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
