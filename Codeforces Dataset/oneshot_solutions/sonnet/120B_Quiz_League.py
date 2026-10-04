n, k = map(int, input().split())
status = list(map(int, input().split()))

current = k - 1  # Convert to 0-indexed

while status[current] == 0:
    current = (current + 1) % n

print(current + 1)
