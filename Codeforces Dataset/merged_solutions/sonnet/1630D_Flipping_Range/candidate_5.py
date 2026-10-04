# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
class FastReader:
    def __init__(self):
        self.data = sys.stdin.buffer.read().split()
        self.pos = 0

    def next_int(self):
        value = int(self.data[self.pos])
        self.pos += 1
        return value

def solve(reader):
    n = reader.next_int()
    m = reader.next_int()

    values = []
    total = 0
    for _ in range(n):
        x = reader.next_int()
        values.append(x)
        total += abs(x)

    g = 0
    for _ in range(m):
        g = gcd(g, reader.next_int())

    parity = bytearray(g)
    minimum = [10 ** 30] * g

    r = 0
    for x in values:
        y = abs(x)
        if x < 0:
            parity[r] ^= 1
        if y < minimum[r]:
            minimum[r] = y
        r += 1
        if r == g:
            r = 0

    same_zero = total
    same_one = total
    for i in range(g):
        if parity[i]:
            same_zero -= 2 * minimum[i]
        else:
            same_one -= 2 * minimum[i]

    return same_zero if same_zero >= same_one else same_one

# CLAUSE: finish_program
def main():
    reader = FastReader()
    t = reader.next_int()
    answers = [str(solve(reader)) for _ in range(t)]
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
