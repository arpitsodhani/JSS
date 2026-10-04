# CLAUSE: setup_environment
n, k = map(int, input().split())

# CLAUSE: solve_logic
diplomas = (n // 2) // (k + 1)
certificates = diplomas * k
others = n - diplomas - certificates

# CLAUSE: finish_program
print(diplomas, certificates, others)
