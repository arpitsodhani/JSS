import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    juices = []
    for i in range(n):
        price = int(raw[1 + 2 * i])
        signature = 0
        for letter in raw[2 + 2 * i]:
            signature |= 1 << (letter - 65)
        juices.append((price, signature))
    return juices


# --- clause: cheapest_set :: (juices: list[tuple[int, int]]) -> int ---
def cheapest_set(juices):
    infinity = float("inf")
    cost = [infinity] * 8
    cost[0] = 0
    for price, signature in juices:
        for have in range(8):
            if cost[have] == infinity:
                continue
            amount = cost[have] + price
            if amount < cost[have | signature]:
                cost[have | signature] = amount
    return -1 if cost[7] == infinity else cost[7]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % cheapest_set(read_input()))


if __name__ == "__main__":
    main()
