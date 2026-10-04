n = int(input())
fingers = list(map(int, input().split()))
S = sum(fingers)

count = 0
for d in range(1, 6):
    total = S + d
    if (total - 1) % (n + 1) != 0:
        count += 1

print(count)
