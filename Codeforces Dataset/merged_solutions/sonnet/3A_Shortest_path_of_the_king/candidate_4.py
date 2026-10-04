import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), numbers[1].decode()


# --- clause: walk_moves :: (start: str, goal: str) -> list[str] ---
def walk_moves(start, goal):
    x = ord(goal[0]) - ord(start[0])
    y = int(goal[1]) - int(start[1])
    across = "R" if x > 0 else "L"
    updown = "U" if y > 0 else "D"
    left = abs(x)
    down = abs(y)
    moves = []
    while left > 0 and down > 0:
        moves.append(across + updown)
        left -= 1
        down -= 1
    moves.extend([across] * left)
    moves.extend([updown] * down)
    return moves


# --- clause: main :: () -> None ---
def main():
    start, goal = read_input()
    moves = walk_moves(start, goal)
    sys.stdout.write("%d\n%s\n" % (len(moves), "\n".join(moves)) if moves else "0\n")


if __name__ == "__main__":
    main()
