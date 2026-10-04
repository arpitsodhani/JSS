# CLAUSE: setup_environment
import sys
from itertools import permutations

MOD = 10**9 + 7

# CLAUSE: solve_logic
def anti_median(p):
    n = len(p)
    for i in range(n):
        r = 1
        border = min(i + 1, n - i)
        while r < border:
            s = p[i - r:i + r + 1]
            if sorted(s)[r] == p[i]:
                return False
            r += 1
    return True

def solve_one(n, fixed):
    present = [False] * (n + 1)
    blanks = []
    for i in range(n):
        if fixed[i] == -1:
            blanks.append(i)
        else:
            present[fixed[i]] = True
    choices = []
    for value in range(1, n + 1):
        if not present[value]:
            choices.append(value)
    if len(choices) != len(blanks):
        return 0
    ans = 0
    base = fixed[:]
    for order in permutations(choices):
        for i, pos in enumerate(blanks):
            base[pos] = order[i]
        if anti_median(base):
            ans += 1
    for pos in blanks:
        base[pos] = -1
    return ans % MOD

# CLAUSE: finish_program
def main():
    items = sys.stdin.read().strip().split()
    if not items:
        return
    t = int(items[0])
    index = 1
    output = []
    for _ in range(t):
        n = int(items[index])
        index += 1
        fixed = [int(items[index + j]) for j in range(n)]
        index += n
        output.append(str(solve_one(n, fixed)))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
