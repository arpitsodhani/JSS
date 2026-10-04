# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, k, p = (data[0], data[1], data[2])
a = data[3:]
odds = [x for x in a if x % 2]
evens = [x for x in a if x % 2 == 0]
odd_groups = k - p
if len(odds) < odd_groups or (len(odds) - odd_groups) % 2 != 0:
    print('NO')
    sys.exit()
even_resources = len(evens) + (len(odds) - odd_groups) // 2
if even_resources < p:
    print('NO')
    sys.exit()
groups = []
for _ in range(odd_groups):
    groups.append([odds.pop()])
for _ in range(p):
    if evens:
        groups.append([evens.pop()])
    else:
        groups.append([odds.pop(), odds.pop()])
leftover = evens + odds
if leftover:
    groups[-1].extend(leftover)
print('YES')
for g in groups:
    print(len(g), *g)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
