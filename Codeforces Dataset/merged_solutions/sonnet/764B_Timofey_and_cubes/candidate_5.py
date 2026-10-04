import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: undo_layers :: (a: list[int]) -> list[int] ---
def undo_layers(a):
    band = list(a)
    n = len(band)
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        band[i], band[j] = band[j], band[i]
    return band


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, undo_layers(read_input()))) + "\n")


if __name__ == "__main__":
    main()
