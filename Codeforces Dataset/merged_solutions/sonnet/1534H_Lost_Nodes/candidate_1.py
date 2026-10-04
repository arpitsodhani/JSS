# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

INF = 10 ** 18

def one_value(costs):
    costs.sort(reverse=True)
    result = len(costs)
    for i, c in enumerate(costs):
        result = max(result, c + i)
    return result

def compute_single(items):
    if not items:
        return 0
    
    costs = [c for c, _ in items]
    base = one_value(costs[:])
    best = base
    
    for i in range(len(items)):
        other = [items[j][0] for j in range(len(items)) if j != i]
        best = min(best, max(one_value(other), items[i][1]))
    
    return best

def transition_all(items):
    d = len(items)
    if d == 1:
        return [0]
    
    order = sorted(range(d), key=lambda i: (-items[i][0], i))
    rank = [0] * d
    costs = [0] * d
    extra = [0] * d
    
    for i, idx in enumerate(order):
        rank[idx] = i
        costs[i] = items[idx][0]
        extra[i] = items[idx][1]
    
    val0 = [costs[i] + i for i in range(d)]
    val1 = [costs[i] + i - 1 for i in range(d)]
    val2 = [costs[i] + i - 2 for i in range(d)]
    
    pref0 = [0] * d
    pref1 = [0] * d
    pref2 = [0] * d
    for i in range(d):
        pref0[i] = val0[i] if i == 0 else max(pref0[i - 1], val0[i])
        pref1[i] = val1[i] if i == 0 else max(pref1[i - 1], val1[i])
        pref2[i] = val2[i] if i == 0 else max(pref2[i - 1], val2[i])
    
    suff0 = [0] * d
    suff1 = [0] * d
    suff2 = [0] * d
    for i in range(d - 1, -1, -1):
        suff0[i] = val0[i] if i == d - 1 else max(suff0[i + 1], val0[i])
        suff1[i] = val1[i] if i == d - 1 else max(suff1[i + 1], val1[i])
        suff2[i] = val2[i] if i == d - 1 else max(suff2[i + 1], val2[i])
    
    def range_max(arr, l, r):
        if l > r:
            return -INF
        if arr == 0:
            return pref0[r] if l == 0 else max(val0[l:r + 1])
        if arr == 1:
            return pref1[r] if l == 0 else max(val1[l:r + 1])
        return pref2[r] if l == 0 else max(val2[l:r + 1])
    
    def one_without(a):
        result = d - 1
        if a > 0:
            result = max(result, pref0[a - 1])
        if a + 1 < d:
            result = max(result, suff1[a + 1])
        return result
    
    def one_without_two(a, b):
        if a > b:
            a, b = b, a
        
        result = d - 2
        if a > 0:
            result = max(result, pref0[a - 1])
        if a + 1 <= b - 1:
            result = max(result, max(val1[a + 1:b]))
        if b + 1 < d:
            result = max(result, suff2[b + 1])
        return result
    
    result_by_rank = [0] * d
    for excluded in range(d):
        best = one_without(excluded)
        for nxt in range(d):
            if nxt == excluded:
                continue
            best = min(best, max(one_without_two(excluded, nxt), extra[nxt]))
        result_by_rank[excluded] = best
    
    result = [0] * d
    for i in range(d):
        result[i] = result_by_rank[rank[i]]
    return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    adj = [[] for _ in range(n)]
    idx = 1
    
    for _ in range(n - 1):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    if n == 1:
        print(0)
        return
    
    parent = [-1] * n
    order = [0]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    
    c_msg = {}
    d_msg = {}
    
    for v in reversed(order[1:]):
        items = []
        for u in adj[v]:
            if u != parent[v]:
                items.append((c_msg[(u, v)], d_msg[(u, v)]))
        
        d = compute_single(items)
        d_msg[(v, parent[v])] = d
        c_msg[(v, parent[v])] = d + 1
    
    for v in order:
        neighbors = adj[v]
        items = []
        ready = True
        
        for u in neighbors:
            if (u, v) not in c_msg:
                ready = False
                break
            items.append((c_msg[(u, v)], d_msg[(u, v)]))
        
        if not ready:
            continue
        
        out = transition_all(items)
        for i, u in enumerate(neighbors):
            d_msg[(v, u)] = out[i]
            c_msg[(v, u)] = out[i] + 1
    
    answer = 0
    
    for v in range(n):
        costs = [c_msg[(u, v)] for u in adj[v]]
        costs.sort(reverse=True)
        m = len(costs)
        
        current = m
        if m >= 1:
            current = max(current, m - 1 + costs[0])
        if m >= 2:
            for j in range(1, m):
                current = max(current, j - 1 + costs[0] + costs[j])
        
        answer = max(answer, current)
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
