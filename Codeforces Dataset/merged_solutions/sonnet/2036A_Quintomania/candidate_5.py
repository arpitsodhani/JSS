import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    melodies = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        melodies.append(raw[offset:offset + n])
        offset += n
    return melodies


# --- clause: is_perfect :: (notes: list[int]) -> bool ---
def is_perfect(notes):
    gaps = set()
    for first, second in zip(notes, notes[1:]):
        gaps.add(abs(first - second))
    return gaps <= {5, 7}


# --- clause: main :: () -> None ---
def main():
    written = []
    for notes in read_input():
        written.append("YES" if is_perfect(notes) else "NO")
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
