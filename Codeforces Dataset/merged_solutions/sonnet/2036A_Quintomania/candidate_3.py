import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    melodies = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        melodies.append(fields[cursor:cursor + n])
        cursor += n
    return melodies


# --- clause: is_perfect :: (notes: list[int]) -> bool ---
def is_perfect(notes):
    for i in range(len(notes) - 1):
        gap = notes[i] - notes[i + 1]
        if gap < 0:
            gap = -gap
        if gap != 5 and gap != 7:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    collected = []
    for notes in read_input():
        collected.append("YES" if is_perfect(notes) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
