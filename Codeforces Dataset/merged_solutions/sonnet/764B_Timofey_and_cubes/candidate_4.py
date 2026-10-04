import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: undo_layers :: (a: list[int]) -> list[int] ---
def undo_layers(a):
    n = len(a)
    row = []
    for i in range(n):
        layer = i if i < n - 1 - i else n - 1 - i
        if layer % 2:
            row.append(a[i])
        else:
            row.append(a[n - 1 - i])
    return row


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()
