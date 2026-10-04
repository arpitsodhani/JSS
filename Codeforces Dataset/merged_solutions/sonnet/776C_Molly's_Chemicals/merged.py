# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    arr = data[2:2 + n]

    if k == 1:
        powers = [1]
    elif k == -1:
        powers = [1, -1]
    elif k == 0:
        powers = [1, 0]
    else:
        powers = []
        cur = 1
        while abs(cur) <= 10 ** 15:
            powers.append(cur)
            cur *= k

    seen = defaultdict(int)
    seen[0] = 1
    total = 0
    pref = 0

    for value in arr:
        pref += value
        for target in powers:
            total += seen[pref - target]
        seen[pref] += 1

    sys.stdout.write(str(total))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


