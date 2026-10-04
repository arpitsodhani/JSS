# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def triples(x):
    if x < 3:
        return 0
    return x * (x - 1) * (x - 2) // 6

def pairs(x):
    if x < 2:
        return 0
    return x * (x - 1) // 2

def scaled_success(n, k):
    other = n - k
    only_one = k * pairs(other)
    two_or_more = 2 * pairs(k) * other + 2 * triples(k)
    return only_one + two_or_more

def find_answer(n, p):
    denominator = 2 * triples(n)
    k = 0
    while k <= n:
        if scaled_success(n, k) / denominator >= p - 1e-9:
            return k
        k += 1
    return n

# CLAUSE: finish_program
items = sys.stdin.buffer.read().split()
n = int(items[0])
p = float(items[1])
sys.stdout.write(str(find_answer(n, p)) + "\n")
