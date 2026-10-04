s = input().strip()
n = len(s)

# Compute prefix arrays
prefix_a = [0] * (n + 1)
prefix_b = [0] * (n + 1)

for i in range(n):
    prefix_a[i + 1] = prefix_a[i] + (1 if s[i] == 'a' else 0)
    prefix_b[i + 1] = prefix_b[i] + (1 if s[i] == 'b' else 0)

# Compute f[i] = prefix_a[i] - prefix_b[i]
# Compute max_f[j] = max(f[0], f[1], ..., f[j])
max_f = prefix_a[0] - prefix_b[0]
max_len = 0

for j in range(n + 1):
    # For this j, length = prefix_a[n] + max_f + (prefix_b[j] - prefix_a[j])
    length = prefix_a[n] + max_f + prefix_b[j] - prefix_a[j]
    max_len = max(max_len, length)
    
    # Update max_f for next iteration
    if j < n:
        f = prefix_a[j + 1] - prefix_b[j + 1]
        max_f = max(max_f, f)

print(max_len)
