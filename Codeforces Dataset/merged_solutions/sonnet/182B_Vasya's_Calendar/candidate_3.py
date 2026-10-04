import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    d, n = int(data[0]), int(data[1])
    months = [int(token) for token in data[2:n + 2]]
    return d, n, months


# --- clause: manual_clicks :: (d: int, n: int, months: list[int]) -> int ---
def manual_clicks(d, n, months):
    total = 0
    i = 0
    while i < n - 1:
        total = total + d - months[i]
        i += 1
    return total


# --- clause: main :: () -> None ---
def main():
    d, n, months = read_input()
    print(manual_clicks(d, n, months))


if __name__ == "__main__":
    main()
