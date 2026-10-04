# CLAUSE: setup_environment
n = int(input())
s = input().strip()

# CLAUSE: solve_logic
chars = list(s)
cut = n - 1
for i, ch in enumerate(chars[:-1]):
    if ch > chars[i + 1]:
        cut = i
        break
del chars[cut]

# CLAUSE: finish_program
print("".join(chars))
