import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: undo_layers :: (a: list[int]) -> list[int] ---
def undo_layers(a):
    entry_row = list(a)
    n = len(entry_row)
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        entry_row[i], entry_row[j] = entry_row[j], entry_row[i]
    return entry_row


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()
