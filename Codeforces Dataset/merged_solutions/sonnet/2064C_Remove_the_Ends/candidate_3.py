# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def best_score(a):
    total_negative = sum(-x for x in a if x < 0)
    current = total_negative
    best = current
    for x in a:
        if x > 0:
            current += x
        else:
            current -= -x
        if current > best:
            best = current
    return best

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 1
    cases = data[0]
    result = []
    for _ in range(cases):
        n = data[index]
        index += 1
        a = data[index:index + n]
        index += n
        result.append(str(best_score(a)))
    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
