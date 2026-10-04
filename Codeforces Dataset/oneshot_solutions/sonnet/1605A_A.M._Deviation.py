t = int(input())
for _ in range(t):
    a1, a2, a3 = map(int, input().split())
    S = a1 + a3 - 2 * a2
    r = S % 3
    print(min(r, 3 - r))
