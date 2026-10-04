# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    n, m, q = map(int, tokens[:3])
    columns = [[0] * n for _ in range(m)]
    occupied = 0
    limit = n * m
    bit = [0] * (limit + 1)

    def update(pos, value):
        while pos <= limit:
            bit[pos] += value
            pos += pos & -pos

    def count_until(pos):
        acc = 0
        while pos > 0:
            acc += bit[pos]
            pos &= pos - 1
        return acc

# CLAUSE: solve_logic
    k = 3
    for r in range(n):
        line = tokens[k]
        k += 1
        for c, char in enumerate(line):
            if char == 42:
                columns[c][r] = 1
                occupied += 1
                update(c * n + r + 1, 1)

    result = []
    for k in range(k, k + 2 * q, 2):
        r = int(tokens[k]) - 1
        c = int(tokens[k + 1]) - 1
        pos = c * n + r + 1
        if columns[c][r]:
            columns[c][r] = 0
            occupied -= 1
            update(pos, -1)
        else:
            columns[c][r] = 1
            occupied += 1
            update(pos, 1)
        result.append(str(occupied - count_until(occupied)))

# CLAUSE: finish_program
    print("\n".join(result))

if __name__ == "__main__":
    main()
