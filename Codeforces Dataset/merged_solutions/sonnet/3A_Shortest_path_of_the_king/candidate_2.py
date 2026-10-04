import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return tokens[0].decode(), tokens[1].decode()


# --- clause: walk_moves :: (start: str, goal: str) -> list[str] ---
def walk_moves(start, goal):
    x = ord(goal[0]) - ord(start[0])
    y = int(goal[1]) - int(start[1])
    moves = []
    while x or y:
        stride = ""
        if x > 0:
            stride += "R"
            x -= 1
        elif x < 0:
            stride += "L"
            x += 1
        if y > 0:
            stride += "U"
            y -= 1
        elif y < 0:
            stride += "D"
            y += 1
        moves.append(stride)
    return moves


# --- clause: main :: () -> None ---
def main():
    start, goal = read_input()
    moves = walk_moves(start, goal)
    sys.stdout.write("%d\n%s\n" % (len(moves), "\n".join(moves)) if moves else "0\n")


if __name__ == "__main__":
    main()
