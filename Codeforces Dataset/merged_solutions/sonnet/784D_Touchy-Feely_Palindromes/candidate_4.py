# CLAUSE: setup_environment
s = input().strip()
same = {"0", "1", "3", "7", "8", "9"}
opposite = {("4", "6"), ("6", "4")}

# CLAUSE: solve_logic
left = 0
right = len(s) - 1
possible = True
while left <= right:
    a = s[left]
    b = s[right]
    if not ((a == b and a in same) or ((a, b) in opposite)):
        possible = False
        break
    left += 1
    right -= 1

# CLAUSE: finish_program
print("Yes" if possible else "No")
