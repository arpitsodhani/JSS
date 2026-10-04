# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def marked_bits(k):
    mask = 1
    bit = 0
    result = []
    while mask <= k:
        if k & mask:
            result.append(bit)
        mask <<= 1
        bit += 1
    return result

def add_edge(grid, a, b):
    grid[a][b] = "Y"
    grid[b][a] = "Y"

def answer(k):
    if k == 1:
        return ["2", "NY", "YN"]

    bits = marked_bits(k)
    high = bits[-1]
    n = 2 * high + 2
    grid = [["N"] * n for _ in range(n)]

    current = [0]
    for depth in range(1, high + 1):
        nxt = [2 * depth, 2 * depth + 1]
        for a in current:
            for b in nxt:
                add_edge(grid, a, b)
        current = nxt

    chosen = set(bits)
    if 0 in chosen:
        add_edge(grid, 0, 1)

    for depth in range(1, high + 1):
        if depth in chosen:
            add_edge(grid, 2 * depth, 1)

    out = [str(n)]
    out.extend("".join(row) for row in grid)
    return out

# CLAUSE: finish_program
def main():
    k = int(sys.stdin.readline())
    print("\n".join(answer(k)))

if __name__ == "__main__":
    main()
