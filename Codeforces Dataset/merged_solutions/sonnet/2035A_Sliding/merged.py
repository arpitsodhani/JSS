# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = sys.stdin.buffer.read().split()
    total = int(data[0])
    lines = []
    index = 1
    while total:
        n = int(data[index])
        m = int(data[index + 1])
        r = int(data[index + 2])
        c = int(data[index + 3])
        index += 4
        total -= 1
        leaving_number = (r - 1) * m + c
        shifted_people = n * m - leaving_number
        row_wraps = n - r
        lines.append(str(shifted_people + row_wraps * (m - 1)))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


