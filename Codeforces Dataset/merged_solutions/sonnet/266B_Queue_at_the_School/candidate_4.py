import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return int(numbers[1]), numbers[2].decode()


# --- clause: shuffle_queue :: (t: int, line: str) -> str ---
def shuffle_queue(t, line):
    for _ in range(t):
        parts = line.split("BG")
        line = "GB".join(parts)
    return line


# --- clause: main :: () -> None ---
def main():
    t, line = read_input()
    sys.stdout.write(shuffle_queue(t, line) + "\n")


if __name__ == "__main__":
    main()
