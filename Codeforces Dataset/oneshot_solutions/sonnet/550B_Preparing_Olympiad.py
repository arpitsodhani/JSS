n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))

count = 0
for mask in range(1, 1 << n):
    subset = [c[i] for i in range(n) if mask & (1 << i)]
    
    if len(subset) < 2:
        continue
    
    total = sum(subset)
    if l <= total <= r and max(subset) - min(subset) >= x:
        count += 1

print(count)
