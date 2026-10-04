# CLAUSE: setup_environment
import sys

def xor_prefix(n):
    if n < 0:
        return 0
    rem = n & 3
    if rem == 0:
        return n
    if rem == 1:
        return 1
    if rem == 2:
        return n + 1
    return 0

def excluded_prefix(n, i, k):
    if n < k:
        return 0
    step = 1 << i
    q = (n - k) // step
    value = xor_prefix(q) << i
    if (q + 1) & 1:
        value ^= k
    return value

# CLAUSE: solve_logic
def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    pos = 1
    out = []
    for _ in range(t):
        l, r, i, k = values[pos], values[pos + 1], values[pos + 2], values[pos + 3]
        pos += 4
        all_xor = xor_prefix(r) ^ xor_prefix(l - 1)
        bad_xor = excluded_prefix(r, i, k) ^ excluded_prefix(l - 1, i, k)
        out.append(str(all_xor ^ bad_xor))
    return "\n".join(out)

# CLAUSE: finish_program
if __name__ == "__main__":
    sys.stdout.write(solve())
