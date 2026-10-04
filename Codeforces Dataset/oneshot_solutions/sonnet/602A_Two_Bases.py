import sys

def base_to_decimal(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
    return result

data = sys.stdin.read().split()
idx = 0

n = int(data[idx])
b_x = int(data[idx + 1])
idx += 2

x_digits = [int(data[idx + i]) for i in range(n)]
idx += n

m = int(data[idx])
b_y = int(data[idx + 1])
idx += 2

y_digits = [int(data[idx + i]) for i in range(m)]

x_value = base_to_decimal(x_digits, b_x)
y_value = base_to_decimal(y_digits, b_y)

if x_value < y_value:
    print('<')
elif x_value > y_value:
    print('>')
else:
    print('=')
