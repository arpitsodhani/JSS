import sys

def main():
    def count(mask, min_val):
        if mask == 0:
            return 1
        
        key = (mask, min_val)
        if key in memo:
            return memo[key]
        
        result = 0
        for num in range(1, n + 1):
            if (mask >> (num - 1)) & 1 and num >= min_val:
                new_mask = mask ^ (1 << (num - 1))
                result += count(new_mask, num - 1)
        
        memo[key] = result
        return result
    
    def construct(mask, min_val, k):
        if mask == 0:
            return []
        
        for num in range(1, n + 1):
            if (mask >> (num - 1)) & 1 and num >= min_val:
                new_mask = mask ^ (1 << (num - 1))
                cnt = count(new_mask, num - 1)
                if k <= cnt:
                    return [num] + construct(new_mask, num - 1, k)
                k -= cnt
        
        return None
    
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        memo = {}
        initial_mask = (1 << n) - 1
        total = count(initial_mask, 1)
        
        if k > total:
            print(-1)
        else:
            result = construct(initial_mask, 1, k)
            print(' '.join(map(str, result)))

main()
