# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.40]
print(result[n - 1])


