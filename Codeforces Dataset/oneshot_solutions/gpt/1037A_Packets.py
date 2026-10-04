n = int(input())
ans = 0
v = 1
while v <= n:
    v <<= 1
    ans += 1
print(ans)
