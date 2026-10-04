p1, p2, p3, p4, a, b = map(int, input().split())
m = min(p1, p2, p3, p4)
print(max(0, min(b, m - 1) - a + 1))
