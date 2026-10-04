n = input().strip()
current = int(n)

count = 0
while current >= 10:
    current = sum(int(d) for d in str(current))
    count += 1

print(count)
