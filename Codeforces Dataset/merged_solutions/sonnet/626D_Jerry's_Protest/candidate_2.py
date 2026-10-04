import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: gap_counts :: (balls: list[int]) -> list[int] ---
def gap_counts(balls):
    sorted_items = sorted(balls)
    n = len(sorted_items)
    counts = [0] * 5001
    for i in range(n):
        for j in range(i + 1, n):
            counts[sorted_items[j] - sorted_items[i]] += 1
    return counts


# --- clause: win_chance :: (counts: list[int]) -> float ---
def win_chance(counts):
    total = 0
    for value in counts:
        total += value
    if total == 0:
        return 0.0
    above = [0] * (len(counts) + 2)
    for d in range(len(counts) - 1, -1, -1):
        above[d] = above[d + 1] + counts[d]
    present = []
    for d in range(len(counts)):
        if counts[d]:
            present.append(d)
    good = 0
    for d1 in present:
        for d2 in present:
            here = counts[d1] * counts[d2]
            reach = d1 + d2 + 1
            if reach < len(counts):
                good += here * above[reach]
    return good / (float(total) ** 3)


# --- clause: main :: () -> None ---
def main():
    balls = read_input()
    sys.stdout.write("%.10f\n" % win_chance(gap_counts(balls)))


if __name__ == "__main__":
    main()
