s = input().strip()
n = len(s)
seen = set()

for i in range(n):
    seen.add(s[i:] + s[:i])

print(len(seen))
