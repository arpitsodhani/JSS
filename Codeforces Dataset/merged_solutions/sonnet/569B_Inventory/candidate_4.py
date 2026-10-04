# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    numbers = [int(item) for item in raw[1:1 + n]]
    first_positions = {}
    bad_positions = []
    for position in range(n):
        number = numbers[position]
        if number < 1 or number > n or number in first_positions:
            bad_positions.append(position)
        else:
            first_positions[number] = position
    absent = []
    for number in range(1, n + 1):
        if number not in first_positions:
            absent.append(number)
    for position in range(len(bad_positions)):
        numbers[bad_positions[position]] = absent[position]
    sys.stdout.write(" ".join(str(number) for number in numbers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
