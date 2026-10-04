# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        x = int(data[idx])
        idx += 1
        
        removed = 0
        last_removed = -10
        
        for i in range(n):
            if i >= 1 and last_removed != i - 1:
                if a[i] + a[i - 1] < 2 * x:
                    removed += 1
                    last_removed = i
                    continue
            
            if i >= 2 and last_removed != i - 1 and last_removed != i - 2:
                if a[i] + a[i - 1] + a[i - 2] < 3 * x:
                    removed += 1
                    last_removed = i
        
        results.append(str(n - removed))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
