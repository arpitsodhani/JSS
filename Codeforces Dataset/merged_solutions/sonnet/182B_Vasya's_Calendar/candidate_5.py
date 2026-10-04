import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    d = int(data[0])
    n = int(data[1])
    months = list(map(int, data[2:2 + n]))
    return d, n, months


# --- clause: manual_clicks :: (d: int, n: int, months: list[int]) -> int ---
def manual_clicks(d, n, months):
    total = 0
    for month in months[0:n - 1]:
        total += d - month
    return total


# --- clause: main :: () -> None ---
def main():
    d, n, months = read_input()
    sys.stdout.write(str(manual_clicks(d, n, months)) + "\n")


if __name__ == "__main__":
    main()
