import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = data[0]
    start = data[1]
    end = data[2]
    
    n = len(t)
    a = len(start)
    b = len(end)
    
    base1 = 911382323
    base2 = 972663749
    mod1 = 1000000007
    mod2 = 1000000009
    
    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    
    for i, ch in enumerate(t):
        x = ord(ch)
        pow1[i + 1] = pow1[i] * base1 % mod1
        pow2[i + 1] = pow2[i] * base2 % mod2
        h1[i + 1] = (h1[i] * base1 + x) % mod1
        h2[i + 1] = (h2[i] * base2 + x) % mod2
    
    def get_hash(l, r):
        x1 = (h1[r] - h1[l] * pow1[r - l]) % mod1
        x2 = (h2[r] - h2[l] * pow2[r - l]) % mod2
        return (x1, x2, r - l)
    
    starts = []
    ends = []
    
    for i in range(n - a + 1):
        if t[i:i + a] == start:
            starts.append(i)
    
    for i in range(n - b + 1):
        if t[i:i + b] == end:
            ends.append(i)
    
    seen = set()
    
    for l in starts:
        min_end = l + a
        for e in ends:
            r = e + b
            if e >= l and r >= min_end:
                seen.add(get_hash(l, r))
    
    print(len(seen))

if __name__ == "__main__":
    main()
