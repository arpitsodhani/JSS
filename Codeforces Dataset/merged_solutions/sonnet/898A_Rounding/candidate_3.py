# CLAUSE: setup_environment
value = input().strip()

# CLAUSE: solve_logic
n = int(value)
digit = int(value[-1])
down = n - digit
up = down + 10
answer = down if digit <= 5 else up

# CLAUSE: finish_program
print(answer)
