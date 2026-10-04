n = int(input())
f = list(map(int, input().split()))

# Convert to 0-indexed
f = [x - 1 for x in f]

found = False
for i in range(n):
    if f[f[f[i]]] == i:
        found = True
        break

print("YES" if found else "NO")
