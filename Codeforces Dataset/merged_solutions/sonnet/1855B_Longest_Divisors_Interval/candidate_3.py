import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: longest_run :: (n: int) -> int ---
def longest_run(n):
    delta = 1
    while n % delta == 0:
        delta += 1
    return delta - 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
