# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def reduce_pair(pair):
    a, b = pair
    if a == 0:
        return -1 if b == 0 else 0
    if b == 0:
        return 1

    moves = 0
    while True:
        if a == b:
            return (moves + 2) % 3
        if a < b:
            a, b = b, a
        quotient = a // b
        remainder = a % b
        if remainder == 0:
            return (moves + quotient + 1) % 3
        moves += quotient
        a, b = b, remainder


def solve():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    p = 0
    tests = data[p]
    p += 1
    answer = []

    for _ in range(tests):
        n = data[p]
        p += 1
        pairs = zip(data[p:p + n], data[p + n:p + 2 * n])
        p += 2 * n

        chosen = None
        good = True
        for pair in pairs:
            residue = reduce_pair(pair)
            if residue == -1:
                continue
            if chosen is None:
                chosen = residue
            elif chosen != residue:
                good = False
                break

        answer.append("YES" if good else "NO")

    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
