# CLAUSE: setup_environment
data = tuple(map(int, input().split()))
n = data[0]
k = data[1]

# CLAUSE: solve_logic
counts = [0, 0, n]
counts[0] = n // (2 * (k + 1))
counts[1] = counts[0] * k
counts[2] = n - counts[0] - counts[1]

# CLAUSE: finish_program
print(*counts)
