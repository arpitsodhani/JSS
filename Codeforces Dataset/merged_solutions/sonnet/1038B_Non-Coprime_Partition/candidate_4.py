# CLAUSE: setup_environment
def make_partition(limit):
    single = [limit]
    rest = [number for number in range(1, limit)]
    return single, rest

n = int(input())

# CLAUSE: solve_logic
possible = n > 2
lines = ["No"]
if possible:
    first, second = make_partition(n)
    lines = [
        "Yes",
        "{} {}".format(len(first), " ".join(str(x) for x in first)),
        "{} {}".format(len(second), " ".join(str(x) for x in second)),
    ]

# CLAUSE: finish_program
for line in lines:
    print(line)
