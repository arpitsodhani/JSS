import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[0].decode(), fields[1].decode()


# --- clause: walk_moves :: (start: str, goal: str) -> list[str] ---
def walk_moves(start, goal):
    x = ord(goal[0]) - ord(start[0])
    y = int(goal[1]) - int(start[1])
    moves = []
    while x or y:
        delta = ""
        if x > 0:
            delta += "R"
            x -= 1
        elif x < 0:
            delta += "L"
            x += 1
        if y > 0:
            delta += "U"
            y -= 1
        elif y < 0:
            delta += "D"
            y += 1
        moves.append(delta)
    return moves


# --- clause: main :: () -> None ---
def main():
    start, goal = read_input()
    moves = walk_moves(start, goal)
    sys.stdout.write("%d\n%s\n" % (len(moves), "\n".join(moves)) if moves else "0\n")


if __name__ == "__main__":
    main()
