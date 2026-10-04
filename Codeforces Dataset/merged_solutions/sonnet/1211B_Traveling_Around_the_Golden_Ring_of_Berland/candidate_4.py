import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    wanted = [int(data[i + 1]) for i in range(n)]
    return n, wanted


# --- clause: count_visits :: (n: int, wanted: list[int]) -> int ---
def count_visits(n, wanted):
    most = wanted[0]
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
    answer = count_visits(n, wanted)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
