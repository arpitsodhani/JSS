import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: longest_run :: (n: int) -> int ---
def longest_run(n):
    advance = 1
    while n % advance == 0:
        advance += 1
    return advance - 1


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        lines.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
