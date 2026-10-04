import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    wanted = [int(token) for token in data[1:n + 1]]
    return n, wanted


# --- clause: count_visits :: (n: int, wanted: list[int]) -> int ---
def count_visits(n, wanted):
    most = 0
    for value in wanted:
        if value > most:
            most = value
    last = 0
    for i in range(n):
        if wanted[i] == most:
            last = i + 1
    return (most - 1) * n + last


# --- clause: main :: () -> None ---
def main():
    n, wanted = read_input()
    sys.stdout.write(str(count_visits(n, wanted)) + "\n")


if __name__ == "__main__":
    main()
