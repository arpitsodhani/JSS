# CLAUSE: setup_environment
import sys
from functools import reduce
from operator import mul

# CLAUSE: solve_logic
n = int(sys.stdin.readline().strip())
fermat = tuple((1 << (1 << i)) + 1 for i in range(10))
result = []
for mask in range(1 << len(fermat)):
    if mask == 0:
        result.append(1)
    elif mask % 2 == 1:
        factors = [fermat[index] for index in range(len(fermat)) if (mask >> index) & 1]
        result.append(reduce(mul, factors, 1))
result = sorted(result)

# CLAUSE: finish_program
print(result[n - 1])
