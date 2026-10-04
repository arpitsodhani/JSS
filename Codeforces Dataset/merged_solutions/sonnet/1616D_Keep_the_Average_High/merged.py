# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    ans = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        a = [int(tokens[pos + i]) for i in range(n)]
        pos += n
        x = int(tokens[pos])
        pos += 1

        removed = 0
        last_removed = -10

        for i in range(n):
            if i >= 1 and last_removed != i - 1 and a[i] + a[i - 1] < 2 * x:
                removed += 1
                last_removed = i
                continue
            if i >= 2 and last_removed != i - 1 and last_removed != i - 2 and a[i] + a[i - 1] + a[i - 2] < 3 * x:
                removed += 1
                last_removed = i

        ans.append(str(n - removed))
    sys.stdout.write("\n".join(ans))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


