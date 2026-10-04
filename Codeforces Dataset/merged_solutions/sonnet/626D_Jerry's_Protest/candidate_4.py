import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: gap_counts :: (balls: list[int]) -> list[int] ---
def gap_counts(balls):
    present = [0] * 5001
    for value in balls:
        present[value] = 1
    counts = [0] * 5001
    order = sorted(balls)
    for i in range(len(order) - 1, 0, -1):
        big = order[i]
        for j in range(i):
            counts[big - order[j]] += 1
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
