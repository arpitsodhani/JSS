import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    d = int(data[0])
    n = int(data[1])
    months = list(map(int, data[2:n + 2]))
    return d, n, months


# --- clause: manual_clicks :: (d: int, n: int, months: list[int]) -> int ---
def manual_clicks(d, n, months):
    return sum(d - month for month in months[:n - 1])


# --- clause: main :: () -> None ---
def main():
    d, n, months = read_input()
    sys.stdout.write("%d\n" % manual_clicks(d, n, months))


if __name__ == "__main__":
    main()
