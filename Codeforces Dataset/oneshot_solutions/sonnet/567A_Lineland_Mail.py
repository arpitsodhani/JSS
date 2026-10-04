n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    # Minimum distance
    if i == 0:
        min_dist = x[1] - x[0]
    elif i == n - 1:
        min_dist = x[n-1] - x[n-2]
    else:
        min_dist = min(x[i] - x[i-1], x[i+1] - x[i])
    
    # Maximum distance
    max_dist = max(x[i] - x[0], x[n-1] - x[i])
    
    print(min_dist, max_dist)
