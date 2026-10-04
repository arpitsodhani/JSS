# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def solve_one(tokens, pos):
    n = int(tokens[pos])
    m = int(tokens[pos + 1])
    pos += 2
    arr = [int(x) for x in tokens[pos:pos + n]]
    pos += n

    step = 0
    for _ in range(m):
        step = gcd(step, int(tokens[pos]))
        pos += 1

    total = 0
    odd = [0] * step
    smallest = [10 ** 30] * step

    for i in range(n):
        value = arr[i]
        av = value if value >= 0 else -value
        total += av
        r = i % step
        if value < 0:
            odd[r] ^= 1
        if av < smallest[r]:
            smallest[r] = av

    best = -10 ** 40
    for wanted in range(2):
        score = total
        for r in range(step):
            if odd[r] != wanted:
                score -= 2 * smallest[r]
        if score > best:
            best = score

    return best, pos

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 1
    out = []
    for _ in range(int(tokens[0])):
        ans, pos = solve_one(tokens, pos)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
