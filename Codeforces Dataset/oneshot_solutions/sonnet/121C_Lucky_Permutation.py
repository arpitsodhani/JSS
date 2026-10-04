from math import factorial

def get_kth_permutation(n, k):
    # k is 1-indexed, convert to 0-indexed
    k -= 1
    
    elements = list(range(1, n + 1))
    permutation = []
    
    for i in range(n, 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        permutation.append(elements[index])
        elements.pop(index)
        k %= fact
    
    return permutation

def is_lucky(num):
    if num <= 0:
        return False
    s = str(num)
    return all(c in '47' for c in s)

def solve(n, k):
    perm = get_kth_permutation(n, k)
    
    count = 0
    for pos in range(1, n + 1):
        if is_lucky(pos):
            value = perm[pos - 1]
            if is_lucky(value):
                count += 1
    
    return count

# Read input
n, k = map(int, input().split())
print(solve(n, k))
