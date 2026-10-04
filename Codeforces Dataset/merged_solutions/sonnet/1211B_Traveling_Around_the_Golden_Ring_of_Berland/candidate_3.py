import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    wanted = []
    for token in data[1:n + 1]:
        wanted.append(int(token))
    return n, wanted


# --- clause: count_visits :: (n: int, wanted: list[int]) -> int ---
def count_visits(n, wanted):
    most = 0
    for value in wanted:
        if value > most:
            most = value
    last = n
    while wanted[last - 1] != most:
        last -= 1
    return (most - 1) * n + last


# --- clause: main :: () -> None ---
def main():
    n, wanted = read_input()
    print(count_visits(n, wanted))


if __name__ == "__main__":
    main()
