t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    tools = list(map(int, input().split()))
    
    total_time = b
    for x in tools:
        total_time += min(x, a - 1)
    
    print(total_time)
