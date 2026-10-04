n, m = map(int, input().split())
difficulties = list(map(int, input().split()))

count = [0] * (n + 1)
zeros = n

result = []
for d in difficulties:
    if count[d] == 0:
        zeros -= 1
    count[d] += 1
    
    if zeros == 0:
        result.append('1')
        for i in range(1, n + 1):
            count[i] -= 1
            if count[i] == 0:
                zeros += 1
    else:
        result.append('0')

print(''.join(result))
