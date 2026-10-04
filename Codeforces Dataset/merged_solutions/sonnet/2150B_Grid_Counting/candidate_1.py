# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve(n, a):
    MOD = 998244353
    
    if sum(a) != n:
        return 0
    
    all_row_assignments = []
    
    def generate_rows(k, counts, rows):
        if k > n:
            if counts == a:
                all_row_assignments.append(tuple(rows))
            return
        
        for r in range(1, k+1):
            if counts[r-1] < a[r-1]:
                new_counts = counts[:]
                new_counts[r-1] += 1
                generate_rows(k+1, new_counts, rows + [r])
    
    generate_rows(1, [0] * n, [])
    
    total = 0
    
    for row_assignment in all_row_assignments:
        cols = [0] * (n+1)
        flexible_ks = []
        
        for k in range(1, n+1):
            r = row_assignment[k-1]
            if r < k:
                cols[k] = k
            else:
                flexible_ks.append(k)
        
        def count_col_assignments(idx):
            if idx == len(flexible_ks):
                values = []
                for k in range(1, n+1):
                    r = row_assignment[k-1]
                    c = cols[k]
                    v = max(r, n+1-c)
                    values.append(v)
                
                return 1 if sorted(values) == list(range(1, n+1)) else 0
            
            k = flexible_ks[idx]
            count = 0
            for c in range(1, k+1):
                cols[k] = c
                count += count_col_assignments(idx+1)
            return count
        
        total = (total + count_col_assignments(0)) % MOD
    
    return total

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        print(solve(n, a))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
