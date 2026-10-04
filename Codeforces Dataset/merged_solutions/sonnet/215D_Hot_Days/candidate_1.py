import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    regions = []
    for i in range(n):
        regions.append((data[2 + 4 * i], data[3 + 4 * i], data[4 + 4 * i], data[5 + 4 * i]))
    return m, regions


# --- clause: region_cost :: (m: int, warm: int, limit: int, fee: int, price: int) -> int ---
def region_cost(m, warm, limit, fee, price):
    together = price + m * fee
    if limit <= warm:
        return together
    room = limit - warm
    buses = (m + room - 1) // room
    split = buses * price
    return split if split < together else together


# --- clause: main :: () -> None ---
def main():
    m, regions = read_input()
    total = 0
    for warm, limit, fee, price in regions:
        total += region_cost(m, warm, limit, fee, price)
    sys.stdout.write("%d\n" % total)


if __name__ == "__main__":
    main()
