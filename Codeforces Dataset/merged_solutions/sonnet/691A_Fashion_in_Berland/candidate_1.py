import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = [int(token) for token in data[1:n + 1]]
    return n, buttons


# --- clause: fastened_well :: (n: int, buttons: list[int]) -> str ---
def fastened_well(n, buttons):
    done = 0
    for value in buttons:
        done += value
    if n == 1:
        if done == 1:
            return "YES"
        return "NO"
    if done == n - 1:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    n, buttons = read_input()
    sys.stdout.write(fastened_well(n, buttons) + "\n")


if __name__ == "__main__":
    main()
