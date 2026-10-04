import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()

# Clause walk_moves [Confidence: 0.80]
def walk_moves(start, goal):
    x = ord(goal[0]) - ord(start[0])
    y = int(goal[1]) - int(start[1])
    moves = []
    while x or y:
        advance = ""
        if x > 0:
            advance += "R"
            x -= 1
        elif x < 0:
            advance += "L"
            x += 1
        if y > 0:
            advance += "U"
            y -= 1
        elif y < 0:
            advance += "D"
            y += 1
        moves.append(advance)
    return moves

# Clause main [Confidence: 1.00]
def main():
    start, goal = read_input()
    moves = walk_moves(start, goal)
    sys.stdout.write("%d\n%s\n" % (len(moves), "\n".join(moves)) if moves else "0\n")


if __name__ == "__main__":
    main()

