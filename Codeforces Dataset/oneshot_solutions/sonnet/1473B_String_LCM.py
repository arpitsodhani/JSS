import sys
from math import gcd

def main():
    data = sys.stdin.read().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(q):
        s = data[idx]
        t = data[idx + 1]
        idx += 2
        
        g = gcd(len(s), len(t))
        lcm_len = len(s) // g * len(t)
        
        a = s * (lcm_len // len(s))
        b = t * (lcm_len // len(t))
        
        if a == b:
            out.append(a)
        else:
            out.append("-1")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
