# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    pos = 1
    result = []
    seen = [False] * (n + 1)

    for _ in range(n):
        best = 0
        for value in values[pos:pos + n]:
            if value > best:
                best = value
        pos += n
        result.append(best)
        if best:
            seen[best] = True

    missing = 1
    while seen[missing]:
        missing += 1

    replaced = False
    used = [0] * (n + 1)
    for i, value in enumerate(result):
        used[value] += 1
        if value and used[value] == 2 and not replaced:
            result[i] = missing
            replaced = True

    sys.stdout.write(" ".join(map(str, result)))


# Clause finish_program [Confidence: 0.80]
main()


