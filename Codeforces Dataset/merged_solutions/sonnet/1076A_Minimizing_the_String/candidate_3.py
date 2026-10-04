# CLAUSE: setup_environment
n = int(input())
s = input().strip()

# CLAUSE: solve_logic
cut = n - 1
i = 0
while i + 1 < n:
    if s[i] > s[i + 1]:
        cut = i
        i = n
    else:
        i += 1
parts = [s[:cut], s[cut + 1:]]

# CLAUSE: finish_program
print("".join(parts))
