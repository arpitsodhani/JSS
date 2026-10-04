# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def choose2(x):
    return x * (x - 1) // 2

def choose3(x):
    return x * (x - 1) * (x - 2) // 6

def probability(n, k):
    total = choose3(n)
    value = 0.0
    if k >= 1 and n - k >= 2:
        value += k * choose2(n - k) * 0.5 / total
    if k >= 2 and n - k >= 1:
        value += choose2(k) * (n - k) / total
    if k >= 3:
        value += choose3(k) / total
    return value

# CLAUSE: finish_program
data = sys.stdin.read().split()
n = int(data[0])
p = float(data[1])
answer = 0
for studied in range(n + 1):
    if probability(n, studied) >= p - 1e-9:
        answer = studied
        break
print(answer)
