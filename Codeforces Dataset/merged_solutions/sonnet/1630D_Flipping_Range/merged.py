# Clause setup_environment [Confidence: 0.80]
import sys
from math import gcd


# Clause solve_logic [Confidence: 0.40]
def case_answer(n, m, values, moves):
    g = moves[0]
    for x in moves[1:]:
        g = gcd(g, x)

    groups = [[0, 10 ** 30] for _ in range(g)]
    total = sum(abs(x) for x in values)

    for index, value in enumerate(values):
        group = groups[index % g]
        if value < 0:
            group[0] = 1 - group[0]
            value = -value
        if value < group[1]:
            group[1] = value

    keep_even = total
    keep_odd = total
    for parity, low in groups:
        if parity:
            keep_even -= low + low
        else:
            keep_odd -= low + low

    return keep_even if keep_even > keep_odd else keep_odd


# Clause finish_program [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    answers = []
    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2
        values = data[p:p + n]
        p += n
        moves = data[p:p + m]
        p += m
        answers.append(str(case_answer(n, m, values, moves)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()


