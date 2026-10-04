n = int(input())

lower = -10**18
upper = 10**18

for _ in range(n):
    parts = input().split()
    op = parts[0]
    x = int(parts[1])
    answer = parts[2]
    
    if answer == 'Y':
        if op == '>':
            lower = max(lower, x + 1)
        elif op == '<':
            upper = min(upper, x - 1)
        elif op == '>=':
            lower = max(lower, x)
        elif op == '<=':
            upper = min(upper, x)
    else:  # answer == 'N'
        if op == '>':
            upper = min(upper, x)
        elif op == '<':
            lower = max(lower, x)
        elif op == '>=':
            upper = min(upper, x - 1)
        elif op == '<=':
            lower = max(lower, x + 1)

if lower > upper:
    print("Impossible")
else:
    print(lower)
