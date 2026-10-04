# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    limit = 70
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        prefix = [0] * (n + 1)
        positions = []
        
        for i, x in enumerate(a):
            prefix[i + 1] = prefix[i] + x
            if x > 1:
                positions.append(i)
        
        if not positions:
            out.append("1 1")
            continue
        
        if len(positions) > limit:
            out.append(f"{positions[0] + 1} {positions[-1] + 1}")
            continue
        
        best_gain = 0
        best_l = 0
        best_r = 0
        
        m = len(positions)
        for i in range(m):
            product = 1
            for j in range(i, m):
                product *= a[positions[j]]
                l = positions[i]
                r = positions[j]
                current_sum = prefix[r + 1] - prefix[l]
                gain = product - current_sum
                
                if gain > best_gain:
                    best_gain = gain
                    best_l = l
                    best_r = r
        
        out.append(f"{best_l + 1} {best_r + 1}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
