n = int(input())
strengths = list(map(int, input().split()))
assignment = input().strip()

# Calculate initial Bob's strength (all B's)
initial = sum(strengths[i] for i in range(n) if assignment[i] == 'B')

max_gain = 0

# Try all prefixes
gain = 0
for i in range(n):
    if assignment[i] == 'A':
        gain += strengths[i]
    else:
        gain -= strengths[i]
    max_gain = max(max_gain, gain)

# Try all suffixes
gain = 0
for i in range(n-1, -1, -1):
    if assignment[i] == 'A':
        gain += strengths[i]
    else:
        gain -= strengths[i]
    max_gain = max(max_gain, gain)

print(initial + max_gain)
