n, k, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if a[n-1] - a[0] > l:
    print(0)
else:
    if k == 1:
        print(sum(a))
    else:
        print(sum(a[:n]))
