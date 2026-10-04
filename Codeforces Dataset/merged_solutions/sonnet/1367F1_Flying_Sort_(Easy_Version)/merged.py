# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def solve_case(n, a):
    ordered = sorted(a)
    rank = {}
    for i, value in enumerate(ordered):
        rank[value] = i
    positions = [0] * n
    for i, value in enumerate(a):
        positions[rank[value]] = i
    longest = 1
    run = 1
    for i in range(1, n):
        if positions[i - 1] < positions[i]:
            run += 1
        else:
            run = 1
        if run > longest:
            longest = run
    return n - longest

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    out = []
    for _ in range(t):
        n = int(data[p])
        p += 1
        a = [int(x) for x in data[p:p + n]]
        p += n
        out.append(str(solve_case(n, a)))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


