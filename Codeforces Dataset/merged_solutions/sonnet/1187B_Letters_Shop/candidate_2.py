import sys


# --- clause: read_input :: () -> tuple[str, list[str]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    s = tokens[1].decode()
    m = int(tokens[2])
    return s, [tokens[3 + i].decode() for i in range(m)]


# --- clause: letter_spots :: (s: str) -> dict[str, list[int]] ---
def letter_spots(s):
    spots = {}
    for i in range(len(s)):
        spots.setdefault(s[i], []).append(i + 1)
    return spots


# --- clause: prefix_length :: (spots: dict[str, list[int]], name: str) -> int ---
def prefix_length(spots, name):
    tally = {}
    for ch in name:
        tally[ch] = tally.get(ch, 0) + 1
    best = 0
    for ch in tally:
        place = spots[ch][tally[ch] - 1]
        if place > best:
            best = place
    return best


# --- clause: main :: () -> None ---
def main():
    s, names = read_input()
    spots = letter_spots(s)
    out = []
    for name in names:
        out.append(prefix_length(spots, name))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
