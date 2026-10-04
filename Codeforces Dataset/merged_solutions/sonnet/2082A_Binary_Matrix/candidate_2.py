# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    pos = 0
    tests = int(tokens[pos])
    pos += 1
    result = []

    for _ in range(tests):
        n = int(tokens[pos])
        m = int(tokens[pos + 1])
        pos += 2

        odd_rows = 0
        odd_cols = [0] * m

        for _ in range(n):
            row = tokens[pos]
            pos += 1
            row_xor = 0

            for j in range(m):
                value = 1 if row[j] == "1" else 0
                row_xor ^= value
                odd_cols[j] ^= value

            odd_rows += row_xor

        result.append(str(max(odd_rows, sum(odd_cols))))

    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
