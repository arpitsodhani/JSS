import bisect

n, u = map(int, input().split())
e = list(map(int, input().split()))

max_eff = -1

for i in range(n - 2):
    # Find the largest k such that e[k] - e[i] <= u
    target = e[i] + u
    k = bisect.bisect_right(e, target) - 1
    
    if k > i + 1:
        j = i + 1
        eff = (e[k] - e[j]) / (e[k] - e[i])
        max_eff = max(max_eff, eff)

print(max_eff)
