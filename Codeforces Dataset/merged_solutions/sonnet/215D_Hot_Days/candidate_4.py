import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int, int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    regions = []
    for i in range(n):
        regions.append((numbers[2 + 4 * i], numbers[3 + 4 * i], numbers[4 + 4 * i], numbers[5 + 4 * i]))
    return m, regions


# --- clause: region_cost :: (m: int, warm: int, limit: int, fee: int, price: int) -> int ---
def region_cost(m, warm, limit, fee, price):
    best = price + m * fee
    room = limit - warm
    if room > 0:
        buses = m // room
        if m % room:
            buses += 1
        if buses * price < best:
            best = buses * price
    return best


# --- clause: main :: () -> None ---
def main():
    m, regions = read_input()
    summed = 0
    for warm, limit, fee, price in regions:
        summed += region_cost(m, warm, limit, fee, price)
    sys.stdout.write("%d\n" % summed)


if __name__ == "__main__":
    main()
