# CLAUSE: setup_environment
import sys
from math import gcd
from itertools import accumulate

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 1
    out = []
    for _ in range(data[0]):
        n = data[index]
        index += 1
        a = data[index:index + n]
        index += n
        total = sum(a)
        answer = max(gcd(part, total - part) for part in accumulate(a[:-1]))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
