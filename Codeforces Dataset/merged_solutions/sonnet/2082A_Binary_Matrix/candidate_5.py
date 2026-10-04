# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    items = iter(sys.stdin.buffer.read().split())
    t = int(next(items))
    answers = []

    for _ in range(t):
        n = int(next(items))
        m = int(next(items))
        column_parity = bytearray(m)
        rows_with_odd_xor = 0

        for _ in range(n):
            row = next(items)
            row_parity = 0

            for i, code in enumerate(row):
                bit = code & 1
                row_parity ^= bit
                column_parity[i] ^= bit

            rows_with_odd_xor += row_parity

        columns_with_odd_xor = 0
        for bit in column_parity:
            columns_with_odd_xor += bit

        answers.append(str(max(rows_with_odd_xor, columns_with_odd_xor)))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
