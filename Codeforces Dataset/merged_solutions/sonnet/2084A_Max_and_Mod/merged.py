import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return data[1:1 + t]

# Clause solve_case [Confidence: 1.00]
def solve_case(n):
    if n % 2 == 1:
        row = [str(n)]
        for v in range(1, n):
            row.append(str(v))
        return " ".join(row)
    return "-1"

# Clause main [Confidence: 1.00]
def main():
    cases = read_input()
    answers = []
    for n in cases:
        answers.append(solve_case(n))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()

