import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    fights = []
    for i in range(m):
        fights.append((numbers[2 + 3 * i], numbers[3 + 3 * i], numbers[4 + 3 * i]))
    return n, fights


# --- clause: run_tournament :: (n: int, fights: list[tuple[int, int, int]]) -> list[int] ---
def run_tournament(n, fights):
    beaten = [0] * (n + 2)
    parent = list(range(n + 2))
    for left, right, winner in fights:
        spot = left
        while spot <= right:
            root = spot
            while parent[root] != root:
                root = parent[root]
            while parent[spot] != root:
                parent[spot], spot = root, parent[spot]
            spot = root
            if spot > right:
                break
            if spot == winner:
                spot += 1
                continue
            beaten[spot] = winner
            parent[spot] = spot + 1
            spot += 1
    return beaten[1:n + 1]


# --- clause: main :: () -> None ---
def main():
    n, fights = read_input()
    sys.stdout.write(" ".join(map(str, run_tournament(n, fights))) + "\n")


if __name__ == "__main__":
    main()
