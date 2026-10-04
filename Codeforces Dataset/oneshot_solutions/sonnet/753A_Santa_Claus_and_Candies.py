n = int(input())

# Find largest k such that k*(k+1)/2 <= n
k = 0
while (k+1)*(k+2)//2 <= n:
    k += 1

sum_k = k * (k + 1) // 2
r = n - sum_k

if r == 0:
    print(k)
    print(' '.join(map(str, range(1, k+1))))
else:
    if r > k:
        print(k + 1)
        print(' '.join(map(str, list(range(1, k+1)) + [r])))
    else:
        print(k)
        print(' '.join(map(str, list(range(1, k)) + [k + r])))
