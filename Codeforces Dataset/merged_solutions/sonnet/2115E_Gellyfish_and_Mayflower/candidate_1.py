# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

NEG = -10**30

def close_mod(values, mod, base_w, cost, power):
    d = gcd(mod, cost)
    result = [NEG] * mod
    
    for start in range(d):
        seq = []
        x = start
        while True:
            seq.append(x)
            x = (x + cost) % mod
            if x == start:
                break
        
        length = len(seq)
        gains = [power - ((seq[i] + cost) // mod) * base_w for i in range(length)]
        
        prefix = [0] * (2 * length)
        for i in range(1, 2 * length):
            prefix[i] = prefix[i - 1] + gains[(i - 1) % length]
        
        deque_idx = []
        head = 0
        
        for k in range(2 * length - 1):
            pos = seq[k % length]
            val = values[pos]
            cand = val - prefix[k] if val > NEG // 2 else NEG
            
            while len(deque_idx) > head:
                last = deque_idx[-1]
                last_pos = seq[last % length]
                last_val = values[last_pos]
                last_cand = last_val - prefix[last] if last_val > NEG // 2 else NEG
                if last_cand >= cand:
                    break
                deque_idx.pop()
            deque_idx.append(k)
            
            left = k - length + 1
            while len(deque_idx) > head and deque_idx[head] < left:
                head += 1
            
            if k >= length - 1:
                best = deque_idx[head]
                best_pos = seq[best % length]
                best_val = values[best_pos]
                if best_val > NEG // 2:
                    result[pos] = best_val - prefix[best] + prefix[k]
    
    return result

def merge_into(dst, src):
    if src is None:
        return dst
    if dst is None:
        return src[:]
    for i, val in enumerate(src):
        if val > dst[i]:
            dst[i] = val
    return dst

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    cost = [0] * (n + 1)
    power = [0] * (n + 1)
    for i in range(1, n + 1):
        cost[i] = data[idx]
        power[i] = data[idx + 1]
        idx += 2
    
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        edges[u].append(v)
    
    q = data[idx]
    idx += 1
    
    queries = []
    max_cost = max(cost)
    small_limit = max_cost * max_cost
    small_need = 0
    has_large = False
    
    for _ in range(q):
        p = data[idx]
        r = data[idx + 1]
        idx += 2
        queries.append((p, r))
        if r <= small_limit:
            small_need = max(small_need, r)
        else:
            has_large = True
    
    small_dp = None
    if small_need > 0:
        small_dp = [[NEG] * (small_need + 1) for _ in range(n + 1)]
        small_dp[1] = [0] * (small_need + 1)
        
        for u in range(1, n + 1):
            arr = small_dp[u]
            c = cost[u]
            w = power[u]
            for x in range(c, small_need + 1):
                val = arr[x - c] + w
                if val > arr[x]:
                    arr[x] = val
            
            for v in edges[u]:
                dst = small_dp[v]
                for x, val in enumerate(arr):
                    if val > dst[x]:
                        dst[x] = val
    
    large_table = None
    if has_large:
        large_table = [None] * (n + 1)
        
        for best in range(1, n + 1):
            c_best = cost[best]
            w_best = power[best]
            
            dp0 = [None] * (n + 1)
            dp1 = [None] * (n + 1)
            
            if power[1] * c_best <= w_best * cost[1]:
                start = [NEG] * c_best
                start[0] = 0
                if best == 1:
                    dp1[1] = start
                else:
                    dp0[1] = start
            
            for u in range(1, n + 1):
                if power[u] * c_best > w_best * cost[u]:
                    continue
                
                if u == best:
                    dp1[u] = merge_into(dp1[u], dp0[u])
                    dp0[u] = None
                
                if u != best:
                    if dp0[u] is not None:
                        dp0[u] = close_mod(dp0[u], c_best, w_best, cost[u], power[u])
                    if dp1[u] is not None:
                        dp1[u] = close_mod(dp1[u], c_best, w_best, cost[u], power[u])
                
                for v in edges[u]:
                    if power[v] * c_best <= w_best * cost[v]:
                        dp0[v] = merge_into(dp0[v], dp0[u])
                        dp1[v] = merge_into(dp1[v], dp1[u])
            
            table_for_best = [None] * (n + 1)
            for p in range(1, n + 1):
                arr = dp1[p]
                if arr is None:
                    table_for_best[p] = [NEG] * c_best
                    continue
                
                prefix = [NEG] * c_best
                suffix = [NEG] * (c_best + 1)
                
                cur = NEG
                for i in range(c_best):
                    if arr[i] > cur:
                        cur = arr[i]
                    prefix[i] = cur
                
                cur = NEG
                for i in range(c_best - 1, -1, -1):
                    if arr[i] > cur:
                        cur = arr[i]
                    suffix[i] = cur
                
                offsets = [NEG] * c_best
                for rem in range(c_best):
                    best_val = prefix[rem]
                    if suffix[rem + 1] > NEG // 2:
                        best_val = max(best_val, suffix[rem + 1] - w_best)
                    offsets[rem] = best_val
                
                table_for_best[p] = offsets
            
            large_table[best] = table_for_best
    
    out = []
    for p, r in queries:
        if r <= small_limit:
            out.append(str(small_dp[p][r]))
        else:
            ans = NEG
            for best in range(1, n + 1):
                c_best = cost[best]
                val = large_table[best][p][r % c_best]
                if val > NEG // 2:
                    total = (r // c_best) * power[best] + val
                    if total > ans:
                        ans = total
            out.append(str(ans))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
