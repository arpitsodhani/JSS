# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def classify(position, n, left, right, both):
    if position <= left:
        return "-"
    if position > n - right:
        return "-"
    if position <= left + both:
        return "?"
    if position > n - right - both:
        return "?"
    return "+"

def main():
    values = sys.stdin.read().strip().split()
    if not values:
        return

    total = int(values[0])
    cursor = 1
    lines = []

    for _ in range(total):
        n = int(values[cursor])
        k = int(values[cursor + 1])
        moves = values[cursor + 2]
        cursor += 3

        zeros = ones = twos = 0
        for move in moves:
            if move == "0":
                zeros += 1
            elif move == "1":
                ones += 1
            else:
                twos += 1

        line = "".join(classify(i, n, zeros, ones, twos) for i in range(1, n + 1))
        lines.append(line)

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
