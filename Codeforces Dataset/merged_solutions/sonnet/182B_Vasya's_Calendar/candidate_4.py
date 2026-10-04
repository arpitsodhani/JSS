import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    d = int(data[0])
    n = int(data[1])
    months = [int(data[i + 2]) for i in range(n)]
    return d, n, months


# --- clause: manual_clicks :: (d: int, n: int, months: list[int]) -> int ---
def manual_clicks(d, n, months):
    total = d * (n - 1)
    for i in range(n - 1):
        total -= months[i]
    return total


# --- clause: main :: () -> None ---
def main():
    d, n, months = read_input()
    answer = manual_clicks(d, n, months)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
