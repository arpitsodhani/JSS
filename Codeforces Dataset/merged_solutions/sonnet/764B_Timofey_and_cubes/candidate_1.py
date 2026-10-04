import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: undo_layers :: (a: list[int]) -> list[int] ---
def undo_layers(a):
    row = list(a)
    n = len(row)
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        row[i], row[j] = row[j], row[i]
    return row


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()
