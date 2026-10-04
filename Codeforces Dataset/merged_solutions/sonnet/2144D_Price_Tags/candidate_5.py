# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def calculate(n, y, prices):
    maximum = 0
    occurrences = {}
    for price in prices:
        maximum = max(maximum, price)
        occurrences[price] = occurrences.get(price, 0) + 1

    if maximum == 1:
        return n

    prefix = [0] * (maximum + 1)
    for price, amount in occurrences.items():
        prefix[price] = amount
    for price in range(1, maximum + 1):
        prefix[price] += prefix[price - 1]

    best = -10**30
    for x in range(2, maximum + 1):
        earned = 0
        kept = 0
        tag = 1
        start = 1
        while start <= maximum:
            stop = min(maximum, start + x - 1)
            cnt = prefix[stop] - prefix[start - 1]
            if cnt:
                earned += cnt * tag
                old = occurrences.get(tag, 0)
                if old:
                    kept += min(old, cnt)
            start += x
            tag += 1
        score = earned - y * (n - kept)
        if score > best:
            best = score
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pointer = 1
    answers = []
    for _ in range(data[0]):
        n = data[pointer]
        y = data[pointer + 1]
        pointer += 2
        segment = data[pointer:pointer + n]
        pointer += n
        answers.append(str(calculate(n, y, segment)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
