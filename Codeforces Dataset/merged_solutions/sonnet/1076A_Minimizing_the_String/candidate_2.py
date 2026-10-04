# CLAUSE: setup_environment
n = int(input())
s = input().strip()

# CLAUSE: solve_logic
cut = n - 1
for i in range(n - 1):
    if s[i] > s[i + 1]:
        cut = i
        break
answer = s[:cut] + s[cut + 1:]

# CLAUSE: finish_program
print(answer)
