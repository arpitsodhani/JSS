import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(data[i + 1]) for i in range(n)]
    
    MOD = 10**9 + 7
    
    # Coordinate compression
    sorted_a = sorted(enumerate(a), key=lambda x: x[1])
    rank = [0] * n
    for r, (i, _) in enumerate(sorted_a):
        rank[i] = r + 1
    
    # Fenwick Tree
    class FenwickTree:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)
        
        def update(self, idx, val):
            while idx <= self.size:
                self.tree[idx] = (self.tree[idx] + val) % MOD
                idx += idx & (-idx)
        
        def query(self, idx):
            res = 0
            while idx > 0:
                res = (res + self.tree[idx]) % MOD
                idx -= idx & (-idx)
            return res
    
    # Compute S1(i) = sum of (j+1) for j < i where a[j] < a[i]
    S1 = [0] * n
    ft1 = FenwickTree(n)
    for i in range(n):
        S1[i] = ft1.query(rank[i] - 1)
        ft1.update(rank[i], i + 1)
    
    # Compute S2(i) = sum of (n-j) for j > i where a[j] < a[i]
    S2 = [0] * n
    ft2 = FenwickTree(n)
    for i in range(n - 1, -1, -1):
        S2[i] = ft2.query(rank[i] - 1)
        ft2.update(rank[i], n - i)
    
    # Compute total contribution
    total = 0
    for i in range(n):
        contrib = a[i] % MOD
        term1 = (n - i) * ((i + 1 + S1[i]) % MOD) % MOD
        term2 = (i + 1) * S2[i] % MOD
        term = (term1 + term2) % MOD
        total = (total + contrib * term) % MOD
    
    print(total)

if __name__ == "__main__":
    main()
