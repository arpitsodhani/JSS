# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())

    is_prime = [True] * (n + 1)
    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

    used = [False] * (n + 1)
    ans = []

    for p in reversed(primes):
        if p * 2 > n:
            continue

        v = []
        for x in range(p, n + 1, p):
            if not used[x]:
                v.append(x)

        if len(v) % 2 == 1:
            leave = 2 * p
            v.remove(leave)

        for i in range(0, len(v), 2):
            a, b = v[i], v[i + 1]
            used[a] = True
            used[b] = True
            ans.append((a, b))

    print(len(ans))
    for a, b in ans:
        print(a, b)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
