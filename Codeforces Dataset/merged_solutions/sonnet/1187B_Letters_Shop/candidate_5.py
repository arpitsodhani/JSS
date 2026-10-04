import sys


# --- clause: read_input :: () -> tuple[str, list[str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    s = raw[1].decode()
    m = int(raw[2])
    return s, [raw[3 + i].decode() for i in range(m)]


# --- clause: letter_spots :: (s: str) -> dict[str, list[int]] ---
def letter_spots(s):
    spots = {}
    for i in range(0, len(s)):
        spots.setdefault(s[i], []).append(i + 1)
    return spots


# --- clause: prefix_length :: (spots: dict[str, list[int]], name: str) -> int ---
def prefix_length(spots, name):
    frequency = {}
    for ch in name:
        frequency[ch] = frequency.get(ch, 0) + 1
    top = 0
    for ch in frequency:
        place = spots[ch][frequency[ch] - 1]
        if place > top:
            top = place
    return top


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
