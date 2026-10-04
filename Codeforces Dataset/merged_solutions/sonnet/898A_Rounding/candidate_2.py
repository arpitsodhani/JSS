# CLAUSE: setup_environment
n = int(input())

# CLAUSE: solve_logic
last = n % 10
if last <= 5:
    answer = n - last
else:
    answer = n + 10 - last

# CLAUSE: finish_program
print(answer)
