def solve(n):
    MOD = 998244353
    
    # Compute minimum depth sum for each size
    f = [0] * (n + 1)
    for i in range(2, n + 1):
        f[i] = float('inf')
        for k in range(1, i + 1):
            f[i] = min(f[i], f[k-1] + f[i-k] + i - 1)
    
    memo = {}
    
    def count(size, start_parity, is_left_child, parent_parity):
        """
        Count perfectly balanced striped BSTs.
        size: number of nodes
        start_parity: parity of smallest key (0=even, 1=odd)
        is_left_child: None/True/False
        parent_parity: parity of parent's key
        """
        if size == 0:
            return 1
        
        if size == 1:
            root_parity = start_parity
            if is_left_child is not None:
                if is_left_child and root_parity == parent_parity:
                    return 0
                if not is_left_child and root_parity != parent_parity:
                    return 0
            return 1
        
        key = (size, start_parity, is_left_child, parent_parity)
        if key in memo:
            return memo[key]
        
        result = 0
        min_sum = f[size]
        
        for k in range(1, size + 1):
            left_size = k - 1
            right_size = size - k
            
            # Check if this split achieves minimum depth sum
            if f[left_size] + f[right_size] + size - 1 != min_sum:
                continue
            
            # Root at position k has parity (start_parity + k - 1) % 2
            root_parity = (start_parity + k - 1) % 2
            
            # Check striped constraint from parent
            if is_left_child is not None:
                if is_left_child and root_parity == parent_parity:
                    continue
                if not is_left_child and root_parity != parent_parity:
                    continue
            
            # Subtree starting parities
            left_start_parity = start_parity
            right_start_parity = (start_parity + k) % 2
            
            # Count valid subtrees
            left_count = count(left_size, left_start_parity, True, root_parity)
            right_count = count(right_size, right_start_parity, False, root_parity)
            
            result = (result + left_count * right_count) % MOD
        
        memo[key] = result
        return result
    
    # Keys 1 to n start with parity 1 (1 is odd)
    return count(n, 1, None, None)

n = int(input())
print(solve(n))
