import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: shifted_order :: (n: int) -> list[int] ---
def shifted_order(n):
    arranged = []
    for j in range(1, n + 1):
        arranged.append(j % n + 1)
    return arranged


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write(" ".join(map(str, shifted_order(n))) + "\n")


if __name__ == "__main__":
    main()
