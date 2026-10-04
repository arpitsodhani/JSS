import sys

input_data = sys.stdin.buffer.read().decode('ascii').strip()
a, x, y = map(int, input_data.split())

if 0 < x < a and 0 < y < a:
    print(0)
elif 0 <= x <= a and 0 <= y <= a:
    print(1)
else:
    print(2)
