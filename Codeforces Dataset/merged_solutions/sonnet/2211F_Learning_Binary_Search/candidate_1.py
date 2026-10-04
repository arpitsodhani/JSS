# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

MOD = 676767677

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    T = int(input_data[0])
    idx = 1
    
    # Precompute factorials
    MAX = 2 * 10**6 + 10
    fact = [1] * MAX
    for i in range(1, MAX):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * MAX
    inv_fact[MAX-1] = pow(fact[MAX-1], MOD - 2, MOD)
    for i in range(MAX-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n or n < 0:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
    
    def count_arrays(length, low, high):
        if length == 0:
            return 1
        if low > high:
            return 0
        n = high - low + length
        return comb(n, length)
    
    results = []
    for _ in range(T):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        memo = {}
        
        def solve(l, r, low, high):
            if l > r or low > high:
                return 0, 0
            
            key = (l, r, low, high)
            if key in memo:
                return memo[key]
            
            if l == r:
                result = (high - low + 1) % MOD
                memo[key] = (result, result)
                return result, result
            
            mid = (l + r) // 2
            total_solve = 0
            total_distinct = 0
            
            for v in range(low, high + 1):
                L_count = count_arrays(mid - l, low, v)
                R_count = count_arrays(r - mid, v, high)
                
                # k == v
                total_solve = (total_solve + L_count * R_count) % MOD
                total_distinct = (total_distinct + L_count * R_count) % MOD
                
                # k < v
                if v > low and mid > l:
                    S_L, D_L = solve(l, mid - 1, low, v - 1)
                    total_solve = (total_solve + R_count * (D_L + S_L)) % MOD
                    total_distinct = (total_distinct + R_count * D_L) % MOD
                
                # k > v
                if v < high and mid < r:
                    S_R, D_R = solve(mid + 1, r, v + 1, high)
                    total_solve = (total_solve + L_count * (D_R + S_R)) % MOD
                    total_distinct = (total_distinct + L_count * D_R) % MOD
            
            memo[key] = (total_solve, total_distinct)
            return total_solve, total_distinct
        
        ans, _ = solve(1, n, 1, m)
        results.append(ans)
    
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
