# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
