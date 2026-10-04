import sys

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
    
    def kth(self, k):
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1
        return idx + 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        a = [0] + data[idx:idx + n]
        idx += n
        
        fenwick = Fenwick(n)
        is_record = [False] * (n + 1)
        count = 0
        best = 10 ** 30
        
        for i in range(1, n + 1):
            if a[i] < best:
                best = a[i]
                is_record[i] = True
                fenwick.add(i, 1)
                count += 1
        
        line = []
        
        for _ in range(m):
            k = data[idx]
            d = data[idx + 1]
            idx += 2
            
            a[k] -= d
            
            if not is_record[k]:
                before = fenwick.sum(k - 1)
                prev = fenwick.kth(before)
                
                if a[k] < a[prev]:
                    is_record[k] = True
                    fenwick.add(k, 1)
                    count += 1
                else:
                    line.append(str(count))
                    continue
            
            pos_count = fenwick.sum(k)
            while pos_count < count:
                nxt = fenwick.kth(pos_count + 1)
                if a[nxt] < a[k]:
                    break
                
                is_record[nxt] = False
                fenwick.add(nxt, -1)
                count -= 1
            
            line.append(str(count))
        
        answers.append(' '.join(line))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
