import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    q = numbers[0]
    reader = 1
    cases = []
    for _ in range(q):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: biggest_gift :: (a: list[int]) -> int ---
def biggest_gift(a):
    counts = [0] * (len(a) + 2)
    for value in a:
        counts[value] += 1
    sizes = []
    for value in range(len(counts)):
        if counts[value]:
            sizes.append(counts[value])
    sizes.sort()
    total = 0
    allowed = len(a) + 1
    spot = len(sizes) - 1
    while spot >= 0:
        take = min(sizes[spot], allowed - 1)
        if take <= 0:
            break
        total += take
        allowed = take
        spot -= 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(biggest_gift(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
