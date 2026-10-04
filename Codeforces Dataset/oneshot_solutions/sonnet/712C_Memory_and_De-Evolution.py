x, y = map(int, input().split())

# Work from smaller to larger
start, end = min(x, y), max(x, y)

sides = [start, start, start]
steps = 0

while sides != [end, end, end]:
    sides.sort()
    sides[0] = min(end, sides[1] + sides[2] - 1)
    steps += 1

print(steps)
