# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    counts = {}
    maximum = 0
    for token in data[1:1 + n]:
        length = int(token)
        counts[length] = counts.get(length, 0) + 1
        if counts[length] > maximum:
            maximum = counts[length]
    answer = (maximum, len(counts))

# CLAUSE: finish_program
    sys.stdout.write(f"{answer[0]} {answer[1]}")

if __name__ == "__main__":
    main()
