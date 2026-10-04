import sys
from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def add(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx
    
    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        values = sorted(set(a))
        tree = Fenwick(len(values))
        
        result = 0
        seen = 0
        
        for x in a:
            pos = bisect_left(values, x) + 1
            
            less = tree.sum(pos - 1)
            less_or_equal = tree.sum(pos)
            greater = seen - less_or_equal
            
            result += min(less, greater)
            tree.add(pos, 1)
            seen += 1
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
