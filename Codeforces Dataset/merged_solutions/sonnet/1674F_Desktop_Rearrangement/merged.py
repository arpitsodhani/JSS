# Clause setup_environment [Confidence: 0.60]
import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    rows = [bytearray(data[i + 3]) for i in range(n)]
    size = n * m
    tree = [0] * (size + 1)
    total = 0

    def add(index, delta):
        while index <= size:
            tree[index] += delta
            index += index & -index

    def prefix(index):
        result = 0
        while index:
            result += tree[index]
            index -= index & -index
        return result


# Clause solve_logic [Confidence: 0.60]
    for i in range(n):
        row = rows[i]
        for j in range(m):
            if row[j] == 42:
                total += 1
                add(j * n + i + 1, 1)

    at = 3 + n
    answers = []
    for _ in range(q):
        x = int(data[at]) - 1
        y = int(data[at + 1]) - 1
        at += 2
        linear = y * n + x + 1
        if rows[x][y] == 42:
            rows[x][y] = 46
            total -= 1
            add(linear, -1)
        else:
            rows[x][y] = 42
            total += 1
            add(linear, 1)
        answers.append(str(total - prefix(total)))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


