a, b = map(int, input().split())

# Segment count for each digit 0-9
segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

total = 0
for num in range(a, b + 1):
    for digit in str(num):
        total += segments[int(digit)]

print(total)
