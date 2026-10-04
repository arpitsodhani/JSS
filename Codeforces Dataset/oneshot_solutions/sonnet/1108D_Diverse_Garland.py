n = int(input())
s = list(input().strip())

colors = ['R', 'G', 'B']
changes = 0

for i in range(n - 1):
    if s[i] == s[i + 1]:
        # Need to change s[i + 1]
        for color in colors:
            if color != s[i] and (i + 2 >= n or color != s[i + 2]):
                s[i + 1] = color
                changes += 1
                break

print(changes)
print(''.join(s))
