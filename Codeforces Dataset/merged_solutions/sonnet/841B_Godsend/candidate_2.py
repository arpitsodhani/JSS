import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values


# --- clause: winner :: (n: int, values: list[int]) -> str ---
def winner(n, values):
    for value in values:
        if value & 1:
            return "First"
    return "Second"


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write("%s\n" % winner(n, values))


if __name__ == "__main__":
    main()
