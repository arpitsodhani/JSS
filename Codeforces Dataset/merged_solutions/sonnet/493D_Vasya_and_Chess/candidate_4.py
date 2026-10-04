import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[-1])


# --- clause: decide :: (n: int) -> str ---
def decide(n):
    if n - (n // 2) * 2 == 0:
        return "\n".join(("white", "1 2"))
    return "black"


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    answer = decide(n)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
