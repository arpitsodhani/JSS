H, n = map(int, input().split())
d = list(map(int, input().split()))

# Calculate prefix sums
prefix = [0]
for di in d:
    prefix.append(prefix[-1] + di)

S = prefix[-1]  # Total change after one round

# Check if the monster dies in the first round
for i in range(1, n + 1):
    if H + prefix[i] <= 0:
        print(i)
        exit()

# If S >= 0, the monster never dies
if S >= 0:
    print(-1)
    exit()

# S < 0, calculate when the monster dies
min_minute = float('inf')
for i in range(1, n + 1):
    numerator = H + prefix[i]
    denominator = -S
    k = (numerator + denominator - 1) // denominator
    total_minute = k * n + i
    min_minute = min(min_minute, total_minute)

print(min_minute)
