import sys


# --- clause: read_input :: () -> tuple[str, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    s = data[1].decode()
    m = int(data[2])
    return s, [data[3 + i].decode() for i in range(m)]


# --- clause: letter_spots :: (s: str) -> dict[str, list[int]] ---
def letter_spots(s):
    spots = {}
    for i in range(len(s)):
        spots.setdefault(s[i], []).append(i + 1)
    return spots


# --- clause: prefix_length :: (spots: dict[str, list[int]], name: str) -> int ---
def prefix_length(spots, name):
    counts = {}
    for ch in name:
        counts[ch] = counts.get(ch, 0) + 1
    best = 0
    for ch in counts:
        place = spots[ch][counts[ch] - 1]
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
