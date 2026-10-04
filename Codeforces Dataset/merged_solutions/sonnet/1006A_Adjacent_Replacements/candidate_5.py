import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: settle :: (a: list[int]) -> list[int] ---
def settle(a):
    written = []
    for item in a:
        written.append(item - 1 if item % 2 == 0 else item)
    return written


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()
