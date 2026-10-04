# CLAUSE: setup_environment
n = int(input())
values = list(map(int, input().split()))

# CLAUSE: solve_logic
ordered = sorted(values)
if n <= 2:
    result = 0
else:
    remove_smallest = ordered[-1] - ordered[1]
    remove_largest = ordered[-2] - ordered[0]
    result = remove_smallest if remove_smallest < remove_largest else remove_largest

# CLAUSE: finish_program
print(result)
