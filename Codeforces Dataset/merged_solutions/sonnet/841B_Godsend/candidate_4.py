import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: winner :: (n: int, values: list[int]) -> str ---
def winner(n, values):
    for i in range(n):
        if values[i] % 2 == 1:
            return "First"
    return "Second"


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    answer = winner(n, values)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
