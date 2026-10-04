# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def close(left_min, left_max, right_min, right_max):
    return left_min <= right_max + 1 and right_min <= left_max + 1

def solve_case(a):
    n = len(a)
    
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            return 0
    
    answer = n
    for mid in range(n - 1):
        left_min = left_max = a[mid]
        
        for l in range(mid, -1, -1):
            left_min = min(left_min, a[l])
            left_max = max(left_max, a[l])
            
            right_min = right_max = a[mid + 1]
            for r in range(mid + 1, n):
                right_min = min(right_min, a[r])
                right_max = max(right_max, a[r])
                
                if close(left_min, left_max, right_min, right_max):
                    answer = min(answer, r - l - 1)
                    break
    
    return -1 if answer == n else answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        result.append(str(solve_case(a)))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
