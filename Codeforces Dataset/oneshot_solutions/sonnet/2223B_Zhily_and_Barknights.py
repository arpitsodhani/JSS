import sys
from collections import Counter

MOD = 998244353

class Ratio:
    __slots__ = ("num", "den", "weight")
    
    def __init__(self, num, den, weight):
        self.num = num
        self.den = den
        self.weight = weight
    
    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n
        
        if n == 1:
            out.append("0")
            continue
        
        b_count = Counter(b)
        b_items = list(b_count.items())
        
        ratios = []
        for den, den_count in b_items:
            for num, num_count in b_items:
                if den == num:
                    weight = den_count * (den_count - 1)
                else:
                    weight = den_count * num_count
                
                if weight:
                    ratios.append(Ratio(num, den, weight))
        
        ratios.sort()
        
        nums = [r.num for r in ratios]
        dens = [r.den for r in ratios]
        prefix = [0] * (len(ratios) + 1)
        for i, r in enumerate(ratios):
            prefix[i + 1] = (prefix[i] + r.weight) % MOD
        
        def count_less(x, y):
            low, high = 0, len(ratios)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] * y < dens[mid] * x:
                    low = mid + 1
                else:
                    high = mid
            return prefix[low]
        
        seen = Counter()
        total = 0
        
        for y in a:
            for x, cnt in seen.items():
                total = (total + cnt * count_less(x, y)) % MOD
            seen[y] += 1
        
        denom = n * (n - 1) % MOD
        answer = total * pow(denom, MOD - 2, MOD) % MOD
        out.append(str(answer))
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
