import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = list(map(int, data[1:1 + n]))
    return n, buttons


# --- clause: fastened_well :: (n: int, buttons: list[int]) -> str ---
def fastened_well(n, buttons):
    done = buttons.count(1)
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
    answer = fastened_well(n, buttons)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
