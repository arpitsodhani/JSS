# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.buffer.read()
    parts = data.split()
    if not parts:
        return
    n = int(parts[0])
    m = int(parts[1])
    k = int(parts[2])
    s = b"".join(parts[3:])

    row_prefix = [[0] * (m + 1) for _ in range(n)]
    index = 0
    for r in range(n):
        row = row_prefix[r]
        running = 0
        for c in range(m):
            running += s[index] - 48
            row[c + 1] = running
            index += 1

    total_answer = 0
    for left in range(m):
        for right in range(left + 1, m + 1):
            prefix = 0
            stored = {0: 1}
            for r in range(n):
                prefix += row_prefix[r][right] - row_prefix[r][left]
                total_answer += stored.get(prefix - k, 0)
                stored[prefix] = stored.get(prefix, 0) + 1

    sys.stdout.write(str(total_answer))

# CLAUSE: finish_program
solve()
