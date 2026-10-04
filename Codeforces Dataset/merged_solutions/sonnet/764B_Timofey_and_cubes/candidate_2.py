import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: undo_layers :: (a: list[int]) -> list[int] ---
def undo_layers(a):
    line = list(a)
    n = len(line)
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        line[i], line[j] = line[j], line[i]
    return line


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()
