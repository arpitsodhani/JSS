import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = [int(data[i + 1]) for i in range(n)]
    return n, buttons


# --- clause: fastened_well :: (n: int, buttons: list[int]) -> str ---
def fastened_well(n, buttons):
    done = 0
    for value in buttons:
        done += value
    open_count = n - done
    if n == 1:
        return "YES" if open_count == 0 else "NO"
    return "YES" if open_count == 1 else "NO"


# --- clause: main :: () -> None ---
def main():
    n, buttons = read_input()
    verdict = fastened_well(n, buttons)
    sys.stdout.write(verdict + "\n")


if __name__ == "__main__":
    main()
