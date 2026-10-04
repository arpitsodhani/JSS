import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    juices = []
    for i in range(n):
        price = int(tokens[1 + 2 * i])
        bits = 0
        for letter in tokens[2 + 2 * i]:
            bits |= 1 << (letter - 65)
        juices.append((price, bits))
    return juices


# --- clause: cheapest_set :: (juices: list[tuple[int, int]]) -> int ---
def cheapest_set(juices):
    infinity = float("inf")
    cheapest = [infinity] * 8
    for price, mask in juices:
        if price < cheapest[mask]:
            cheapest[mask] = price
    cheapest[0] = 0
    best = infinity
    for first in range(8):
        for second in range(first, 8):
            for third in range(second, 8):
                if first | second | third != 7:
                    continue
                total = cheapest[first] + cheapest[second] + cheapest[third]
                if total < best:
                    best = total
    return -1 if best == infinity else best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % cheapest_set(read_input()))


if __name__ == "__main__":
    main()
