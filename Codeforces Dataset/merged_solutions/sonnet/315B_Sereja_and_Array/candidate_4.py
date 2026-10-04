import sys


# --- clause: read_input :: () -> tuple[list[int], list[list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    a = numbers[2:2 + n]
    reader = 2 + n
    steps = []
    for _ in range(m):
        kind = numbers[reader]
        if kind == 1:
            steps.append([1, numbers[reader + 1], numbers[reader + 2]])
            reader += 3
        else:
            steps.append([kind, numbers[reader + 1]])
            reader += 2
    return a, steps


# --- clause: run_steps :: (a: list[int], steps: list[list[int]]) -> list[int] ---
def run_steps(a, steps):
    board = {}
    shift = 0
    out = []
    for step in steps:
        if step[0] == 1:
            board[step[1] - 1] = step[2] - shift
        elif step[0] == 2:
            shift += step[1]
        else:
            spot = step[1] - 1
            base = board[spot] if spot in board else a[spot]
            out.append(base + shift)
    return out


# --- clause: main :: () -> None ---
def main():
    a, steps = read_input()
    sys.stdout.write("\n".join(map(str, run_steps(a, steps))) + "\n")


if __name__ == "__main__":
    main()
