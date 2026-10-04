# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:1 + n]
    
    bits = [x.bit_count() for x in a]
    
    even_prefix = 1
    odd_prefix = 0
    parity = 0
    answer = 0
    
    for b in bits:
        parity ^= b & 1
        if parity == 0:
            answer += even_prefix
            even_prefix += 1
        else:
            answer += odd_prefix
            odd_prefix += 1
    
    bad = 0
    for l in range(n):
        total = 0
        maximum = 0
        
        for r in range(l, min(n, l + 130)):
            total += bits[r]
            maximum = max(maximum, bits[r])
            
            if total % 2 == 0 and maximum * 2 > total:
                bad += 1
    
    print(answer - bad)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
