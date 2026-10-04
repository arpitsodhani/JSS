import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[2:2 + raw[0]]


# --- clause: colour_order :: (colours: list[int]) -> list[int] ---
def colour_order(colours):
    tally = {}
    for number in colours:
        tally[number] = tally.get(number, 0) + 1
    sorted_items = sorted(tally, key=lambda number: (-tally[number], number))
    line = []
    for number in sorted_items:
        for _ in range(tally[number]):
            line.append(number)
    return line


# --- clause: pair_up :: (line: list[int]) -> tuple[int, list[tuple[int, int]]] ---
def pair_up(line):
    n = len(line)
    shift = n // 2
    rights = line[shift:] + line[:shift]
    good = []
    bad = []
    for i in range(n):
        if line[i] != rights[i]:
            good.append((line[i], rights[i]))
        else:
            bad.append((line[i], rights[i]))
    return len(good), good + bad


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
