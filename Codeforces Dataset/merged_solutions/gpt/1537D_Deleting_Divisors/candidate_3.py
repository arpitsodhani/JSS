# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r = int(math.isqrt(x))
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True

    def winner(n):
        if n == 1 or n % 2 == 1:
            return "Bob"
        if n == 2:
            return "Bob"

        m = n
        twos = 0
        while m % 2 == 0:
            twos += 1
            m //= 2

        if m == 1:
            return "Alice" if twos % 2 == 1 else "Bob"

        if twos > 1:
            return "Alice"

        return "Bob" if is_prime(m) else "Alice"

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    for i in range(1, t + 1):
        ans.append(winner(int(data[i])))
    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
