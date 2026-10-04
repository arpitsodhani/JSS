import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(data[i]) for i in range(1, n + 1)]
    
    max_len = 0
    left_indices = set()
    
    for j in range(n):
        divisor = a[j]
        l = j
        while l > 0 and a[l-1] % divisor == 0:
            l -= 1
        
        r = j
        while r < n - 1 and a[r+1] % divisor == 0:
            r += 1
        
        length = r - l
        if length > max_len:
            max_len = length
            left_indices = {l+1}
        elif length == max_len:
            left_indices.add(l+1)
    
    result = sorted(left_indices)
    print(len(result), max_len)
    print(' '.join(map(str, result)))

solve()
