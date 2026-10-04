# CLAUSE: setup_environment
n = int(input())

# CLAUSE: solve_logic
if n <= 2:
    result = "No"
else:
    numbers = tuple(range(1, n))
    second_line = "1 " + str(n)
    third_line = str(len(numbers))
    for item in numbers:
        third_line += " " + str(item)
    result = "Yes\n" + second_line + "\n" + third_line

# CLAUSE: finish_program
print(result)
