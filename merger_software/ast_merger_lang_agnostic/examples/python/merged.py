# Clause C1 [Confidence: 1.00]
if a is None or n <= 0:
    return -1

# Clause C2 [Confidence: 1.00]
max_val = a[0]
last_idx = 0
for i in range(1, n):
    if a[i] >= max_val:
        max_val = a[i]
        last_idx = i
return last_idx

