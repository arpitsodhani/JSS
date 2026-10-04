# CLAUSE: setup_environment
n, k = [int(x) for x in input().split()]

# CLAUSE: solve_logic
winners = (n // 2) // (k + 1) * (k + 1)
diplomas = winners // (k + 1)
certificates = winners - diplomas
others = n - winners

# CLAUSE: finish_program
print(diplomas, certificates, others)
