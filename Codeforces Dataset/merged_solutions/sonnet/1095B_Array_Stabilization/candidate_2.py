# CLAUSE: setup_environment
n = int(input())
a = list(map(int, input().split()))

# CLAUSE: solve_logic
a.sort()
answer = 0 if n == 2 else min(a[-1] - a[1], a[-2] - a[0])

# CLAUSE: finish_program
print(answer)
