# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(input())

fermat = []
for i in range(10):
    fermat.append(2 ** (2 ** i) + 1)

products = []

for mask in range(1 << len(fermat)):
    if mask == 0 or mask & 1:
        prod = 1
        for i in range(len(fermat)):
            if mask & (1 << i):
                prod *= fermat[i]
        products.append(prod)

products.sort()
print(products[n - 1])

# CLAUSE: finish_program
RESULT_SENTINEL = None
