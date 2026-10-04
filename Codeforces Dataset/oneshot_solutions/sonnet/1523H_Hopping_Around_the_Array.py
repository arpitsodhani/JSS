import sys
from array import array

def build_sparse(values, logs):
    tables = []
    n = len(values[0])
    
    for arr in values:
        levels = [arr]
        length = 1
        while length * 2 <= n:
            prev = levels[-1]
            size = n - length * 2 + 1
            cur = array('i', [0]) * size
            for i in range(size):
                a = prev[i]
                b = prev[i + length]
                cur[i] = a if a >= b else b
            levels.append(cur)
            length *= 2
        tables.append(levels)
    
    return tables

def range_max(table, logs, budget, left, right):
    if right < left:
        return left
    levels = table[budget]
    length = right - left + 1
    p = logs[length]
    a = levels[p][left]
    b = levels[p][right - (1 << p) + 1]
    return a if a >= b else b

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    q = data[idx + 1]
    idx += 2
    
    a = data[idx:idx + n]
    idx += n
    
    queries = []
    max_k = 0
    for qi in range(q):
        l = data[idx] - 1
        r = data[idx + 1] - 1
        k = data[idx + 2]
        idx += 3
        queries.append((l, r, k, qi))
        if k > max_k:
            max_k = k
    
    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1
    
    max_level = (n + 1).bit_length() + 1
    
    all_up = []
    base = []
    for c in range(max_k + 1):
        arr = array('i', [0]) * n
        for i, x in enumerate(a):
            if x == 0:
                arr[i] = i
            else:
                reach = i + x + c
                arr[i] = n - 1 if reach >= n else reach
        base.append(arr)
    all_up.append(base)
    
    for level in range(max_level - 1):
        table = build_sparse(all_up[-1], logs)
        nxt = []
        
        for c in range(max_k + 1):
            arr = array('i', [0]) * n
            for i in range(n):
                best = i
                for first_cost in range(c + 1):
                    mid = all_up[-1][first_cost][i]
                    val = range_max(table, logs, c - first_cost, i, mid)
                    if val > best:
                        best = val
                arr[i] = best
            nxt.append(arr)
        
        all_up.append(nxt)
    
    answers = [0] * q
    states = []
    active = []
    
    for pos, (l, r, k, qi) in enumerate(queries):
        if l == r:
            answers[qi] = 0
        else:
            states.append(([l] * (k + 1), 0, l, r, k, qi))
            active.append(len(states) - 1)
    
    for level in range(max_level - 1, -1, -1):
        if not active:
            break
        
        table = build_sparse(all_up[level], logs)
        new_active = []
        
        for state_id in active:
            far, hops, l, r, k, qi = states[state_id]
            new_far = [l] * (k + 1)
            
            for total_cost in range(k + 1):
                best = l
                for used in range(total_cost + 1):
                    right = far[used]
                    if right >= n:
                        right = n - 1
                    val = range_max(table, logs, total_cost - used, l, right)
                    if val > best:
                        best = val
                new_far[total_cost] = best
            
            if new_far[k] < r:
                states[state_id] = (new_far, hops + (1 << level), l, r, k, qi)
            
            new_active.append(state_id)
        
        active = new_active
    
    for far, hops, l, r, k, qi in states:
        answers[qi] = -1 if far[k] < r else hops + 1
    
    sys.stdout.write('\n'.join(map(str, answers)))

if __name__ == "__main__":
    main()
