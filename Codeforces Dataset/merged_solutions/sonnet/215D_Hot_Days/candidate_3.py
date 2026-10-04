import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    regions = []
    for i in range(n):
        regions.append((fields[2 + 4 * i], fields[3 + 4 * i], fields[4 + 4 * i], fields[5 + 4 * i]))
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
    tally = 0
    for warm, limit, fee, price in regions:
        tally += region_cost(m, warm, limit, fee, price)
    sys.stdout.write("%d\n" % tally)


if __name__ == "__main__":
    main()
