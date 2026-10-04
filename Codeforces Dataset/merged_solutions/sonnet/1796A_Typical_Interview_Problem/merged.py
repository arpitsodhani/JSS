import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    words = []
    for _ in range(t):
        pos += 1
        words.append(data[pos].decode())
        pos += 1
    return words

# Clause build_fb [Confidence: 1.00]
def build_fb(limit):
    chars = []
    for value in range(1, limit + 1):
        if value % 3 == 0:
            chars.append("F")
        if value % 5 == 0:
            chars.append("B")
    return "".join(chars)

# Clause solve_case [Confidence: 1.00]
def solve_case(word, table):
    if word in table:
        return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    table = build_fb(300)
    answers = []
    for word in read_input():
        answers.append(solve_case(word, table))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()

