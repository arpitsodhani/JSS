# Clause setup_environment [Confidence: 0.40]
n = int(input())


# Clause solve_logic [Confidence: 0.40]
if n <= 2:
    result = "No"
else:
    numbers = tuple(range(1, n))
    second_line = "1 " + str(n)
    third_line = str(len(numbers))
    for item in numbers:
        third_line += " " + str(item)
    result = "Yes\n" + second_line + "\n" + third_line


# Clause finish_program [Confidence: 0.40]
print("\n".join(answer))


