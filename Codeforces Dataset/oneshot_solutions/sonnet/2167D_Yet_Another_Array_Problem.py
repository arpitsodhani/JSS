import sys
from math import gcd

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    idx = 1
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        g = 0
        for _ in range(n):
            g = gcd(g, data[idx])
            idx += 1
        
        candidate = 2
        while True:
            is_prime = True
            d = 2
            while d * d <= candidate:
                if candidate % d == 0:
                    is_prime = False
                    break
                d += 1
            
            if is_prime and g % candidate != 0:
                answers.append(str(candidate))
                break
            
            candidate += 1
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
