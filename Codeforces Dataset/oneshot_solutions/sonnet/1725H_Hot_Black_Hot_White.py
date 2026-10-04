def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Compute each stone's value mod 3
    mod3 = [x % 3 for x in a]
    
    # Count stones ≡ 0 (mod 3)
    c0 = sum(1 for m in mod3 if m == 0)
    
    # Initialize coloring
    coloring = ['0'] * n
    white_target = n // 2
    
    if c0 <= n // 2:
        z = 0
        white_count = 0
        
        # Color all stones ≡ 0 (mod 3) as white
        for i in range(n):
            if mod3[i] == 0:
                coloring[i] = '0'
                white_count += 1
        
        # Color additional stones (not ≡ 0 mod 3) as white
        for i in range(n):
            if mod3[i] != 0 and white_count < white_target:
                coloring[i] = '0'
                white_count += 1
            elif mod3[i] != 0:
                coloring[i] = '1'
    else:
        z = 2
        white_count = 0
        
        # Color all stones ≡ 1 or 2 (mod 3) as white
        for i in range(n):
            if mod3[i] != 0:
                coloring[i] = '0'
                white_count += 1
        
        # Color additional stones (≡ 0 mod 3) as white
        for i in range(n):
            if mod3[i] == 0 and white_count < white_target:
                coloring[i] = '0'
                white_count += 1
            elif mod3[i] == 0:
                coloring[i] = '1'
    
    print(z)
    print(''.join(coloring))

solve()
