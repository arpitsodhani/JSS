# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def transformed_bit(a, c):
    bit = int(a)
    choice = int(c)
    return bit if choice else bit ^ 1

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    length = int(tokens[0])
    xs = tokens[1][:length]
    bs = tokens[2][:length]
    start = int(tokens[4]) if len(tokens) > 4 else 0
    total = start
    for pair in zip(xs, bs):
        total ^= transformed_bit(pair[0], pair[1])
    print(total)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
