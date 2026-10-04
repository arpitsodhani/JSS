import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = []
    for token in data[1:n + 1]:
        values.append(int(token))
    return n, values


# --- clause: winner :: (n: int, values: list[int]) -> str ---
def winner(n, values):
    for value in values:
        if value % 2 == 0:
            continue
        return "First"
    return "Second"


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    print(winner(n, values))


if __name__ == "__main__":
    main()
