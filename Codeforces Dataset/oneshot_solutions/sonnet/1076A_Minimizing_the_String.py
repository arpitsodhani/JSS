n = int(input())
s = input().strip()

remove_idx = n - 1
for i in range(n - 1):
    if s[i] > s[i + 1]:
        remove_idx = i
        break

print(s[:remove_idx] + s[remove_idx + 1:])
