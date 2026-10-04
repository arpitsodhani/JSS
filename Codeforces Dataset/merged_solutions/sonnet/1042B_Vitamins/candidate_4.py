import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    juices = []
    for i in range(n):
        price = int(numbers[1 + 2 * i])
        pattern = 0
        for letter in numbers[2 + 2 * i]:
            pattern |= 1 << (letter - 65)
        juices.append((price, pattern))
    return juices


# --- clause: cheapest_set :: (juices: list[tuple[int, int]]) -> int ---
def cheapest_set(juices):
    infinity = float("inf")
    cost = [infinity] * 8
    cost[0] = 0
    for price, pattern in juices:
        for have in range(8):
            if cost[have] == infinity:
                continue
            total = cost[have] + price
            if total < cost[have | pattern]:
                cost[have | pattern] = total
    return -1 if cost[7] == infinity else cost[7]


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % cheapest_set(read_input()))


if __name__ == "__main__":
    main()
