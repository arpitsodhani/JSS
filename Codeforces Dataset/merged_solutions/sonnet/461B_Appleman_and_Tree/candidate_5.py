# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[int(raw[i])].append(i)

    color_start = n
    zero = [1] * n
    one = [0] * n

    for i in range(n):
        if int(raw[color_start + i]) == 1:
            zero[i] = 0
            one[i] = 1

    for parent in range(n - 1, -1, -1):
        z = zero[parent]
        o = one[parent]
        for child in children[parent]:
            child_total = (zero[child] + one[child]) % MOD
            z, o = z * child_total % MOD, (o * child_total + z * one[child]) % MOD
        zero[parent] = z
        one[parent] = o

    sys.stdout.write("%d\n" % (one[0] % MOD))

# CLAUSE: finish_program
main()
