# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def get_moves(tokens):
    if len(tokens) == 1:
        return "".join(x for x in tokens[0] if x == "U" or x == "R")
    return tokens[1]

def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

def count_crossings(moves):
    position = 0
    previous = 0
    total = 0

    for move in moves:
        if move == "U":
            position -= 1
        else:
            position += 1

        now = sign(position)
        if now != 0:
            if previous != 0 and previous != now:
                total += 1
            previous = now

    return total

def main():
    tokens = sys.stdin.read().split()
    sys.stdout.write(str(count_crossings(get_moves(tokens))))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
