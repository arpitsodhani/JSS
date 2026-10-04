import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = [int(data[i+1]) for i in range(n)]
    
    MOD = 998244353
    
    # Compute prefix XOR
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ a[i]
    
    result = 0
    
    # Process each bit position
    for bit in range(31):
        count = [0, 0]
        sum_indices = [0, 0]
        
        contribution = 0
        for j in range(n + 1):
            b_j = (pre[j] >> bit) & 1
            opposite = 1 - b_j
            
            # Add contribution from all i < j with bit value opposite to b_j
            contribution += j * count[opposite] - sum_indices[opposite]
            
            # Update for current index
            count[b_j] += 1
            sum_indices[b_j] += j
        
        # Apply modulo and add to result
        contribution %= MOD
        result = (result + ((1 << bit) % MOD) * contribution) % MOD
    
    print(result)

solve()
