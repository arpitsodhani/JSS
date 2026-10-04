t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    points = [(a, 0), (b, 0), (c, 1), (d, 1)]
    points.sort()
    
    # Check if pattern alternates (0, 1, 0, 1) or (1, 0, 1, 0)
    if points[0][1] != points[1][1] and points[1][1] != points[2][1]:
        print("YES")
    else:
        print("NO")
