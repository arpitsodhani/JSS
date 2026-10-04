# CLAUSE: setup_environment
import sys

MOD = 10 ** 9 + 7

# CLAUSE: solve_logic
def build_inverses(size):
    inverse = [0] * (size + 1)
    inverse[1] = 1
    for number in range(2, size + 1):
        inverse[number] = (MOD - MOD // number) * inverse[MOD % number] % MOD
    return inverse

def contribution(fixed, edge, limit, inverse):
    begin = limit // fixed + 1
    if begin < 1:
        begin = 1
    total = 0
    for length in range(begin, edge):
        total += inverse[length + limit // length]
        if total >= MOD:
            total -= MOD
    return total

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    count = raw[0]
    tests = []
    max_size = 1

    for i in range(count):
        base = 1 + 3 * i
        n, m, k = raw[base], raw[base + 1], raw[base + 2]
        tests.append((n, m, k))
        max_size = max(max_size, n + m)

    inverse = build_inverses(max_size)
    answer_lines = []

    for n, m, k in tests:
        limit = k - 1
        if n * m <= limit:
            answer_lines.append("0")
        else:
            value = 1
            value += contribution(n, m, limit, inverse)
            if value >= MOD:
                value -= MOD
            value += contribution(m, n, limit, inverse)
            value %= MOD
            answer_lines.append(str(value))

    sys.stdout.write("\n".join(answer_lines))

# CLAUSE: finish_program
main()
