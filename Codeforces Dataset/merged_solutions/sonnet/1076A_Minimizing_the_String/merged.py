# Clause setup_environment [Confidence: 0.80]
n = int(input())
s = input().strip()


# Clause solve_logic [Confidence: 0.40]
cut = n - 1
for i in range(n - 1):
    if s[i] > s[i + 1]:
        cut = i
        break
answer = s[:cut] + s[cut + 1:]


# Clause finish_program [Confidence: 0.40]
print(answer)


