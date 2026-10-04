# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    pointer = 0
    n, m, q = map(int, tokens[pointer:pointer + 3])
    pointer += 3

    by_letter = [[0] * m for _ in range(26)]

    for row in range(n):
        row_data = tokens[pointer]
        pointer += 1
        marker = 1 << row
        col = 0
        for code in row_data:
            by_letter[code - 97][col] |= marker
            col += 1

    output = []
    for _ in range(q):
        query = tokens[pointer]
        pointer += 1

        possible = by_letter[query[0] - 97][0]
        if not possible:
            output.append("-1")
            continue

        shifts = 0
        col = 1
        while col < m:
            nxt = by_letter[query[col] - 97][col]
            if not nxt:
                shifts = -1
                break
            both = possible & nxt
            if both:
                possible = both
            else:
                shifts += 1
                possible = nxt
            col += 1

        output.append(str(shifts))

    print("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
