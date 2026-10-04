import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    juices = []
    for i in range(n):
        price = int(fields[1 + 2 * i])
        flags = 0
        for letter in fields[2 + 2 * i]:
            flags |= 1 << (letter - 65)
        juices.append((price, flags))
    return juices


# --- clause: cheapest_set :: (juices: list[tuple[int, int]]) -> int ---
def cheapest_set(juices):
    infinity = float("inf")
    cost = [infinity] * 8
    cost[0] = 0
    for price, flags in juices:
        for have in range(8):
            if cost[have] == infinity:
                continue
            summed = cost[have] + price
            if summed < cost[have | flags]:
                cost[have | flags] = summed
    return -1 if cost[7] == infinity else cost[7]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % cheapest_set(read_input()))


if __name__ == "__main__":
    main()
