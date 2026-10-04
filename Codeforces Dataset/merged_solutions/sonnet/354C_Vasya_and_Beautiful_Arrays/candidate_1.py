# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    a = data[2:]
    
    max_a = max(a)
    min_a = min(a)
    
    freq = [0] * (max_a + 1)
    for x in a:
        freq[x] += 1
    
    prefix = [0] * (max_a + 1)
    for i in range(1, max_a + 1):
        prefix[i] = prefix[i - 1] + freq[i]
    
    for d in range(min_a, 0, -1):
        good = 0
        start = d
        
        while start <= max_a:
            end = min(start + k, start + d - 1, max_a)
            good += prefix[end] - prefix[start - 1]
            start += d
        
        if good == n:
            print(d)
            return

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
