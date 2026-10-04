n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))

mn = min(s)
mx = max(b)

if mx <= mn:
    print(r)
else:
    shares = r // mn
    print((r % mn) + shares * mx)
