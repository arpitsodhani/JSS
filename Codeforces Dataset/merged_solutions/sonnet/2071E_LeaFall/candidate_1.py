# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 998244353
INV2 = (MOD + 1) // 2

def solve_case(n, probs, edges):
    survive = [0] * (n + 1)
    fall = [0] * (n + 1)
    
    for i in range(1, n + 1):
        p, q = probs[i - 1]
        prob_fall = (p % MOD) * pow(q % MOD, MOD - 2, MOD) % MOD
        fall[i] = prob_fall
        survive[i] = (1 - prob_fall) % MOD
    
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    zero_count = [0] * (n + 1)
    prod_nonzero = [1] * (n + 1)
    ratio_sum = [0] * (n + 1)
    
    for v in range(1, n + 1):
        prod = 1
        total = 0
        zeros = 0
        
        for u in graph[v]:
            if fall[u] == 0:
                zeros += 1
            else:
                inv = pow(fall[u], MOD - 2, MOD)
                prod = prod * fall[u] % MOD
                total = (total + survive[u] * inv) % MOD
        
        zero_count[v] = zeros
        prod_nonzero[v] = prod
        ratio_sum[v] = total
    
    def all_fall_except(v, banned):
        zeros = zero_count[v]
        prod = prod_nonzero[v]
        
        if fall[banned] == 0:
            zeros -= 1
        else:
            prod = prod * pow(fall[banned], MOD - 2, MOD) % MOD
        
        return 0 if zeros > 0 else prod
    
    def one_survives_except(v, banned):
        zeros = zero_count[v]
        prod = prod_nonzero[v]
        total = ratio_sum[v]
        
        if fall[banned] == 0:
            zeros -= 1
        else:
            inv = pow(fall[banned], MOD - 2, MOD)
            prod = prod * inv % MOD
            total = (total - survive[banned] * inv) % MOD
        
        if zeros >= 2:
            return 0
        if zeros == 1:
            return prod
        return prod * total % MOD
    
    leaf_prob = [0] * (n + 1)
    total_leaf = 0
    total_leaf_sq = 0
    
    for v in range(1, n + 1):
        if zero_count[v] >= 2:
            exact_one = 0
        elif zero_count[v] == 1:
            exact_one = prod_nonzero[v]
        else:
            exact_one = prod_nonzero[v] * ratio_sum[v] % MOD
        
        leaf_prob[v] = survive[v] * exact_one % MOD
        total_leaf = (total_leaf + leaf_prob[v]) % MOD
        total_leaf_sq = (total_leaf_sq + leaf_prob[v] * leaf_prob[v]) % MOD
    
    answer = (total_leaf * total_leaf - total_leaf_sq) * INV2 % MOD
    
    for u, v in edges:
        actual = survive[u] * survive[v] % MOD
        actual = actual * all_fall_except(u, v) % MOD
        actual = actual * all_fall_except(v, u) % MOD
        
        expected_independent = leaf_prob[u] * leaf_prob[v] % MOD
        answer = (answer + actual - expected_independent) % MOD
    
    for center in range(1, n + 1):
        sum_a = sum_a_sq = 0
        sum_b = sum_b_sq = 0
        sum_c = sum_c_sq = 0
        
        for v in graph[center]:
            a = survive[v] * all_fall_except(v, center) % MOD
            b = survive[v] * one_survives_except(v, center) % MOD
            c = leaf_prob[v]
            
            sum_a = (sum_a + a) % MOD
            sum_a_sq = (sum_a_sq + a * a) % MOD
            sum_b = (sum_b + b) % MOD
            sum_b_sq = (sum_b_sq + b * b) % MOD
            sum_c = (sum_c + c) % MOD
            sum_c_sq = (sum_c_sq + c * c) % MOD
        
        actual_pairs = survive[center] * (sum_a * sum_a - sum_a_sq) % MOD
        actual_pairs += fall[center] * (sum_b * sum_b - sum_b_sq) % MOD
        actual_pairs %= MOD
        actual_pairs = actual_pairs * INV2 % MOD
        
        independent_pairs = (sum_c * sum_c - sum_c_sq) * INV2 % MOD
        answer = (answer + actual_pairs - independent_pairs) % MOD
    
    return answer % MOD

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        probs = []
        for _ in range(n):
            p = data[idx]
            q = data[idx + 1]
            idx += 2
            probs.append((p, q))
        
        edges = []
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            edges.append((u, v))
        
        out.append(str(solve_case(n, probs, edges)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
