import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    regions = []
    for i in range(n):
        regions.append((tokens[2 + 4 * i], tokens[3 + 4 * i], tokens[4 + 4 * i], tokens[5 + 4 * i]))
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
    amount = 0
    for warm, limit, fee, price in regions:
        amount += region_cost(m, warm, limit, fee, price)
    sys.stdout.write("%d\n" % amount)


if __name__ == "__main__":
    main()
