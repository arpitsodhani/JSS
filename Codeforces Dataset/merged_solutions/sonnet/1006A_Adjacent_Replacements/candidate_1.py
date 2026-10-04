import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: settle :: (a: list[int]) -> list[int] ---
def settle(a):
    out = []
    for value in a:
        out.append(value - 1 if value % 2 == 0 else value)
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()
