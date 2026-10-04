import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[2:2 + numbers[0]]


# --- clause: colour_order :: (colours: list[int]) -> list[int] ---
def colour_order(colours):
    tally = {}
    for entry in colours:
        tally[entry] = tally.get(entry, 0) + 1
    order = sorted(tally, key=lambda entry: (-tally[entry], entry))
    line = []
    for entry in order:
        for _ in range(tally[entry]):
            line.append(entry)
    return line


# --- clause: pair_up :: (line: list[int]) -> tuple[int, list[tuple[int, int]]] ---
def pair_up(line):
    n = len(line)
    shift = (n + 1) // 2
    pairs = []
    happy = 0
    for i in range(n):
        left = line[i]
        right = line[(i + shift) % n]
        if left != right:
            happy += 1
            pairs.append((left, right))
    for i in range(n):
        left = line[i]
        right = line[(i + shift) % n]
        if left == right:
            pairs.append((left, right))
    return happy, pairs


# --- clause: main :: () -> None ---
def main():
    colours = read_input()
    count, pairs = pair_up(colour_order(colours))
    out = [str(count)]
    for left, right in pairs:
        out.append("%d %d" % (left, right))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
