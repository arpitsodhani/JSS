# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def rect_sum(flat, width, r1, c1, r2, c2):
    return flat[r2 * width + c2] - flat[(r1 - 1) * width + c2] - flat[r2 * width + c1 - 1] + flat[(r1 - 1) * width + c1 - 1]

def main():
    tokens = sys.stdin.buffer.read().split()
    it = iter(tokens)

    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    width = m + 1
    size = (n + 1) * width

    garlands = []
    for _ in range(k):
        count = int(next(it))
        table = array("q", [0]) * size
        for _ in range(count):
            r = int(next(it))
            c = int(next(it))
            value = int(next(it))
            table[r * width + c] = value

        for r in range(1, n + 1):
            base = r * width
            above = base - width
            running = 0
            for c in range(1, m + 1):
                pos = base + c
                running += table[pos]
                table[pos] = running + table[above + c]
        garlands.append(table)

    q = int(next(it))
    enabled = [True] * k
    out = []

    for _ in range(q):
        command = next(it)
        if command[0] == 83:
            idx = int(next(it)) - 1
            enabled[idx] = not enabled[idx]
        else:
            r1 = int(next(it))
            c1 = int(next(it))
            r2 = int(next(it))
            c2 = int(next(it))
            answer = 0
            for idx, flat in enumerate(garlands):
                if enabled[idx]:
                    answer += rect_sum(flat, width, r1, c1, r2, c2)
            out.append(str(answer))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
main()
