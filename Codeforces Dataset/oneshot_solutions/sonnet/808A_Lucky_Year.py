n = int(input())
s = str(n)
first_digit = int(s[0])
length = len(s)

if first_digit < 9:
    next_lucky = (first_digit + 1) * (10 ** (length - 1))
else:
    next_lucky = 10 ** length

print(next_lucky - n)
