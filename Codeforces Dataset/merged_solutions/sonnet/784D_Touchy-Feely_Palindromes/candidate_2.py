# CLAUSE: setup_environment
s = input().strip()
rotates = {"0": "0", "1": "1", "3": "3", "4": "6", "6": "4", "7": "7", "8": "8", "9": "9"}

# CLAUSE: solve_logic
answer = "Yes"
for left in range(len(s)):
    right = len(s) - 1 - left
    if s[left] not in rotates or rotates[s[left]] != s[right]:
        answer = "No"
        break

# CLAUSE: finish_program
print(answer)
