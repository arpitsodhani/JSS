import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    words = data[2:2 + n]
    queries = data[2 + n:]
    
    mod1 = 1000000007
    mod2 = 1000000009
    base = 911382323
    
    max_len = 0
    for s in words:
        max_len = max(max_len, len(s))
    for s in queries:
        max_len = max(max_len, len(s))
    
    pow1 = [1] * (max_len + 1)
    pow2 = [1] * (max_len + 1)
    for i in range(max_len):
        pow1[i + 1] = pow1[i] * base % mod1
        pow2[i + 1] = pow2[i] * base % mod2
    
    stored = set()
    
    def get_hash(s):
        h1 = 0
        h2 = 0
        for c in s:
            val = c - 96
            h1 = (h1 * base + val) % mod1
            h2 = (h2 * base + val) % mod2
        return h1, h2
    
    for s in words:
        stored.add((len(s),) + get_hash(s))
    
    result = []
    letters = (1, 2, 3)
    
    for s in queries:
        length = len(s)
        h1, h2 = get_hash(s)
        found = False
        
        for i, c in enumerate(s):
            old = c - 96
            power = length - i - 1
            
            for new in letters:
                if new == old:
                    continue
                
                nh1 = (h1 + (new - old) * pow1[power]) % mod1
                nh2 = (h2 + (new - old) * pow2[power]) % mod2
                
                if (length, nh1, nh2) in stored:
                    found = True
                    break
            
            if found:
                break
        
        result.append("YES" if found else "NO")
    
    print("\n".join(result))

if __name__ == "__main__":
    main()
