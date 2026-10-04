import sys


# --- clause: read_input :: () -> tuple[str, list[str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    s = fields[1].decode()
    m = int(fields[2])
    return s, [fields[3 + i].decode() for i in range(m)]


# --- clause: letter_spots :: (s: str) -> dict[str, list[int]] ---
def letter_spots(s):
    spots = {}
    for i in range(len(s)):
        spots.setdefault(s[i], []).append(i + 1)
    return spots


# --- clause: prefix_length :: (spots: dict[str, list[int]], name: str) -> int ---
def prefix_length(spots, name):
    occurrences = {}
    for ch in name:
        occurrences[ch] = occurrences.get(ch, 0) + 1
    finest = 0
    for ch in occurrences:
        place = spots[ch][occurrences[ch] - 1]
        if place > finest:
            finest = place
    return finest


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
