# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def prepare(limit):
    factorials = [1] * (limit + 1)
    for i in range(limit):
        factorials[i + 1] = factorials[i] * (i + 1) % MOD

    inverse_factorials = [1] * (limit + 1)
    inverse_factorials[limit] = pow(factorials[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inverse_factorials[i - 1] = inverse_factorials[i] * i % MOD

    return factorials, inverse_factorials

def comb(n, r, factorials, inverse_factorials):
    if r < 0 or r > n:
        return 0
    return factorials[n] * inverse_factorials[r] % MOD * inverse_factorials[n - r] % MOD

def solve_case(k, ones, zeros, factorials, inverse_factorials):
    needed = k // 2 + 1
    start = max(needed, k - zeros)
    stop = min(k, ones)
    answer = 0

    current = start
    while current <= stop:
        answer = (answer + comb(ones, current, factorials, inverse_factorials) * comb(zeros, k - current, factorials, inverse_factorials)) % MOD
        current += 1

    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    cases = []
    max_seen = 0

    for _ in range(t):
        n = data[ptr]
        k = data[ptr + 1]
        ptr += 2
        ones = 0
        for value in data[ptr:ptr + n]:
            ones += value
        ptr += n
        cases.append((k, ones, n - ones))
        max_seen = max(max_seen, n)

    factorials, inverse_factorials = prepare(max_seen)
    output = []

    for k, ones, zeros in cases:
        output.append(str(solve_case(k, ones, zeros, factorials, inverse_factorials)))

    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
