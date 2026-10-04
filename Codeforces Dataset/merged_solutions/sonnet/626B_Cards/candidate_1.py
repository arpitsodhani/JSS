import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: possible_colors :: (deck: str) -> str ---
def possible_colors(deck):
    counts = {"B": 0, "G": 0, "R": 0}
    for ch in deck:
        counts[ch] += 1
    absent = [c for c in "BGR" if counts[c] == 0]
    if len(absent) == 2:
        return "".join(c for c in "BGR" if counts[c])
    if len(absent) == 1:
        missing = absent[0]
        singles = [c for c in "BGR" if c != missing and counts[c] == 1]
        if len(singles) == 2:
            return missing
        if len(singles) == 1:
            return "".join(sorted(singles + [missing]))
    return "BGR"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(possible_colors(read_input()) + "\n")


if __name__ == "__main__":
    main()
