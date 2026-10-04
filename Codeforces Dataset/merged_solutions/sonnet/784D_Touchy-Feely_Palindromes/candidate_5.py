# CLAUSE: setup_environment
s = input().strip()
allowed_pairs = {"00", "11", "33", "46", "64", "77", "88", "99"}

# CLAUSE: solve_logic
n = len(s)
checks = []
for i, ch in enumerate(s):
    checks.append(ch + s[n - 1 - i] in allowed_pairs)
verdict = "Yes" if all(checks) else "No"

# CLAUSE: finish_program
print(verdict)
