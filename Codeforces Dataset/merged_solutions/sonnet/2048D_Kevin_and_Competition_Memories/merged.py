# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.80]
def ranks_for_problems(ratings, problems):
    kevin = ratings[0]
    stronger = []
    for r in ratings:
        if r > kevin:
            stronger.append(r)
    stronger.sort()
    penalties = []
    size = len(stronger)
    for d in problems:
        if d > kevin:
            beaten = size - bisect_left(stronger, d)
            if beaten:
                penalties.append(beaten)
    penalties.sort(reverse=True)
    return penalties

def answers_for_m(penalties, m):
    h = len(penalties)
    answers = []
    for group_size in range(1, m + 1):
        skipped = m % group_size
        if skipped > h:
            skipped = h
        s = m // group_size
        chosen = penalties[skipped::group_size]
        for value in chosen:
            s += value
        answers.append(str(s))
    return answers

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    cases = data[at]
    at += 1
    result = []
    for _ in range(cases):
        n = data[at]
        m = data[at + 1]
        at += 2
        ratings = data[at:at + n]
        at += n
        problems = data[at:at + m]
        at += m
        result.append(" ".join(answers_for_m(ranks_for_problems(ratings, problems), m)))
    sys.stdout.write("\n".join(result))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


