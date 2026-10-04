import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: possible_colors :: (deck: str) -> str ---
def possible_colors(deck):
    blue = deck.count("B")
    green = deck.count("G")
    red = deck.count("R")
    present = [c for c, k in (("B", blue), ("G", green), ("R", red)) if k]
    if len(present) == 1:
        return present[0]
    if len(present) == 3:
        return "BGR"
    missing = [c for c in "BGR" if c not in present][0]
    counts = {"B": blue, "G": green, "R": red}
    singles = [c for c in present if counts[c] == 1]
    if len(singles) == 2:
        return missing
    if len(singles) == 1:
        return "".join(sorted([singles[0], missing]))
    return "BGR"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(possible_colors(read_input()) + "\n")


if __name__ == "__main__":
    main()
