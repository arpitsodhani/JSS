# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve(n, fixed):
    MOD = 10**9 + 7
    
    used = set(v for v in fixed if v != -1)
    available = [v for v in range(1, n + 1) if v not in used]
    unknown_pos = [i for i in range(n) if fixed[i] == -1]
    
    if len(available) != len(unknown_pos):
        return 0
    
    def is_valid_partial(perm):
        for center in range(n):
            if perm[center] == -1:
                continue
            for radius in range(1, min(center + 1, n - center)):
                if center - radius < 0 or center + radius >= n:
                    continue
                subarray = perm[center - radius:center + radius + 1]
                if -1 in subarray:
                    continue
                sorted_sub = sorted(subarray)
                if sorted_sub[radius] == perm[center]:
                    return False
        return True
    
    count = [0]
    
    def backtrack(pos_idx, perm, remaining):
        if pos_idx == len(unknown_pos):
            count[0] += 1
            return
        
        pos = unknown_pos[pos_idx]
        for val in remaining:
            perm[pos] = val
            if is_valid_partial(perm):
                backtrack(pos_idx + 1, perm, remaining - {val})
            perm[pos] = -1
    
    perm = fixed[:]
    backtrack(0, perm, set(available))
    
    return count[0] % MOD

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        fixed = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        print(solve(n, fixed))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
