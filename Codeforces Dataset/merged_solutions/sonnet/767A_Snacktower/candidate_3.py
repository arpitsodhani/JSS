import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: build_tower :: (fallen: list[int]) -> list[str] ---
def build_tower(fallen):
    n = len(fallen)
    have = [False] * (n + 2)
    wanted = n
    collected = []
    for length_of in fallen:
        have[length_of] = True
        placed = []
        while wanted >= 1 and have[wanted]:
            placed.append(str(wanted))
            wanted -= 1
        collected.append(" ".join(placed))
    return collected


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(build_tower(read_input())) + "\n")


if __name__ == "__main__":
    main()
