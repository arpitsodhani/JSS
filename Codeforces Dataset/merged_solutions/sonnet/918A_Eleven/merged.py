import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause fibonacci_upto [Confidence: 1.00]
def fibonacci_upto(n):
    marks = set()
    previous = 1
    current = 1
    while previous <= n:
        marks.add(previous)
        previous, current = current, previous + current
    return marks

# Clause build_name [Confidence: 1.00]
def build_name(n, marks):
    letters = []
    for i in range(1, n + 1):
        letters.append("O" if i in marks else "o")
    return "".join(letters)

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    sys.stdout.write(build_name(n, fibonacci_upto(n)) + "\n")


if __name__ == "__main__":
    main()

