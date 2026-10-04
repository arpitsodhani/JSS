# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 10 ** 9 + 7

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    graph = [[] for _ in range(n)]
    
    idx = 1
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        w = data[idx + 2] % MOD
        idx += 3
        
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    parent = [-1] * n
    parent[0] = 0
    parent_weight = [0] * n
    order = [0]
    
    for v in order:
        for to, w in graph[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            parent_weight[to] = w
            order.append(to)
    
    coef = [0] * n
    const = [0] * n
    
    for v in reversed(order[1:]):
        if len(graph[v]) == 1:
            continue
        
        sum_coef = 0
        sum_const = parent_weight[v]
        
        for to, w in graph[v]:
            if to == parent[v]:
                continue
            sum_coef = (sum_coef + coef[to]) % MOD
            sum_const = (sum_const + w + const[to]) % MOD
        
        denom = (len(graph[v]) - sum_coef) % MOD
        inv_denom = pow(denom, MOD - 2, MOD)
        coef[v] = inv_denom
        const[v] = sum_const * inv_denom % MOD
    
    sum_coef = 0
    sum_const = 0
    
    for to, w in graph[0]:
        sum_coef = (sum_coef + coef[to]) % MOD
        sum_const = (sum_const + w + const[to]) % MOD
    
    denom = (len(graph[0]) - sum_coef) % MOD
    answer = sum_const * pow(denom, MOD - 2, MOD) % MOD
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
