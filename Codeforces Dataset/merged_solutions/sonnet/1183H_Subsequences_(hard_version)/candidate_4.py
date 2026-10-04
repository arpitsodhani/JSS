# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.buffer.read().split()
    n, k = map(int, parts[:2])
    chars = [x - 97 for x in parts[2]]

    counts = [0] * (n + 1)
    counts[0] = 1
    previous = [[0] * 26 for _ in range(n + 1)]

    for index, code in enumerate(chars):
        for length in range(index + 1, 0, -1):
            value = counts[length - 1]
            counts[length] += value - previous[length][code]
            previous[length][code] = value

    answer = 0
    for length, amount in reversed(list(enumerate(counts))):
        chosen = amount if amount < k else k
        answer += chosen * (n - length)
        k -= chosen
        if k == 0:
            sys.stdout.write(str(answer))
            return

    sys.stdout.write("-1")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
