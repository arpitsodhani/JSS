# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    MOD = 10**9 + 7

    def first_divisible_index(k):
        if k == 1:
            return 1
        a = 1 % k
        b = 1 % k
        for i in range(3, 10 * k + 10):
            a, b = b, (a + b) % k
            if b == 0:
                return i

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        ans = []
        p = 1
        for _ in range(t):
            n = data[p]
            k = data[p + 1]
            p += 2
            z = first_divisible_index(k)
            ans.append(str((n % MOD) * (z % MOD) % MOD))
        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
