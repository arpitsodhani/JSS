import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_tower :: (fallen: list[int]) -> list[str] ---
def build_tower(fallen):
    n = len(fallen)
    have = [False] * (n + 2)
    wanted = n
    out = []
    for size in fallen:
        have[size] = True
        placed = []
        while wanted >= 1 and have[wanted]:
            placed.append(str(wanted))
            wanted -= 1
        out.append(" ".join(placed))
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()
