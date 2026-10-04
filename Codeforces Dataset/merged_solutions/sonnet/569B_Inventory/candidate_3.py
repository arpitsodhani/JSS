# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def rebuild(n, values):
    count = [0] * (n + 1)
    for value in values:
        if 1 <= value <= n:
            count[value] += 1
    missing = iter(i for i in range(1, n + 1) if count[i] == 0)
    result = []
    kept = [False] * (n + 1)
    for value in values:
        if 1 <= value <= n and count[value] > 0 and not kept[value]:
            kept[value] = True
            result.append(value)
        else:
            result.append(next(missing))
    return result

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    values = [int(x) for x in tokens[1:1 + n]]
    answer = rebuild(n, values)
    print(*answer)

# CLAUSE: finish_program
main()
