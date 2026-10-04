# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def get_residue(a, b):
    if a == 0 and b == 0:
        return -1
    if a == 0:
        return 0
    if b == 0:
        return 1

    count = 0
    while a != b:
        if a < b:
            a, b = b, a
        q, r = divmod(a, b)
        if r == 0:
            count += q - 1
            break
        count += q
        a, b = b, r
    return (count + 2) % 3


def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = values[pos]
    pos += 1
    out = []

    for _ in range(t):
        n = values[pos]
        pos += 1
        a = values[pos:pos + n]
        pos += n
        b = values[pos:pos + n]
        pos += n

        target = -1
        possible = True

        for x, y in zip(a, b):
            cur = get_residue(x, y)
            if cur == -1:
                continue
            if target == -1:
                target = cur
            elif cur != target:
                possible = False
                break

        out.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
solve()


