# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = [int(x) for x in sys.stdin.read().split()]
    grid = [values[0:3], values[3:6], values[6:9]]
    lights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    for r in range(3):
        for c in range(3):
            if grid[r][c] % 2:
                lights[r][c] ^= 1
                if r > 0:
                    lights[r - 1][c] ^= 1
                if r < 2:
                    lights[r + 1][c] ^= 1
                if c > 0:
                    lights[r][c - 1] ^= 1
                if c < 2:
                    lights[r][c + 1] ^= 1

    sys.stdout.write("\n".join("".join(str(x) for x in row) for row in lights))

# CLAUSE: finish_program
main()
