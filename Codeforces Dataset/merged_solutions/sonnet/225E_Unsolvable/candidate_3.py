# CLAUSE: setup_environment
import sys
from itertools import combinations

# CLAUSE: solve_logic
n = int(sys.stdin.read())
fermat = [3]
for _ in range(9):
    fermat.append((fermat[-1] - 1) * (fermat[-1] - 1) + 1)
answers = [1]
tail = fermat[1:]
for size in range(len(tail) + 1):
    for chosen in combinations(tail, size):
        product = fermat[0]
        for value in chosen:
            product *= value
        answers.append(product)
answers.sort()

# CLAUSE: finish_program
sys.stdout.write(str(answers[n - 1]))
