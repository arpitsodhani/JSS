# CLAUSE: setup_environment
n = int(input())
numbers = list(map(int, input().split()))

# CLAUSE: solve_logic
numbers.sort()
candidates = []
if n == 2:
    candidates.append(0)
else:
    for left, right in ((1, n - 1), (0, n - 2)):
        candidates.append(numbers[right] - numbers[left])
best = min(candidates)

# CLAUSE: finish_program
print(best)
