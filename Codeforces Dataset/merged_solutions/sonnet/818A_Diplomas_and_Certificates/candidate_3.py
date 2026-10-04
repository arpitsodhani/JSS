# CLAUSE: setup_environment
values = input().split()
n = int(values[0])
k = int(values[1])

# CLAUSE: solve_logic
limit = n // 2
group_size = k + 1
diplomas = limit // group_size
certificates = k * diplomas
others = n - (diplomas + certificates)

# CLAUSE: finish_program
print("{} {} {}".format(diplomas, certificates, others))
