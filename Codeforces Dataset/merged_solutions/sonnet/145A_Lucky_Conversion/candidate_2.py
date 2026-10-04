import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return tokens[0].decode(), tokens[1].decode()


# --- clause: fewest_moves :: (a: str, b: str) -> int ---
def fewest_moves(a, b):
    ups = 0
    downs = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if a[i] == "4":
            ups += 1
        else:
            downs += 1
    return ups if ups > downs else downs


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % fewest_moves(a, b))


if __name__ == "__main__":
    main()
