import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n


# --- clause: decide :: (n: int) -> str ---
def decide(n):
    if n & 1:
        return "black"
    return "white\n1 2"


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("%s\n" % decide(n))


if __name__ == "__main__":
    main()
