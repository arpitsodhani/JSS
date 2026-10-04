s = input().strip()
a = int(s[0])
op = s[1]
b = int(s[2])
print(a + b if op == '+' else a - b)
