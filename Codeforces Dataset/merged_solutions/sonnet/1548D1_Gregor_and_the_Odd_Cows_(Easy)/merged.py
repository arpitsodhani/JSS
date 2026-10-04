# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    groups = [0, 0, 0, 0]
    p = 1
    for _ in range(n):
        x = int(tokens[p]) // 2
        y = int(tokens[p + 1]) // 2
        p += 2
        groups[((x & 1) << 1) | (y & 1)] += 1

    bad = 0
    for a in range(4):
        for b in range(a + 1, 4):
            for c in range(b + 1, 4):
                bad += groups[a] * groups[b] * groups[c]

    sys.stdout.write(str(comb(n, 3) - bad))


# Clause finish_program [Confidence: 0.40]
main()


