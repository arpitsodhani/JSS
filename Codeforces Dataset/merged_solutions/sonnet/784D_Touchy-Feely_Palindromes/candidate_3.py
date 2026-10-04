# CLAUSE: setup_environment
s = input().strip()
valid = set("01346789")
mirror = str.maketrans("01346789", "01364789")

# CLAUSE: solve_logic
if all(ch in valid for ch in s):
    transformed = s.translate(mirror)[::-1]
    result = "Yes" if transformed == s else "No"
else:
    result = "No"

# CLAUSE: finish_program
print(result)
