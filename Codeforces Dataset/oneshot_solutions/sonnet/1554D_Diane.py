t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print('a')
    elif n <= 26:
        # Use distinct characters for small n
        print(''.join(chr(ord('a') + i) for i in range(n)))
    elif n % 2 == 0:
        # Even n: (n-1)//2 'a's + 'b' + n//2 'a's  
        print('a' * ((n - 1) // 2) + 'b' + 'a' * (n // 2))
    else:
        # Odd n: n//2 'a's + 'b' + n//2 'a's
        print('a' * (n // 2) + 'b' + 'a' * (n // 2))
