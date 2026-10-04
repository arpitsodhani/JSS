# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import gcd

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        sys.exit()

    n, m = data[0], data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + n + m]

    for i in range(n):
        x = a[i]
        if x == 1:
            continue
        for j in range(m):
            if x == 1:
                break
            g = gcd(x, b[j])
            if g > 1:
                x //= g
                b[j] //= g
        a[i] = x

    print(n, m)
    print(*a)
    print(*b)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
