import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        
        n = r - l + 1
        a = data[idx:idx + n]
        idx += n
        
        target = set(range(l, r + 1))
        limit = 1
        max_value = max([l, r] + a)
        while limit <= max_value:
            limit <<= 1
        
        answer = 0
        for x in range(limit):
            seen = set()
            ok = True
            
            for value in a:
                original = value ^ x
                if original < l or original > r or original in seen:
                    ok = False
                    break
                seen.add(original)
            
            if ok:
                answer = x
                break
        
        out.append(str(answer))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
