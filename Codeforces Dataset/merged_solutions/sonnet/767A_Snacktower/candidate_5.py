import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: build_tower :: (fallen: list[int]) -> list[str] ---
def build_tower(fallen):
    n = len(fallen)
    have = [False] * (n + 2)
    wanted = n
    written = []
    for width in fallen:
        have[width] = True
        placed = []
        while wanted >= 1 and have[wanted]:
            placed.append(str(wanted))
            wanted -= 1
        written.append(" ".join(placed))
    return written


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()
