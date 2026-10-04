# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    
    bits = 22
    size = 1 << bits
    full = size - 1
    
    dp = [-1] * size
    for x in a:
        dp[x] = x
    
    for bit in range(bits):
        step = 1 << bit
        jump = step << 1
        
        for start in range(0, size, jump):
            left = start
            right = start + step
            
            for i in range(step):
                if dp[right + i] == -1:
                    dp[right + i] = dp[left + i]
    
    result = []
    for x in a:
        result.append(str(dp[full ^ x]))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
