# Clause setup_environment [Confidence: 0.40]
values = input().split()
n = int(values[0])
k = int(values[1])


# Clause solve_logic [Confidence: 0.40]
diplomas = (n // 2) // (k + 1)
certificates = diplomas * k
others = n - diplomas - certificates


# Clause finish_program [Confidence: 0.40]
print(diplomas, certificates, others)


