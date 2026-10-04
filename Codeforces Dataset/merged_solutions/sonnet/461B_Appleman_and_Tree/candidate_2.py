# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    children = [[] for _ in range(n)]
    pos = 1
    for v in range(1, n):
        p = data[pos]
        pos += 1
        children[p].append(v)
    color = data[pos:pos + n]

    order = [0]
    for v in order:
        order += children[v]

    dp0 = [0] * n
    dp1 = [0] * n

    for v in order[::-1]:
        if color[v]:
            zero = 0
            one = 1
        else:
            zero = 1
            one = 0
        for c in children[v]:
            total = dp0[c] + dp1[c]
            zero, one = zero * total % MOD, (one * total + zero * dp1[c]) % MOD
        dp0[v] = zero
        dp1[v] = one

    sys.stdout.write(str(dp1[0] % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
