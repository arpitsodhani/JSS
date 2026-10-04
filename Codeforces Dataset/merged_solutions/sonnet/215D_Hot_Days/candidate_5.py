import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    regions = []
    for i in range(n):
        regions.append((raw[2 + 4 * i], raw[3 + 4 * i], raw[4 + 4 * i], raw[5 + 4 * i]))
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
    running = 0
    for warm, limit, fee, price in regions:
        running += region_cost(m, warm, limit, fee, price)
    sys.stdout.write("%d\n" % running)


if __name__ == "__main__":
    main()
