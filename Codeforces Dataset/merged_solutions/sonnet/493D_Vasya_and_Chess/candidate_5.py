import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    size = int(data[0])
    return size


# --- clause: decide :: (n: int) -> str ---
def decide(n):
    if not n % 2:
        return "white\n1 2"
    return "black"


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write(decide(n) + "\n")


if __name__ == "__main__":
    main()
