# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    p = data[idx + 1]
    idx += 2
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        adj[a].append(b)
        adj[b].append(a)
    
    kmax = n - 1
    if kmax == 0:
        print()
        return
    
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = [1]
    parent[1] = -1
    
    for v in order:
        for to in adj[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            children[v].append(to)
            order.append(to)
    
    dp = [None] * (n + 1)
    leaf_dp = array('I', [0] + [i % p for i in range(1, kmax + 1)])
    
    full = None
    
    for v in reversed(order):
        ch = children[v]
        
        if v == 1:
            full = array('I', [1] * (kmax + 1))
            for c in ch:
                arr = dp[c]
                for t in range(kmax + 1):
                    full[t] = (full[t] * arr[t]) % p
                dp[c] = None
            break
        
        if not ch:
            dp[v] = leaf_dp
            continue
        
        if len(ch) == 1:
            arr = dp[ch[0]]
            res = array('I', [0]) * (kmax + 1)
            for t in range(1, kmax + 1):
                res[t] = (t * arr[t]) % p
            dp[ch[0]] = None
            dp[v] = res
            continue
        
        d = len(ch)
        arrs = [dp[c] for c in ch]
        res = array('I', [0]) * (kmax + 1)
        prefix = [1] * (d + 1)
        extra = [0] * d
        sum_prod = 0
        coef = (1 - d) % p
        
        for t in range(1, kmax + 1):
            for i, arr in enumerate(arrs):
                prefix[i + 1] = (prefix[i] * arr[t]) % p
            
            prod_all = prefix[d]
            sum_prod = (sum_prod + prod_all) % p
            
            suffix = 1
            total = 0
            for i in range(d - 1, -1, -1):
                val = arrs[i][t]
                prod_except = (prefix[i] * suffix) % p
                extra[i] = (extra[i] + prod_except) % p
                total = (total + val * extra[i]) % p
                suffix = (suffix * val) % p
            
            res[t] = (total + coef * sum_prod) % p
        
        for c in ch:
            dp[c] = None
        dp[v] = res
    
    comb = [0] * (kmax + 1)
    comb[0] = 1
    ans = []
    
    for k in range(1, kmax + 1):
        for j in range(k, 0, -1):
            comb[j] = (comb[j] + comb[j - 1]) % p
        
        total = 0
        for s in range(k + 1):
            term = comb[s] * full[s]
            if (k - s) & 1:
                total -= term
            else:
                total += term
        
        ans.append(str(total % p))
    
    print(' '.join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
