import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    s = tokens[2]
    t = tokens[3]
    cars = []
    pos = 4
    for _ in range(n):
        cars.append((tokens[pos], tokens[pos + 1]))
        pos += 2
    stations = sorted(tokens[pos:pos + k])
    return s, t, cars, stations


# --- clause: travel_time :: (tank: int, s: int, stations: list[int]) -> int ---
def travel_time(tank, s, stations):
    spots = [0] + stations + [s]
    amount = 0
    for i in range(1, len(spots)):
        gap = spots[i] - spots[i - 1]
        if tank < gap:
            return 1 << 62
        fast = tank - gap
        if fast > gap:
            fast = gap
        amount += 2 * gap - fast
    return amount


# --- clause: cheapest_car :: (s: int, t: int, cars: list[tuple[int, int]], stations: list[int]) -> int ---
def cheapest_car(s, t, cars, stations):
    low = 1
    high = 2 * s
    while low < high:
        mid = (low + high) // 2
        if travel_time(mid, s, stations) <= t:
            high = mid
        else:
            low = mid + 1
    if travel_time(low, s, stations) > t:
        return -1
    best = -1
    for price, tank in cars:
        if tank >= low and (best < 0 or price < best):
            best = price
    return best


# --- clause: main :: () -> None ---
def main():
    s, t, cars, stations = read_input()
    sys.stdout.write("%d\n" % cheapest_car(s, t, cars, stations))


if __name__ == "__main__":
    main()
