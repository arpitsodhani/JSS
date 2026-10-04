n = int(input())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, r, i))

# Sort by right endpoint, then by left endpoint
events.sort(key=lambda x: (x[1], x[0]))

result = [0] * n
used = set()

for l, r, idx in events:
    # Find the smallest day in [l, r] that hasn't been used
    for day in range(l, r + 1):
        if day not in used:
            result[idx] = day
            used.add(day)
            break

print(' '.join(map(str, result)))
