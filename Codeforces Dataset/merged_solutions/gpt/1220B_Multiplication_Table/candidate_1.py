# CLAUSE: setup_environment
import sys
from math import isqrt

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = []
    idx = 1
    for _ in range(n):
        row = list(map(int, data[idx:idx + n]))
        idx += n
        m.append(row)

    a0 = isqrt(m[0][1] * m[0][2] // m[1][2])
    ans = [a0]
    for i in range(1, n):
        ans.append(m[0][i] // a0)

    print(*ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
