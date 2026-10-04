# Clause setup_environment [Confidence: 0.60]
n = int(input())


# Clause solve_logic [Confidence: 0.20]
last = n % 10
if last <= 5:
    answer = n - last
else:
    answer = n + 10 - last


# Clause finish_program [Confidence: 0.60]
print(answer)


