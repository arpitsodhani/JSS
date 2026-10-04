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
    zeros = sum(1 for c in "BGR" if counts[c] == 0)
    if zeros == 2:
        return "".join(c for c in "BGR" if counts[c])
    if zeros == 0:
        return "BGR"
    missing = [c for c in "BGR" if counts[c] == 0][0]
    others = [c for c in "BGR" if c != missing]
    if counts[others[0]] == 1 and counts[others[1]] == 1:
        return missing
    for c in others:
        if counts[c] == 1:
            return "".join(sorted([c, missing]))
    return "BGR"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(possible_colors(read_input()) + "\n")


if __name__ == "__main__":
    main()
