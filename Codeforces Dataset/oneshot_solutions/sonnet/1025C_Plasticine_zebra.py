s = input().strip()
n = len(s)
max_zebra = 1

# Check s + s
doubled_s = s + s
current_len = 1
for i in range(1, 2 * n):
    if doubled_s[i] != doubled_s[i-1]:
        current_len += 1
    else:
        current_len = 1
    max_zebra = max(max_zebra, min(current_len, n))

# Check reverse(s) + reverse(s)
doubled_rev = s[::-1] + s[::-1]
current_len = 1
for i in range(1, 2 * n):
    if doubled_rev[i] != doubled_rev[i-1]:
        current_len += 1
    else:
        current_len = 1
    max_zebra = max(max_zebra, min(current_len, n))

print(max_zebra)
