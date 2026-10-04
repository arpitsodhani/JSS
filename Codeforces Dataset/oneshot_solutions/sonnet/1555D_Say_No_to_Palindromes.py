import sys
from itertools import permutations

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    s = data[2].decode()
    
    patterns = [''.join(p) for p in permutations('abc')]
    pref = []
    
    for p in patterns:
        cur = [0] * (n + 1)
        for i in range(n):
            cur[i + 1] = cur[i] + (s[i] != p[i % 3])
        pref.append(cur)
    
    out = []
    idx = 3
    for _ in range(m):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        
        ans = n
        for cur in pref:
            ans = min(ans, cur[r] - cur[l - 1])
        out.append(str(ans))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
