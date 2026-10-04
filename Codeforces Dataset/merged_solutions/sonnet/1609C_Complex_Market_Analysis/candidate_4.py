# CLAUSE: setup_environment
import sys

def sieve(limit):
    mark = [False, False] + [True] * max(0, limit - 1)
    for v in range(2, int(limit ** 0.5) + 1):
        if mark[v]:
            for u in range(v * v, limit + 1, v):
                mark[u] = False
    return mark[:limit + 1]

# CLAUSE: solve_logic
def solve_case(n, e, a, prime):
    ans = 0
    for start in range(e):
        one_run = 0
        prime_left_choices = 0
        right_ones = 0
        active_prime = False

        for pos in range(start, n, e):
            val = a[pos]
            if val == 1:
                one_run += 1
                if active_prime:
                    right_ones += 1
            else:
                if active_prime:
                    ans += prime_left_choices * (right_ones + 1) - 1
                if prime[val]:
                    active_prime = True
                    prime_left_choices = one_run + 1
                    right_ones = 0
                else:
                    active_prime = False
                    prime_left_choices = 0
                    right_ones = 0
                one_run = 0

        if active_prime:
            ans += prime_left_choices * (right_ones + 1) - 1
    return ans

def run():
    values = list(map(int, sys.stdin.buffer.read().split()))
    q = values[0]
    cursor = 1
    cases = []
    bound = 0
    for _ in range(q):
        n = values[cursor]
        e = values[cursor + 1]
        cursor += 2
        a = values[cursor:cursor + n]
        cursor += n
        cases.append((n, e, a))
        bound = max(bound, *a)

    prime = sieve(bound)
    print("\n".join(str(solve_case(n, e, a, prime)) for n, e, a in cases))

# CLAUSE: finish_program
if __name__ == "__main__":
    run()
