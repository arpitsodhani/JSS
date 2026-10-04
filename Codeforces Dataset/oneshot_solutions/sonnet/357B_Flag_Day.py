n, m = map(int, input().split())
colors = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    dancers = [a, b, c]
    
    assigned = set()
    unassigned = []
    for d in dancers:
        if colors[d] != 0:
            assigned.add(colors[d])
        else:
            unassigned.append(d)
    
    available = []
    for col in [1, 2, 3]:
        if col not in assigned:
            available.append(col)
    
    for i, d in enumerate(unassigned):
        colors[d] = available[i]

print(' '.join(map(str, colors[1:])))
