# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def distance_sum(n, m, r, c):
    same_row = m - c
    lower_rows = n - r
    return same_row + lower_rows * (2 * m - 1)

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    out = []
    for i in range(1, 1 + 4 * nums[0], 4):
        out.append(str(distance_sum(nums[i], nums[i + 1], nums[i + 2], nums[i + 3])))

# CLAUSE: finish_program
    print("\n".join(out))

if __name__ == "__main__":
    main()
