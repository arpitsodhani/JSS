# CLAUSE: setup_environment
n = int(input())

# CLAUSE: solve_logic
if n <= 2:
    answer = ["No"]
else:
    left = [n]
    right = list(range(1, n))
    answer = ["Yes", str(len(left)) + " " + " ".join(map(str, left)), str(len(right)) + " " + " ".join(map(str, right))]

# CLAUSE: finish_program
print("\n".join(answer))
