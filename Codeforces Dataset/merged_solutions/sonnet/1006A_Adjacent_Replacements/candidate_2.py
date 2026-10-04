import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: settle :: (a: list[int]) -> list[int] ---
def settle(a):
    lines = []
    for value in a:
        lines.append(value - 1 if value % 2 == 0 else value)
    return lines


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()
