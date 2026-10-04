# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def enough(prefix, n, need, step, residue_limit):
    count = 0
    for start in range(0, n + 1, step):
        stop = start + residue_limit
        if stop > n:
            stop = n
        if start:
            count += prefix[stop] - prefix[start - 1]
        else:
            count += prefix[stop]
        if count >= need:
            return True
    return False

def compute_answers(n, values, queries):
    frequency = [0] * (n + 1)
    for value in values:
        frequency[value] += 1

    running = 0
    prefix = []
    for amount in frequency:
        running += amount
        prefix.append(running)

    need = (n + 2) // 2
    answers = {}

    for x in sorted(set(queries)):
        lo = 0
        hi = x - 1
        while lo < hi:
            middle = (lo + hi) >> 1
            if enough(prefix, n, need, x, middle):
                hi = middle
            else:
                lo = middle + 1
        answers[x] = lo

    return answers

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 1
    output = []
    for _ in range(data[0]):
        n = data[cursor]
        q = data[cursor + 1]
        cursor += 2
        values = data[cursor:cursor + n]
        cursor += n
        queries = data[cursor:cursor + q]
        cursor += q
        answers = compute_answers(n, values, queries)
        output.append(" ".join(str(answers[x]) for x in queries))
    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
main()
