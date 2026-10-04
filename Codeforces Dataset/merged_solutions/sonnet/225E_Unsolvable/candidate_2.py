# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(sys.stdin.readline())
fermat = [2 ** (2 ** i) + 1 for i in range(10)]
values = []
for mask in range(1 << 10):
    if mask == 0 or (mask & 1):
        product = 1
        for i, value in enumerate(fermat):
            if mask & (1 << i):
                product *= value
        values.append(product)
values.sort()

# CLAUSE: finish_program
print(values[n - 1])
