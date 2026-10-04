s, x = map(int, input().split())

if s < x or (s - x) % 2 != 0:
    print(0)
else:
    c = (s - x) // 2
    
    if c & x != 0:
        print(0)
    elif x == 0:
        print(1 if s > 0 else 0)
    else:
        k = bin(x).count('1')
        result = 2 ** k
        if c == 0:
            result -= 2
        print(result)
