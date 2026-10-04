# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_arrays(values):
    limit = max(values)
    counts = [0] * (limit + 1)
    for value in values:
        counts[value] += 1
    running = 0
    prefix = [0] * (limit + 1)
    for value in range(1, limit + 1):
        running += counts[value]
        prefix[value] = running
    return limit, counts, prefix

def interval_count(prefix, left, right):
    return prefix[right] - prefix[left - 1]

def best_income(n, y, values):
    limit, counts, prefix = build_arrays(values)
    if limit == 1:
        return n

    answer = -10**30
    for divisor in range(2, limit + 1):
        total = 0
        reused = 0
        blocks = (limit + divisor - 1) // divisor
        for tag in range(1, blocks + 1):
            left = (tag - 1) * divisor + 1
            right = tag * divisor
            if right > limit:
                right = limit
            amount = interval_count(prefix, left, right)
            if amount:
                total += amount * tag
                if tag <= limit and counts[tag]:
                    reused += min(amount, counts[tag])
        value = total - y * (n - reused)
        answer = max(answer, value)
    return answer

def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    cases = items[0]
    at = 1
    answers = []
    for _ in range(cases):
        n, y = items[at], items[at + 1]
        at += 2
        current = items[at:at + n]
        at += n
        answers.append(str(best_income(n, y, current)))
    print("\n".join(answers))

# CLAUSE: finish_program
main()
