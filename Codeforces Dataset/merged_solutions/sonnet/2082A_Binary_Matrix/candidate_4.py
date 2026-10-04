# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(rows, m):
    row_need = 0
    col_mask = [False] * m

    for row in rows:
        parity = False
        for j, ch in enumerate(row):
            if ch == "1":
                parity = not parity
                col_mask[j] = not col_mask[j]
        row_need += parity

    col_need = sum(1 for value in col_mask if value)
    return max(row_need, col_need)

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ptr = 1
    out = []

    for _ in range(t):
        n = int(data[ptr])
        m = int(data[ptr + 1])
        ptr += 2

        rows = []
        for _ in range(n):
            rows.append(data[ptr].decode())
            ptr += 1

        out.append(str(solve_case(rows, m)))

    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
