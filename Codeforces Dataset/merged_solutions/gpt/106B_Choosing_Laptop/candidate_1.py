# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n = data[0]
laptops = []

pos = 1
for i in range(n):
    a, b, c, d = data[pos:pos + 4]
    pos += 4
    laptops.append((a, b, c, d, i + 1))

best_price = 10**18
best_index = -1

for i in range(n):
    outdated = False
    for j in range(n):
        if (laptops[i][0] < laptops[j][0] and
            laptops[i][1] < laptops[j][1] and
            laptops[i][2] < laptops[j][2]):
            outdated = True
            break

    if not outdated and laptops[i][3] < best_price:
        best_price = laptops[i][3]
        best_index = laptops[i][4]

print(best_index)

# CLAUSE: finish_program
RESULT_SENTINEL = None
