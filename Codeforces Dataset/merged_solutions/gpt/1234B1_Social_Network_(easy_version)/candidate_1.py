# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    ids = data[2:2 + n]

    screen = []
    shown = set()

    for friend_id in ids:
        if friend_id in shown:
            continue
        if len(screen) == k:
            removed = screen.pop()
            shown.remove(removed)
        screen.insert(0, friend_id)
        shown.add(friend_id)

    print(len(screen))
    print(*screen)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
