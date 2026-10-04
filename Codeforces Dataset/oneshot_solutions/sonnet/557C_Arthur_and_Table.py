import sys
from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def add(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx
    
    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
    
    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1
        return idx + 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    lengths = data[1:1 + n]
    costs = data[1 + n:1 + 2 * n]
    
    legs = sorted(zip(lengths, costs))
    all_costs = sorted(set(costs))
    
    bit_count = Fenwick(len(all_costs))
    bit_sum = Fenwick(len(all_costs))
    
    total_cost = sum(costs)
    greater_cost = total_cost
    shorter_count = 0
    answer = total_cost
    
    i = 0
    while i < n:
        j = i
        same_count = 0
        same_cost = 0
        
        while j < n and legs[j][0] == legs[i][0]:
            same_count += 1
            same_cost += legs[j][1]
            j += 1
        
        greater_cost -= same_cost
        
        need_remove = max(0, shorter_count - same_count + 1)
        extra_cost = 0
        
        if need_remove > 0:
            pos = bit_count.kth(need_remove)
            before_count = bit_count.sum(pos - 1)
            before_sum = bit_sum.sum(pos - 1)
            take = need_remove - before_count
            extra_cost = before_sum + take * all_costs[pos - 1]
        
        answer = min(answer, greater_cost + extra_cost)
        
        for k in range(i, j):
            c = legs[k][1]
            pos = bisect_left(all_costs, c) + 1
            bit_count.add(pos, 1)
            bit_sum.add(pos, c)
        
        shorter_count += same_count
        i = j
    
    print(answer)

if __name__ == "__main__":
    main()
