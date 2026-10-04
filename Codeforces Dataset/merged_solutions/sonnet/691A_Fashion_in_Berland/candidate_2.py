import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = list(map(int, data[1:n + 1]))
    return n, buttons


# --- clause: fastened_well :: (n: int, buttons: list[int]) -> str ---
def fastened_well(n, buttons):
    done = sum(buttons)
    if n == 1:
        return "YES" if done == 1 else "NO"
    return "YES" if done + 1 == n else "NO"


# --- clause: main :: () -> None ---
def main():
    n, buttons = read_input()
    sys.stdout.write("%s\n" % fastened_well(n, buttons))


if __name__ == "__main__":
    main()
