# CLAUSE: setup_environment
import sys
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    grid = []
    flat_size = n * m
    fenwick = array("i", [0]) * (flat_size + 1)
    star_count = 0

    def add_one_based(i, d):
        while i <= flat_size:
            fenwick[i] += d
            i += i & -i

    def occupied_prefix(i):
        s = 0
        while i:
            s += fenwick[i]
            i -= i & -i
        return s

# CLAUSE: solve_logic
    for r in range(n):
        current = bytearray(data[3 + r])
        grid.append(current)
        c = 0
        while c < m:
            if current[c] == ord("*"):
                star_count += 1
                add_one_based(c * n + r + 1, 1)
            c += 1

    ans = []
    pos = 3 + n
    remaining = q
    while remaining:
        x = int(data[pos]) - 1
        y = int(data[pos + 1]) - 1
        pos += 2
        idx = y * n + x + 1
        if grid[x][y] == ord("*"):
            grid[x][y] = ord(".")
            star_count -= 1
            add_one_based(idx, -1)
        else:
            grid[x][y] = ord("*")
            star_count += 1
            add_one_based(idx, 1)
        ans.append(str(star_count - occupied_prefix(star_count)))
        remaining -= 1

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
