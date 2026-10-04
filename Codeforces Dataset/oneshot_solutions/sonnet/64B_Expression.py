s = input().strip()

a = int(s[0])
op = s[1]
b = int(s[2])

if op == '+':
    print(a + b)
else:
    print(a - b)
