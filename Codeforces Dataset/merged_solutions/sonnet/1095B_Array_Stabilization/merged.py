# Clause setup_environment [Confidence: 0.80]
n = int(input())
a = list(map(int, input().split()))


# Clause solve_logic [Confidence: 0.20]
n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 2:
    print(0)
else:
    print(min(a[-1] - a[1], a[-2] - a[0]))


# Clause finish_program [Confidence: 0.80]
print(ans)


