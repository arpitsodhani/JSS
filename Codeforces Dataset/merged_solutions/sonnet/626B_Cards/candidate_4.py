import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: possible_colors :: (deck: str) -> str ---
def possible_colors(deck):
    counts = {}
    for colour in "BGR":
        counts[colour] = 0
    for ch in deck:
        counts[ch] += 1
    have = [c for c in "BGR" if counts[c] > 0]
    if len(have) == 1:
        return have[0]
    if len(have) == 2:
        gap = [c for c in "BGR" if counts[c] == 0][0]
        small = [c for c in have if counts[c] == 1]
        if len(small) == 2:
            return gap
        if len(small) == 1:
            answer = sorted([small[0], gap])
            return "".join(answer)
    return "BGR"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(possible_colors(read_input()) + "\n")


if __name__ == "__main__":
    main()
