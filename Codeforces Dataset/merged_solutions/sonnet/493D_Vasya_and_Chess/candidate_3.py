import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0].decode())


# --- clause: decide :: (n: int) -> str ---
def decide(n):
    winner = "black" if n % 2 else "white"
    if winner == "black":
        return winner
    return winner + "\n1 2"


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    print(decide(n))


if __name__ == "__main__":
    main()
