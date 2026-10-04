import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: build_tower :: (fallen: list[int]) -> list[str] ---
def build_tower(fallen):
    n = len(fallen)
    have = [False] * (n + 2)
    wanted = n
    lines = []
    for size in fallen:
        have[size] = True
        placed = []
        while wanted >= 1 and have[wanted]:
            placed.append(str(wanted))
            wanted -= 1
        lines.append(" ".join(placed))
    return lines


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()
