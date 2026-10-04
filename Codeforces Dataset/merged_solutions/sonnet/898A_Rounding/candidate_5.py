# CLAUSE: setup_environment
number = int(input())

# CLAUSE: solve_logic
base = number // 10 * 10
offset = number - base
answer = base
if offset > 5:
    answer = base + 10

# CLAUSE: finish_program
print(answer)
