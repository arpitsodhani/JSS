import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_tower :: (fallen: list[int]) -> list[str] ---
def build_tower(fallen):
    n = len(fallen)
    have = set()
    wanted = n
    out = []
    for size in fallen:
        have.add(size)
        placed = []
        while wanted in have:
            placed.append(str(wanted))
            have.discard(wanted)
            wanted -= 1
        out.append(" ".join(placed))
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()
