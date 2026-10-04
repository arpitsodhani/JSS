# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    p = [0] + data[1:1 + n]
    visited = [False] * (n + 1)
    lengths = []

    for i in range(1, n + 1):
        if not visited[i]:
            cur = i
            length = 0
            while not visited[cur]:
                visited[cur] = True
                length += 1
                cur = p[cur]
            lengths.append(length)

    lengths.sort(reverse=True)
    if len(lengths) > 1:
        lengths[0] += lengths[1]
        del lengths[1]

    sys.stdout.write(str(sum(length * length for length in lengths)))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


