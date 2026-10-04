n = int(input())
if n == 1:
    print(0)
else:
    ans = n - 1
    for x in range(1, n + 1):
        a, b = n, x
        cur = 0
        ok = True
        while a != b:
            if a < b:
                a, b = b, a
            q = (a - 1) // b
            a -= q * b
            cur += q
            if cur >= ans:
                ok = False
                break
        if ok and a == 1:
            ans = min(ans, cur)
    print(ans)
