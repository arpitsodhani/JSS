# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import Counter

MOD = 1000000007

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    a = data[2:]
    
    total = sum(a)
    powers = [total - v for v in a]
    count = Counter(powers)
    
    current = None
    carry = 0
    
    for exponent in sorted(count):
        if current is not None:
            while carry > 0 and current < exponent:
                if carry % x != 0:
                    print(pow(x, min(current, total), MOD))
                    return
                carry //= x
                current += 1
        
        current = exponent
        carry += count[exponent]
        
        if carry % x != 0:
            print(pow(x, min(current, total), MOD))
            return
        
        carry //= x
        current += 1
    
    while carry > 0:
        if carry % x != 0:
            print(pow(x, min(current, total), MOD))
            return
        carry //= x
        current += 1
    
    print(pow(x, total, MOD))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
