# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def connect(board, u, v):
    board[u][v] = "Y"
    board[v][u] = "Y"

def make_graph(k):
    bits = [i for i in range(k.bit_length()) if (k >> i) & 1]

    if k == 1:
        return 2, ["NY", "YN"]

    last = k.bit_length() - 1
    n = 2 * last + 2
    board = [["N" for _ in range(n)] for _ in range(n)]

    for layer in range(last):
        left = [0] if layer == 0 else [2 * layer, 2 * layer + 1]
        right = [2 * (layer + 1), 2 * (layer + 1) + 1]
        for u in left:
            for v in right:
                connect(board, u, v)

    for bit in bits:
        if bit == 0:
            connect(board, 0, 1)
        else:
            connect(board, 2 * bit, 1)

    return n, ["".join(row) for row in board]

# CLAUSE: finish_program
def main():
    k = int(sys.stdin.buffer.readline())
    n, rows = make_graph(k)
    sys.stdout.write(str(n) + "\n" + "\n".join(rows))

if __name__ == "__main__":
    main()
