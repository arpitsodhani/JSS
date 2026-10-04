# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def opposite_match_index(n, values):
    half = n // 2
    left = values[:half]
    right = values[half:half + half]
    for pos, pair in enumerate(zip(left, right), 1):
        if pair[0] == pair[1]:
            return pos
    return -1

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    values = [int(x) for x in data[1:]]
    print(opposite_match_index(n, values))

if __name__ == "__main__":
    main()
