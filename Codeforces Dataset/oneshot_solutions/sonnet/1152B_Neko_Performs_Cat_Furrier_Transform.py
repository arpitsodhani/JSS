def is_perfect(num):
    return (num & (num + 1)) == 0

x = int(input())

if is_perfect(x):
    print(0)
else:
    operations = []
    step = 0
    
    while not is_perfect(x):
        if step % 2 == 0:  # Operation A
            n = x.bit_length()
            operations.append(n)
            x = x ^ ((1 << n) - 1)
        else:  # Operation B
            x = x + 1
        step += 1
    
    print(step)
    print(' '.join(map(str, operations)))
