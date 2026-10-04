# Clause setup_environment [Confidence: 0.40]
s = input().strip()
same = {"0", "1", "3", "7", "8", "9"}
opposite = {("4", "6"), ("6", "4")}


# Clause solve_logic [Confidence: 0.20]
answer = "Yes"
for left in range(len(s)):
    right = len(s) - 1 - left
    if s[left] not in rotates or rotates[s[left]] != s[right]:
        answer = "No"
        break


# Clause finish_program [Confidence: 0.60]
print(answer)


