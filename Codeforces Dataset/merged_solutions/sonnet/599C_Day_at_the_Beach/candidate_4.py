import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: block_count :: (h: list[int]) -> int ---
def block_count(h):
    ranked = sorted(h)
    running = 0
    wanted = 0
    blocks = 0
    for i in range(len(h)):
        running += h[i]
        wanted += ranked[i]
        if running == wanted:
            blocks += 1
    return blocks


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % block_count(read_input()))


if __name__ == "__main__":
    main()
