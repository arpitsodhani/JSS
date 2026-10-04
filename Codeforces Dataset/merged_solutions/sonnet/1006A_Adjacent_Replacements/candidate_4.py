import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: settle :: (a: list[int]) -> list[int] ---
def settle(a):
    return [value - (1 - (value & 1)) for value in a]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()
