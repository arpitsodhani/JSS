import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:1 + n]))
    return n, values


# --- clause: winner :: (n: int, values: list[int]) -> str ---
def winner(n, values):
    for value in values:
        if value % 2 != 0:
            return "First"
    return "Second"


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    verdict = winner(n, values)
    sys.stdout.write(verdict + "\n")


if __name__ == "__main__":
    main()
